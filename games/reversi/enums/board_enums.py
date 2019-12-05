from games.reversi.enums.players import PlayerType
from enum import Enum, auto


class TileState(Enum):
    """docstring for TileState."""
    EMPTY = auto()
    PLAYER_1 = auto()
    PLAYER_2 = auto()
    POSSIBLE = auto()

    @property
    def owner(self):
        if self is TileState.PLAYER_1:
            return PlayerType.PLAYER_1
        elif self is TileState.PLAYER_2:
            return PlayerType.PLAYER_2
        elif self is TileState.EMPTY:
            return PlayerType.NOBODY
        else:
            return None

    def __str__(self):
        return self.name[0]+self.name[-1]

    def __repr__(self):
        return self.name[0]+self.name[-1]
