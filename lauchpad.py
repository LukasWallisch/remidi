import mylogging
import mido
from datetime import datetime
import time
from remidi_enums.colors import colors
from remidi_enums.colors import rg_colors

logger = mylogging.setup_logger("launchpad")




class Launchpad(object):
    """docstring for Launchpad_con."""

    def __init__(self):
        self.counter = 0
        self.note_timer = {}
        self.control_timer = {}
        self.ioport = mido.open_ioport("Launchpad Mini 1")

    def __del__(self):
        if not self.ioport.closed:
            self.ioport.close()
            logger.info("ioport closed!")

    @property
    def note_grid(self):
        return self._note_grid

    @property
    def note_bar(self):
        return self._note_bar

    @property
    def control_bar(self):
        return self._control_bar

    def reset_note_grid(self, outport):
        for row_id, row in enumerate(self.note_grid):
            for col_id, col in enumerate(row):
                logger.debug("reset row: " + str(row)+" row_id: "
                             + str(row_id)+" col: "+str(col))
                msg = mido.Message(
                    "note_on", note=self.note_grid[row_id][col_id])
                outport.send(msg)

    def reset_note_bar(self, outport):
        for b_id, button in enumerate(self.note_bar):
            msg = mido.Message("note_on", note=self.note_bar[b_id])
            outport.send(msg)

    def reset_control_bar(self, outport):
        for b_id, button in enumerate(self.control_bar):
            msg = mido.Message(
                "control_change", control=self.control_bar[b_id])
            outport.send(msg)

    def set_note_grid_color(self, row_id, col_id, color, outport):
        msg = mido.Message(
            "note_on", note=self.note_grid[row_id][col_id], velocity=color)
        logger.debug(msg)
        outport.send(msg)

    def set_note_bar_color(self, b_id, color, outport):
        msg = mido.Message("note_on", note=self.note_bar[b_id], velocity=color)
        outport.send(msg)

    def reset_control_bar_color(self, b_id, color, outport):
        msg = mido.Message(
            "control_change", control=self.control_bar[b_id], value=color)
        outport.send(msg)

    def reset_all(self, outport):
        self.reset_note_grid(outport)
        self.reset_note_bar(outport)
        self.reset_control_bar(outport)


class Launchpad_Mini_Mk2(Launchpad):
    """docstring for Launchpad_Mini_Mk2."""

    def __init__(self):
        self.name = "Launchpad Mini 1"
        self._note_grid = [range(0, 9),
                           range(16, 25),
                           range(32, 41),
                           range(48, 57),
                           range(64, 73),
                           range(70, 79),
                           range(86, 95),
                           range(102, 111)]
        self._note_bar = range(9, 121, 16)
        self._control_bar = range(104, 113)
        super(Launchpad_Mini_Mk2, self).__init__()
        # with mido.open_output("Launchpad Mini 1") as outport:
        #     self.outport = outport




def main():
    logger.debug(mido.get_output_names())
    lp = Launchpad_Mini_Mk2()
    logger.debug(lp.inport)
    logger.debug(lp.outport)
    # lp.reset_all(lp.outport)
    # lp.set_note_grid_color(3, 3, colors.RED.value, lp.outport)
    # lp.set_note_grid_color(3, 4, colors.ORANGE.value, lp.outport)
    # lp.set_note_grid_color(4, 3, colors.ORANGE.value, lp.outport)
    # lp.set_note_grid_color(4, 4, colors.RED.value, lp.outport)
    #
    # for row in range(0, 4):
    #     for col in range(0, 4):
    #         lp.set_note_grid_color(
    #             row, col, rg_colors.get_rg_value(row, col), lp.outport)


main()
