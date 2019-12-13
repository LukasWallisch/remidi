import mylogging

from games.reversi.enums import TileState
from games.reversi.enums import Directions
from games.reversi.enums import PlayerType
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

    def score_for_player(self, player):
        if player is PlayerType.PLAYER_1:
            score = self.current_scores[0]
        elif player is PlayerType.PLAYER_2:
            score = self.current_scores[1]
        elif player is PlayerType.NOBODY:
            score = self.current_scores[2]
        else:
            raise TypeError("Wrong Playertype on given")
        return score

    def possible_tiles(self, player):
        if not isinstance(player, PlayerType):
            raise TypeError("Type should be PlayerType, not: "
                            + str(type(player)))
        elif player is PlayerType.NOBODY:
            raise ValueError("PlayerType must not be NOBODY!")
        else:
            result_board = []
            possible_list = []
            for row in range(0, 8):
                row_r = []
                for col in range(0, 8):
                    if not self.board[row][col] is TileState.EMPTY:
                        row_r.append(self.board[row][col])
                    else:
                        direction_result = TileState.EMPTY
                        for d in Directions:
                            direction_result = self._tile_possible(
                                d, row, col, player)
                            if direction_result is TileState.POSSIBLE:
                                possible_list.append((row, col))
                                break
                        row_r.append(direction_result)
                result_board.append(row_r)
            possible_board = ReversiBoard()
            possible_board.board = result_board
            return possible_board, possible_list

    def _tile_possible(self, direction, row, col, player, initial=True):
        d_row, d_col = direction.value
        row += d_row
        col += d_col
        if not (row >= 0 and row < 8 and col >= 0 and col < 8):
            # logger.debug("not on Board")
            return TileState.EMPTY
        # else:
        #     logger.debug("d: %s r: %s c: %s p: %s i: %s t: %s" %
        #                  (direction, row, col, player,
        #                   initial, self.board[row][col]))
        if initial is True:
            if self.board[row][col].owner is player.opponent:
                # logger.debug("next step:")
                return self._tile_possible(direction, row, col, player, False)
            else:
                # logger.debug("Tile rejected")
                return TileState.EMPTY
        else:
            if self.board[row][col].owner is player:
                # logger.debug("Tile accepted")
                return TileState.POSSIBLE
            elif self.board[row][col].owner is player.opponent:
                # logger.debug("next step:")
                return self._tile_possible(direction, row, col, player, False)
            else:
                # logger.debug("Tile rejected")
                return TileState.EMPTY

    def _set_direction_tiles(self, direction, row, col, player, initial=True):
        d_row, d_col = direction.value
        row += d_row
        col += d_col
        if not (row >= 0 and row < 8 and col >= 0 and col < 8):
            # logger.debug("not on Board")
            return False
        # else:
        #     logger.debug("d: %s r: %s c: %s p: %s i: %s t: %s" %
        #                  (direction, row, col, player,
        #                   initial, self.board[row][col]))
        if initial is True:
            if self.board[row][col].owner is player.opponent:
                # logger.debug("next step:")
                if self._set_direction_tiles(direction, row,
                                            col, player, False):
                    self.board[row][col] = player.tile_state
                    return True
            else:
                # logger.debug("Tile rejected")
                return False
        else:
            if self.board[row][col].owner is player:
                # logger.debug("Tile accepted")
                self.board[row][col] = player.tile_state
                return True
            elif self.board[row][col].owner is player.opponent:
                # logger.debug("next step:")
                if self._set_direction_tiles(direction, row,
                                            col, player, False):
                    self.board[row][col] = player.tile_state
                    return True
            else:
                # logger.debug("Tile rejected")
                return False

    def check_tile(self, tile):
        if not isinstance(tile, TileState):
            error = TypeError("tile_state must be from type 'TileState' not: "
                              + str(type(tile)))
            return False, error
        else:
            return True, None

    def set_tile(self, x, y, player):
        super(ReversiBoard, self).set_tile(x, y, player.tile_state)

    def do_move(self, row, col, player):
        self.set_tile(row, col, player)
        for d in Directions:
            self._set_direction_tiles(d, row, col, player)

    def copy(self):
        board = ReversiBoard()
        board.board = self.board
        return board

    def reset(self):
        self.board = [
            [TileState.EMPTY for i in range(0, 8)]for i in range(0, 8)]
        self.set_tile(3, 3, PlayerType.PLAYER_1)
        self.set_tile(3, 4, PlayerType.PLAYER_2)
        self.set_tile(4, 3, PlayerType.PLAYER_2)
        self.set_tile(4, 4, PlayerType.PLAYER_1)
