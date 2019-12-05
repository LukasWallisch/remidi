from enum import Enum, auto


class PlayerType(Enum):
    """docstring for PlayerType."""
    PLAYER_1 = auto()
    PLAYER_2 = auto()
    NOBODY = auto()

    def __str__(self):
        return self.name[0]+self.name[-1]
