#!/usr/bin/env python3

import mylogging
import time
from remidi_view import lauchpad
from remidi_view.layout import ViewGrid, ViewHBar, ViewVBar

logger = mylogging.setup_logger("remidi")


def main():
    try:
        logger.info("Hello to remidi")
        # lp = lauchpad.LaunchpadMiniMk2()
        g = ViewGrid()
        vb = ViewVBar()
        hb = ViewHBar()
        logger.info(g)
        logger.info(vb)
        logger.info(hb)
        while True:
            time.sleep(0.01)
    except KeyboardInterrupt:
        # lp.reset_all()
        logger.info("Good Bye")


if __name__ == "__main__":
    main()
