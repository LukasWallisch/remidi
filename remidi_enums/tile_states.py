from enum import Enum, auto


class TileState(Enum):
    """docstring for TileState."""
    EMPTY = auto()
    PLAYER_1 = auto()
    PLAYER_2 = auto()
    POSSIBLE = auto()

    def __str__(self):
        return self.name[0]+self.name[-1]
