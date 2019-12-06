import mylogging
import time
import random

from games.reversi.board import ReversiBoard
from games.reversi.enums import PlayerType

logger = mylogging.setup_logger("reversi")


class Reversi(object):
    """docstring for Reversi."""

    def __init__(self, player):
        self.board = ReversiBoard()
        self.current_player = player

    def run(self):
        dp_board, pl, player = self.next_player(self.current_player)
        self.current_player = player
        logger.debug("\nPlayer: %s\nPossible Moves: %s\n Current Score: %s\n%s" %
                     (str(player), str(pl), str(self.board.current_scores), str(dp_board)))
        if len(pl) > 0:
            # x, y = pl[-1]
            x, y = random.choice(pl)
            self.board.do_move(x, y, self.current_player)
            # time.sleep(0.2)
            self.run()

    def next_player(self, current_player, initial=True):
        """Retruns the next player, if there isn't a valid move for any
        player, the game is finished."""
        next_player = current_player.opponent
        b, pl = self.board.possible_tiles(next_player)
        if len(pl) == 0:
            if initial is True:
                logger.debug(
                    "skipped next_player: %s  because of no possible moves." % next_player)
                return self.next_player(next_player, False)
            else:
                logger.debug("Game Finished")
                return b, pl, PlayerType.NOBODY
        else:
            return (b, pl, next_player)
