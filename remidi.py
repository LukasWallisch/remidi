#!/usr/bin/env python3

import mylogging
import time
from remidi_view import lauchpad
# from remidi_view.layout import ViewGrid, ViewHBar, ViewVBar
from games.reversi.reversi import Reversi
from games.reversi.enums import PlayerType

# from games.reversi.board import ReversiBoard

logger = mylogging.setup_logger("remidi")


def main():
    mylogging.set_logger_lvl("launchpad", mylogging.logging.INFO)
    rv = Reversi(PlayerType.PLAYER_1, 0)
    t0 = time.time()
    rv.run()
    t1 = time.time()
    logger.debug(t1-t0)
    # lp= lauchpad.LaunchpadMiniMk2()

    # board2.check_possible(Directions.SOUTH_EAST, 2, 2, PlayerType.PLAYER_1,True)
    # logger.debug("board2.current_scores\n" + str(board2.current_scores))

    # try:
    #     logger.info("Hello to remidi")
    #     # lp = lauchpad.LaunchpadMiniMk2()
    #     g = ViewGrid()
    #     vb = ViewVBar()
    #     hb = ViewHBar()
    #     logger.info(g)
    #     logger.info(vb)
    #     logger.info(hb)
    #     while True:
    #         time.sleep(0.01)
    # except KeyboardInterrupt:
    #     # lp.reset_all()
    #     logger.info("Good Bye")


if __name__ == "__main__":
    main()
