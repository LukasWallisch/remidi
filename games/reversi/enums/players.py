from enum import Enum, auto


class PlayerType(Enum):
    """docstring for PlayerType."""
    PLAYER_1 = auto()
    PLAYER_2 = auto()
    NOBODY = auto()

    def __str__(self):
        return self.name[0]+self.name[-1]

    @property
    def opponent(self):
        if self is PlayerType.PLAYER_1:
            return PlayerType.PLAYER_2
        elif self is PlayerType.PLAYER_2:
            return PlayerType.PLAYER_1
        else:
            raise ValueError("PlayerType NOBODY has no opponent! ")
