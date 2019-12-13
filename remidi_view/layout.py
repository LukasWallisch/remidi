from remidi_view.view_enums.layout_objects import BarType
from remidi_view.view_enums.layout_objects import TileType
from remidi_view.view_enums.layout_objects import TileAction
from remidi_view.view_enums.layout_objects import TileGroup
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


class TileEvent(object):
    """docstring for note_grid."""

    def __init__(self, tile_type, action, position, tile_group):
        self.type = tile_type
        self.action = action
        self.group = tile_group
        self.position = position

    @property
    def type(self):
        return self.__tile_type

    @type.setter
    def type(self, tile_type):
        if isinstance(tile_type, TileType):
            self.__tile_type = tile_type
        else:
            raise TypeError("tile_type can only be type TileType not: "
                            + str(type(tile_type)))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        logger.debug(position)
        if self.group is TileGroup.NOTE_GRID \
                and isinstance(position, tuple):
            self.__position = position
        elif self.group in [TileGroup.NOTE_BAR, TileGroup.CONTROL_BAR] \
                and isinstance(position, int):
            self.__position = position
        else:
            raise ValueError("position has wrong format")

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        if isinstance(action, TileAction):
            self.__action = action
        else:
            raise TypeError("action can only be type TileAction not: "
                            + str(type(action)))

    @property
    def group(self):
        return self.__tile_group

    @group.setter
    def group(self, tile_group):
        if isinstance(tile_group, TileGroup):
            self.__tile_group = tile_group
        else:
            raise TypeError("tile_group can only be type TileGroup not: "
                            + str(type(tile_group)))

    def __str__(self):
        output = ("TileEvent:\ntype: %5s Action: %11s pos: %s group: %s"
                  % (self.type, self.action, str(self.position), str(self.group)))
        return output
