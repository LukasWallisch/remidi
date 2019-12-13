import mylogging
import time
import random
from tabulate import tabulate

from games.reversi.board import ReversiBoard
from games.reversi.enums import PlayerType

from remidi_view.lauchpad import LaunchpadMiniMk2
from remidi_view.view_enums.layout_objects import TileGroup
from remidi_view.view_enums.colors import Colors

logger = mylogging.setup_logger("reversi")


class Reversi(object):
    """docstring for Reversi."""

    def __init__(self, player, ai_opponent=0):
        self.board = ReversiBoard()
        self.launchpad = LaunchpadMiniMk2()
        self.ai_opponent = ai_opponent
        if ai_opponent == 1:
            # flipped because of function of next_step
            self.current_player = player
            self.start_player = player
            self.ai_player = player.opponent
        elif ai_opponent == 2:
            # flipped because of function of next_step
            self.current_player = player.opponent
            self.start_player = player.opponent
            self.ai_player = player
        else:
            # flipped because of function of next_step
            self.current_player = player.opponent
            self.start_player = player.opponent
            self.ai_player = PlayerType.NOBODY
        self.show_possibles = True
        self.steps = []

    @property
    def ai_opponent(self):
        return self._ai_opponent

    @ai_opponent.setter
    def ai_opponent(self, value):
        if value in range(0, 3):
            self._ai_opponent = value
        else:
            table = tabulate([(0, "No Ai"),
                              (1, "Ai beginns game"),
                              (2, "PLAYER beginns game")],
                             ["value", "meaning"])
            raise ValueError("ai_opponent can only have following values "
                             + "with corresponding meaning:\n"+table)

    @property
    def current_player(self):
        return self._current_player

    @current_player.setter
    def current_player(self, player):
        if isinstance(player, PlayerType):
            self._current_player = player
        else:
            raise TypeError("current_player must be from type PlayerType not: "
                            + str(type(player)))

    def run(self):
        keep_running = True
        self.steps.append((self.board.copy(), self.current_player))
        while keep_running is True:
            keep_running = self.step()
        # logger.debug(self.steps)

    def step(self):
        dp_board, possible_tiles, player = self.next_step(
            self.current_player)
        self.current_player = player
        self.display_vertical_bar(dp_board)
        self.display_horizontal_bar()
        logger.debug(
            "\nPlayer: %s\nPossible Moves: %s\n Current Score: %s\n%s" %
            (str(player), str(possible_tiles), str(self.board.current_scores),
             str(dp_board)))

        if self.current_player in [PlayerType.PLAYER_1, PlayerType.PLAYER_2]:
            if player is self.ai_player:
                self.display_board(self.board)
                # time.sleep(0.2)
                x, y = random.choice(possible_tiles)
            else:
                self.display_board(dp_board)
                position, keep_running = self.get_player_move(possible_tiles)
                if keep_running is False:
                    return False
                else:
                    if position:
                        x, y = position
                    else:
                        return True
            self.board.do_move(x, y, self.current_player)
            if self.current_player is not self.ai_player:
                self.steps.append((self.board.copy(), self.current_player))
            return True

        else:
            self.display_board(self.board)
            logger.debug("Game Finished")
            tile_event = self.launchpad.get_input()
            if tile_event.group is TileGroup.NOTE_GRID \
                    or(tile_event.group is TileGroup.CONTROL_BAR
                       and tile_event.position == 6):
                self.steps = []
                self.board.reset()
                self.current_player = self.start_player
                return True
            elif tile_event.group is TileGroup.CONTROL_BAR \
                    and tile_event.position == 5:
                self.steps.pop()
                board, player = self.steps.pop()
                logger.debug(board)
                logger.debug(player)
                self.board = board
                self.current_player = player
                self.steps.append((self.board.copy(), self.current_player))
                return True
            else:
                return False

    def next_step(self, current_player, initial=True):
        """Retruns the next player, if there isn't a valid move for any
        player, the game is finished."""
        next_player = current_player.opponent
        b, possible_tiles = self.board.possible_tiles(next_player)
        if len(possible_tiles) == 0:
            if initial is True:
                logger.debug(
                    "skipped next_player: %s  because of no possible moves."
                    % next_player)
                return self.next_step(next_player, False)
            else:
                return b, possible_tiles, PlayerType.NOBODY
        else:
            return (b, possible_tiles, next_player)

    def get_player_move(self, possible_tiles):
        tile_event = self.launchpad.get_input()
        if tile_event.group is TileGroup.NOTE_GRID:
            position = tile_event.position
            if position in possible_tiles:
                return position, True
            else:
                self.display_error("Unallowed Move!")
                return self.get_player_move(possible_tiles)
        else:
            return self.handle_control_input(tile_event, possible_tiles)

    def handle_control_input(self, tile_event, possible_tiles):
        if tile_event.group is TileGroup.CONTROL_BAR:
            if tile_event.position == 7:
                logger.info("exit reversi")
                return None, False
            elif tile_event.position == 6:
                logger.info("reset reversi")
                self.board.reset()
                self.steps = []
                self.steps.append((self.board.copy(), self.current_player))
                return None, True
            elif tile_event.position == 5:
                logger.info("undo last move")
                logger.debug(len(self.steps))
                if len(self.steps) >= 2:
                    self.steps.pop()
                    board, player = self.steps.pop()
                    logger.debug(board)
                    logger.debug(player)
                    self.board = board
                    self.current_player = player
                    self.steps.append((self.board.copy(), self.current_player))
                    return None, True
                else:
                    return self.get_player_move(possible_tiles)
                    logger.debug("not enough steps for undo")
            else:
                return self.get_player_move(possible_tiles)
        elif tile_event.group is TileGroup.NOTE_BAR:
            pass
        else:
            return self.get_player_move(possible_tiles)
        logger.info()

    def display_board(self, board):
        grid = []
        for row_id in range(0, 8):
            row = []
            for col_id in range(0, 8):
                color = board.board[row_id][col_id].color
                # tile = board.board[row_id][col_id]
                # logger.debug("row: %s, col: %s, tile: %s, color: %s"
                #              % (str(row_id), str(col_id), str(tile), str(color)))
                row.append(color)
            grid.append(row)

        self.launchpad.display_grid_on_notegrid(grid)

    def display_vertical_bar(self, board):
        color = self.current_player.tile_state.color
        score = board.score_for_player(self.current_player)
        bar = []
        for digit in format(score, '08b'):
            if digit == "1":
                bar.append(color)
            else:
                bar.append(Colors.BLACK)
        self.launchpad.display_on_note_bar(bar)

    def display_horizontal_bar(self):
        bar = [Colors.BLACK]*5
        if len(self.steps) >= 2:
            bar.append(Colors.GREEN)
        else:
            bar.append(Colors.BLACK)
        bar.append(Colors.ORANGE)
        bar.append(Colors.RED)
        self.launchpad.display_on_control_bar(bar)

    def display_error(self, error_msg):
        logger.info(error_msg)
