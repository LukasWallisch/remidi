from tabulate import tabulate
from itertools import chain

import mylogging


logger = mylogging.setup_logger("Board")


class Board(object):
    """docstring for Board."""

    def __init__(self):
        self.__board = [
            [None for i in range(0, 8)]for i in range(0, 8)]

    @property
    def board(self):
        return self.__board

    @property
    def board_list(self):
        return list(chain.from_iterable(self.board))

    @property
    def current_scores(self):
        raise NotImplementedError("This is the Default Board, "
                                  + "no score evaluation implemented!")

    @board.setter
    def board(self, board):
        new_board = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                tile = board[x][y]
                type_ok, error = self.check_tile(tile)
                if type_ok:
                    row.append(tile)
                else:
                    raise error
            new_board.append(row)
        self.__board = new_board

    def get_data(self):
        data = [[str(tile) for tile in row] for row in self.board]
        output = tabulate(data, tablefmt="grid")
        return "\n"+output

    def __str__(self):
        return str(self.get_data())

    def set_tile(self, x, y, tile_state):
        type_ok, error = self.check_tile(tile_state)
        if x > 7 or y > 7:
            raise ValueError("x and y Coordinates must be in [0,7]")
        elif not type_ok:
            raise error
        else:
            self.board[x][y] = tile_state

    def check_tile(self, tile):
        return True, None

    def copy(self):
        board = Board()
        board.board = self.board
        return board

    def reset(self):
        self.board = [
            [None for i in range(0, 8)]for i in range(0, 8)]
