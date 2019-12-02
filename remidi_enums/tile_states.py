from enum import Enum, auto


class tile_state(Enum):
    """docstring for tile_state."""
    EMPTY = auto()
    PLAYER_1 = auto()
    PLAYER_2 = auto()
    POSSIBLE = auto()

    def __str__(self):

        return self.name[0]+self.name[-1]
