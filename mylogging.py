"""Setup for Logging."""

import logging
# import coloredlogs


def setup_logger(logger_name):
    """Run setup for logger with given Name.

    logger_name: name for new Logger
    """
    logger = logging.Logger(logger_name)
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter_string = '%(asctime)s '
    formatter_string += '| %(levelname)7s '
    formatter_string += '| %(lineno)4d '
    formatter_string += '| %(filename)7s '
    formatter_string += '| %(funcName)7s: '
    formatter_string += '%(message)s'
    f = logging.Formatter(formatter_string)
    sh.setFormatter(f)
    logger.addHandler(sh)
    return logger


def test_logging(test_message):
    """Test method if loggingsetup worked."""
    logger = setup_logging("Logging")
    logger.debug(test_message)
    logger.info(test_message)
    logger.warning(test_message)
    logger.error(test_message)
    logger.critical(test_message)
