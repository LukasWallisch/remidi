from enum import Enum, auto
from remidi.games.reversi.enums.board_enums import TileState


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
            return PlayerType.NOBODY

    @property
    def tile_state(self):
        if self is PlayerType.PLAYER_1:
            return TileState.PLAYER_1
        elif self is PlayerType.PLAYER_2:
            return TileState.PLAYER_2
        else:
            return TileState.EMPTY
