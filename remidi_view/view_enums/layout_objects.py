from enum import Enum, auto


class BarType(Enum):
    """docstring for TileState."""
    VERTICAL = auto()
    HORIZONTAL = auto()

    def header(self):
        if self is BarType.VERTICAL:
            return ["a", "b", "c", "d", "e", "f", "g", "h"]
        elif self is BarType.HORIZONTAL:
            return list(map((lambda x: str(x)), range(1, 9)))
        else:
            raise ValueError("Unknown bar_type: " + str(self))


class TileType(Enum):
    NOTE = auto()
    CONTROL = auto()


class TileGroup(Enum):
    NOTE_GRID = auto()
    NOTE_BAR = auto()
    CONTROL_BAR = auto()


class TileAction(Enum):
    PRESS = auto()
    RELEASE = auto()
