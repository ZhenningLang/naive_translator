import logging
from logging.handlers import TimedRotatingFileHandler
import os

from .config import LOG_LEVEL, LOG_FORMAT, LOG_PATH


def setup_logger(debug=False):

    if debug:
        log_level = logging.DEBUG
    else:
        log_level = LOG_LEVEL
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(LOG_FORMAT)
    handlers = [stream_handler]

    err = None
    if not os.path.isdir(LOG_PATH):
        try:
            os.makedirs(LOG_PATH, exist_ok=True)
        except Exception as e:
            err = e

    log_path_name = None
    if os.path.isdir(LOG_PATH):
        log_path_name = os.path.join(LOG_PATH, 'log')
        file_handler = TimedRotatingFileHandler(log_path_name, when='midnight', backupCount=7)
        file_handler.setFormatter(LOG_FORMAT)
        handlers.append(file_handler)

    logger = logging.getLogger()
    logger.setLevel(log_level)

    for handler in handlers:
        logger.addHandler(handler)
    if len(handlers) == 1:
        logging.error(f'Cannot create file logger {LOG_PATH} with error: {err}')
    logging.info('Log path: {}'.format(log_path_name))
