import mylogging

from games.reversi.board import ReversiBoard
from games.reversi.enums import PlayerType

logger = mylogging.setup_logger("reversi")


class Reversi(object):
    """docstring for Reversi."""

    def __init__(self, player):
        self.board = ReversiBoard()
        self.current_player = player

    def run(self):
        dp_board, player = self.next_player(self.current_player)
        logger.debug(dp_board)
        logger.debug(player)
        # self.board.set_tile(x, y, self.current_player)

    def next_player(self, current_player, initial=True):
        """Retruns the next player, if there isn't a valid move for any
        player, the game is finished."""
        next_player = current_player.opponent
        b, pl = self.board.possible_tiles(next_player)
        if len(pl) == 0:
            if initial is True:
                return self.next_player(next_player, False)
            else:
                logger.debug("Game Finished")
                return b, PlayerType.NOBODY
        else:
            return b, next_player
