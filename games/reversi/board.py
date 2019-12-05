import mylogging

from games.reversi.enums.board_enums import TileState
from games.reversi.enums.players import PlayerType
from games.board import Board

logger = mylogging.setup_logger("Board")


class ReversiBoard(Board):
    """docstring for Board."""

    def __init__(self):
        super(ReversiBoard, self).__init__()
        self.reset()

    @property
    def current_scores(self):
        p1_score = 0
        p2_score = 0
        empty = 0
        for tile in self.board_list:
            if tile.owner is PlayerType.PLAYER_1:
                p1_score += 1
            elif tile.owner is PlayerType.PLAYER_2:
                p2_score += 1
            elif tile.owner is PlayerType.NOBODY:
                empty += 1
            else:
                raise TypeError("Wrong Playertype on Board")
        return (p1_score, p2_score, empty)

    def possible_for_player(self, player):
        if not isinstance(player, PlayerType):
            raise TypeError("Type should be PlayerType, not: "
                            + str(type(player)))
        elif player is PlayerType.NOBODY:
            raise ValueError("PlayerType must not be NOBODY!")
        else:
            directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
            logger.debug(directions)
            for d in directions:
                logger.debug(d)

    def check_direction_possible(self, direction):
        pass

    def check_tile(self, tile):
        if not isinstance(tile, TileState):
            error = TypeError("tile_state must be from type 'TileState' not: "
                              + str(type(tile)))
            return False, error
        else:
            return True, None

    def copy(self):
        board = ReversiBoard()
        board.board = self.board
        return board

    def reset(self):
        self.board = [
            [TileState.EMPTY for i in range(0, 8)]for i in range(0, 8)]
        self.set_tile(3, 3, TileState.PLAYER_1)
        self.set_tile(3, 4, TileState.PLAYER_2)
        self.set_tile(4, 3, TileState.PLAYER_2)
        self.set_tile(4, 4, TileState.PLAYER_1)
