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


class Directions(Enum):
    """docstring for Directions."""
    NORTH_WEST = (-1, -1)
    NORTH = (0, -1)
    NORTH_EAST = (1, -1)
    EAST = (1, 0)
    SOUTH_EAST = (1, 1)
    SOUTH = (0, 1)
    SOUTH_WEST = (-1, 1)
    WEST = (-1, 0)


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
