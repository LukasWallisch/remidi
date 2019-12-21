import mylogging
import mido
from itertools import chain

import time
import json
from remidi_view.view_enums.colors import Colors
from remidi_view.view_enums.colors import RG_Colors
from remidi_view.view_enums.layout_objects import TileType
from remidi_view.view_enums.layout_objects import TileAction
from remidi_view.view_enums.layout_objects import TileGroup
from remidi_view.view_enums.display_chars import DisplayChars
from remidi_view.view_enums.display_chars import CharDisplay
from remidi_view.layout import TileEvent

import config

logger = mylogging.setup_logger("launchpad")


class Launchpad(object):
    """docstring for Launchpad_con."""

    def __init__(self):
        self.counter = 0
        self.note_timer = {}
        self.control_timer = {}
        self.reset_all()

    def __del__(self):
        self.reset_all()

    @property
    def note_grid(self):
        return self._note_grid

    @property
    def note_bar(self):
        return self._note_bar

    @property
    def control_bar(self):
        return self._control_bar

    def _get_note_grid_reset_msg(self):
        msg_list = []
        for row_id in range(0, 8):
            for col_id in range(0, 8):
                msg = self._get_note_grid_msg(row_id, col_id, Colors.BLACK)
                msg_list.append(msg)
        return msg_list

    def _get_note_bar_reset_msg(self):
        msg_list = []
        for b_id, button in enumerate(self.note_bar):
            msg = self._get_note_bar_msg(b_id, Colors.BLACK)
            msg_list.append(msg)
        return msg_list

    def _get_control_bar_reset_msg(self):
        msg_list = []
        for b_id, button in enumerate(self.control_bar):
            msg = self._get_control_bar_msg(b_id, Colors.BLACK)
            msg_list.append(msg)
        return msg_list

    def _get_note_grid_msg(self, row_id, col_id, color):
        if isinstance(color, (Colors, RG_Colors)):
            logger.debug("msg for set row: " + str(row_id)
                         + " col: " + str(col_id)
                         + " to color: " + str(color))

            msg = mido.Message(
                "note_on", note=self.py2midi_grid_tile_id(row_id, col_id),
                velocity=color.value)
        else:
            raise TypeError("Grid must only contain Colors Objects!"
                            + " not: " + str(type(color)))
        return msg

    def _get_note_bar_msg(self, b_id, color):
        if isinstance(color, (Colors, RG_Colors)):
            logger.debug("msg for set note_bar_button: " + str(b_id)
                         + " to color: " + str(color))
            msg = mido.Message("note_on",
                               note=self.py2midi_note_bar_tile_id(b_id),
                               velocity=color.value)
        else:
            raise TypeError("Grid must only contain Colors Objects!"
                            + " not: " + str(type(color)))
        return msg

    def _get_control_bar_msg(self, b_id, color):
        if isinstance(color, (Colors, RG_Colors)):
            logger.debug("msg for set control_bar_button: " + str(b_id)
                         + " to color: " + str(color))
            msg = mido.Message("control_change",
                               control=self.py2midi_control_bar_tile_id(b_id),
                               value=color.value)
        else:
            raise TypeError("Grid must only contain Colors Objects!"
                            + " not: " + str(type(color)))
        return msg

    def reset_all(self):
        msg_list = []
        msg_list.extend(self._get_note_grid_reset_msg())
        msg_list.extend(self._get_note_bar_reset_msg())
        msg_list.extend(self._get_control_bar_reset_msg())
        self.send_to_launchpad(msg_list)

    def display_grid_on_notegrid(self, grid):
        msg_list = []
        for row in range(0, 8):
            for col in range(0, 8):
                msg_list.append(self._get_note_grid_msg(
                    row, col, grid[row][col]))
        self.send_to_launchpad(msg_list)

    def display_text_on_notegrid(self, text, color):
        text = str(text)
        cd = CharDisplay(text.upper())
        if len(text) <= 2:
            grid = cd.get_grid(color)
            self.display_grid_on_notegrid(grid)
        else:
            for dp_steps in range((len(text)-2)*4):
                grid = cd.get_grid(color)
                self.display_grid_on_notegrid(grid)
                time.sleep(0.1)

    def display_on_note_bar(self, bar):
        msg_list = []
        for b_id in range(0, 8):
            msg_list.append(self._get_note_bar_msg(b_id, bar[b_id]))
        self.send_to_launchpad(msg_list)

    def display_on_control_bar(self, bar):
        msg_list = []
        for b_id in range(0, 8):
            msg_list.append(self._get_control_bar_msg(b_id, bar[b_id]))
        self.send_to_launchpad(msg_list)

    def send_to_launchpad(self, msg_list):
        if isinstance(msg_list, list) and len(msg_list) > 0:
            try:
                with mido.open_output(config.Launchpad_output) as outport:
                    # logger.debug("Send to Launchpad: "+str(msg_list))
                    if isinstance(msg_list[0], mido.Message):
                        for msg in msg_list:
                            outport.send(msg)
                    else:
                        raise TypeError(
                            "msg list must only contain "
                            + "mido.Message, not: " + type(msg))
            except IOError as e:
                logger.error("The outport: "+config.Launchpad_output
                             + "doesn't exist. Currently aviable: "
                             + str(mido.get_output_names()))
                raise e
        else:
            raise TypeError("msg_list must be a list, not: "+type(msg))

    def get_input(self):
        try:
            with mido.open_input(config.Launchpad_input) as inport:
                for in_msg in inport:
                    if in_msg.type == "note_on":
                        tile = in_msg.note
                        tile_type = TileType.NOTE
                        value = in_msg.velocity
                    elif in_msg.type == "control_change":
                        tile = in_msg.control
                        tile_type = TileType.CONTROL
                        value = in_msg.value
                    else:
                        raise ValueError("Unknown msg.type: "
                                         + str(in_msg.type))

                    tile_group = self.get_tile_group(tile, tile_type)

                    if value == 127:
                        action = TileAction.PRESS
                    elif value == 0:
                        action = TileAction.RELEASE
                        tile_press = TileEvent(
                            tile_type,
                            action,
                            self.midi2py_tile_id(tile, tile_group),
                            tile_group)
                        return tile_press
                    else:
                        raise ValueError("Unknown Value: %s for tile: %d"
                                         % str(value), tile)
        except IOError as e:
            logger.error("The inport: "+config.Launchpad_output
                         + "doesn't exist. Currently aviable: "
                         + str(mido.get_input_names()))
            raise e


class LaunchpadMiniMk2(Launchpad):
    """docstring for LaunchpadMiniMk2."""

    def __init__(self):
        self._note_grid = [range(0, 8),
                           range(16, 24),
                           range(32, 40),
                           range(48, 56),
                           range(64, 72),
                           range(80, 88),
                           range(96, 104),
                           range(112, 120)]
        self._note_bar = range(8, 121, 16)
        self._control_bar = range(104, 112)
        super(LaunchpadMiniMk2, self).__init__()

    @staticmethod
    def py2midi_grid_tile_id(row, col):
        id = row*16+col
        logger.debug("py2midi for grid tile at (%d,%d) tile_id is: %3d"
                     % (row, col, id))
        return id

    @staticmethod
    def py2midi_note_bar_tile_id(b_id):
        id = b_id*16+8
        logger.debug("py2midi for note_bar button '%d' tile_id is: %3d"
                     % (b_id, id))
        return id

    @staticmethod
    def py2midi_control_bar_tile_id(b_id):
        id = 6*16+8+b_id
        logger.debug("py2midi for control_bar button '%d' tile_id is: %3d"
                     % (b_id, id))
        return id

    @staticmethod
    def midi2py_grid_tile_id(id):
        row = id//16
        col = id % 16
        logger.debug("midi2py for tile_id: '%3d' grid_pos is: (%d,%d)"
                     % (id, row, col))
        return row, col

    @staticmethod
    def midi2py_note_bar_tile_id(id):
        b_id = (id-8)//16
        logger.debug("midi2py for tile_id '%3d' note_bar button is: %d"
                     % (id, b_id))
        return b_id

    @staticmethod
    def midi2py_control_bar_tile_id(id):
        b_id = id - (8+6*16)
        logger.debug("midi2py for tile_id '%3d' control_bar button is: %d"
                     % (id, b_id))
        return b_id

    @staticmethod
    def midi2py_tile_id(tile_id, tile_group):
        logger.debug(tile_id)
        logger.debug(tile_group)
        if tile_group is TileGroup.NOTE_GRID:
            return LaunchpadMiniMk2.midi2py_grid_tile_id(tile_id)
        elif tile_group is TileGroup.NOTE_BAR:
            return LaunchpadMiniMk2.midi2py_note_bar_tile_id(tile_id)
        elif tile_group is TileGroup.CONTROL_BAR:
            return LaunchpadMiniMk2.midi2py_control_bar_tile_id(tile_id)

    def tile_on_note_grid(self, tile_id, tile_type):
        id_ok = tile_id in list(chain.from_iterable(self._note_grid))
        type_ok = tile_type is TileType.NOTE
        logger.debug("id_ok: %s - type_ok: %s" % (id_ok, type_ok))
        return id_ok and type_ok

    def tile_on_note_bar(self, tile_id, tile_type):
        id_ok = tile_id in self._note_bar
        type_ok = tile_type is TileType.NOTE
        return id_ok and type_ok

    def tile_on_control_bar(self, tile_id, tile_type):
        id_ok = tile_id in self._control_bar
        type_ok = tile_type is TileType.CONTROL
        logger.debug("id_ok %s type_ok %s" % (id_ok, type_ok))
        return id_ok and type_ok

    def get_tile_group(self, tile, tile_type):
        if self.tile_on_note_grid(tile, tile_type):
            tile_group = TileGroup.NOTE_GRID
        elif self.tile_on_note_bar(tile, tile_type):
            tile_group = TileGroup.NOTE_BAR
        elif self.tile_on_control_bar(tile, tile_type):
            tile_group = TileGroup.CONTROL_BAR
        else:
            raise ValueError("Unknown tilegroup for tile: " + str(tile))

        # logger.debug(json.dumps(list(chain.from_iterable(self._note_grid)), indent=4))
        # logger.debug(list(self._note_bar))
        # logger.debug(list(self._control_bar))
        logger.debug(tile_group)
        return tile_group


def main():
    logger.debug(mido.get_output_names())
    lp = LaunchpadMiniMk2()
    # logger.debug(lp.inport)
    # logger.debug(lp.outport)
    # lp.reset_all(lp.outport)
    lp.set_note_grid_color(3, 3, Colors.RED.value, lp.outport)
    lp.set_note_grid_color(3, 4, Colors.ORANGE.value, lp.outport)
    lp.set_note_grid_color(4, 3, Colors.ORANGE.value, lp.outport)
    lp.set_note_grid_color(4, 4, Colors.RED.value, lp.outport)
    #
    # for row in range(0, 4):
    #     for col in range(0, 4):
    #         lp.set_note_grid_color(
    #             row, col, RG_Colors.get_rg_value(row, col), lp.outport)


if __name__ == "__main__":
    main()
