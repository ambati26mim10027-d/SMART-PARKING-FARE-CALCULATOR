# logger_setup.py
# Sets up a simple log file so we can see what happened in the program.
import logging
import os
import config


def get_logger():
    # make the logs folder if it is not there
    folder = os.path.dirname(config.LOG_FILE)
    if folder != "" and not os.path.exists(folder):
        os.makedirs(folder)

    logger = logging.getLogger("parking")
    # this check stops the handler from being added again and again
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(config.LOG_FILE)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    return logger
