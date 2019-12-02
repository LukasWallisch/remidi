from remidi_enums.tile_states import tile_state
from remidi_enums.layout_objects import BarType
from remidi_enums.colors import colors
from tabulate import tabulate
import mylogging

logger = mylogging.setup_logger("layouts")


class view_grid(object):
    """docstring for note_grid."""

    def __init__(self):
        self._grid = [[tile_state.EMPTY for x in range(8)] for y in range(8)]

    @property
    def grid(self):
        return self._grid

    def set_tiles(self, tile_list):
        raise NotImplementedError("comming soon")

    def __str__(self):
        output_header = list(range(1, 9))
        output_header.append("row")
        output_data = []
        rows = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i, row in enumerate(self.grid):
            out_row = []
            for tile in row:
                out_row.append(str(tile))

            out_row.append(str(rows[i]))
            output_data.append(out_row)
        return "\n" + tabulate(output_data, output_header)


class view_bar(object):
    """docstring for note_grid."""

    def __init__(self, bar_type):
        self._bar = [colors.BLACK for x in range(8)]
        if isinstance(bar_type, BarType):
            self.header = bar_type.header()
            logger.debug(self.header)

    @property
    def bar(self):
        return self._bar

    def set_tiles(self, tile_list):
        raise NotImplementedError("comming soon")

    def __str__(self):
        output_header = self.header
        output_data = []
        output_row = []
        for tile in self.bar:
            output_row.append(str(tile))
        output_data.append(output_row)
        return "\n" + tabulate(output_data, output_header)


class view_v_bar(view_bar):
    """docstring for note_grid."""

    def __init__(self):
        super(view_v_bar, self).__init__(BarType.VERTICAL)


class view_h_bar(view_bar):
    """docstring for note_grid."""

    def __init__(self):
        super(view_h_bar, self).__init__(BarType.HORIZONTAL)
