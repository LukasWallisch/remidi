import mylogging

from enum import Enum
from remidi_view.view_enums.colors import Colors

logger = mylogging.setup_logger("DisplayChars")

class MyEnum(Enum):
    def __str__(self):
        return self.name


class DisplayChars():

    chars = {"0": [[True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "1": [[False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False]],

             "2": [[True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False]],

             "3": [[True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, True, False]],

             "4": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False]],

             "5": [[True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, True, False]],

             "6": [[True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "7": [[True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False]],

             "8": [[True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "9": [[True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, True, False]],


             "A": [[False, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "B": [[True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, False, False]],

             "C": [[False, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [False, True, True, False]],

             "E": [[True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False]],

             "F": [[True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False]],

             "G": [[True, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "H": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "I": [[False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False]],

             "J": [[True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, False, False]],

             "K": [[True, False, True, False],
                   [True, False, True, False],
                   [True, True, False, False],
                   [True, False, False, False],
                   [True, True, False, False],
                   [True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "L": [[True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False]],

             "M": [[True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "N": [[True, False, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [False, False, True, False]],

             "O": [[True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "P": [[True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False]],

             "Q": [[False, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [False, False, True, False]],

             "R": [[True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, False, False],
                   [True, True, False, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "S": [[False, True, True, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [False, True, False, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [True, True, False, False]],

             "T": [[True, True, True, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False]],

             "U": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False]],

             "V": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [False, True, False, False]],

             "W": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, False, True, False]],

             "X": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, True, True, False],
                   [True, True, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False]],

             "Y": [[True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [True, False, True, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False],
                   [False, True, False, False]],

             "Z": [[True, True, True, False],
                   [False, False, True, False],
                   [False, False, True, False],
                   [False, True, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, False, False, False],
                   [True, True, True, False]]}


class CharDisplay():
    def __init__(self, charlist):
        self.charlist = []
        self.offset = 0
        self.display = [[],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        []]
        for c in charlist:
            self.concat(c)

    def concat(self, char):
        next_char = DisplayChars.chars[char]
        logger.debug(char)
        logger.debug(next_char)
        for r in range(8):
            self.display[r].extend(next_char[r])

    def get_grid(self, color):
        grid = []
        for r in range(8):
            row = []
            for c in range(8):
                try:
                    tile = self.display[r][c+self.offset]
                except IndexError:
                    tile = False
                if tile is True:
                    row.append(color)
                else:
                    row.append(Colors.BLACK)
            grid.append(row)
        if len(self.display[0])-8 > 0:
            self.offset += 1
            if len(self.display[0])-8 <= self.offset:
                self.offset = 0
        return grid
