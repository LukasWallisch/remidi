from enum import Enum, auto


class BarType(Enum):
    """docstring for tile_state."""
    VERTICAL = auto()
    HORIZONTAL = auto()

    def header(self):
        if self is BarType.VERTICAL:
            return ["a", "b", "c", "d", "e", "f", "g", "h"]
        elif self is BarType.HORIZONTAL:
            return list(map((lambda x: str(x)), range(1, 9)))
        else:
            raise ValueError("Unknown bar_type: " + str(self))
