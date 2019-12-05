from remidi_view.view_enums.layout_objects import BarType
from remidi_view.view_enums.colors import Colors
from tabulate import tabulate
import mylogging

logger = mylogging.setup_logger("layouts")


class ViewGrid(object):
    """docstring for note_grid."""

    def __init__(self):
        self._grid = [[Colors.BLACK for x in range(8)] for y in range(8)]

    @property
    def grid(self):
        return self._grid

    def display_board(self, board):
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


class ViewBar(object):
    """docstring for note_grid."""

    def __init__(self, bar_type):
        self._bar = [Colors.BLACK for x in range(8)]
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


class ViewVBar(ViewBar):
    """docstring for note_grid."""

    def __init__(self):
        super(ViewVBar, self).__init__(BarType.VERTICAL)


class ViewHBar(ViewBar):
    """docstring for note_grid."""

    def __init__(self):
        super(ViewHBar, self).__init__(BarType.HORIZONTAL)
