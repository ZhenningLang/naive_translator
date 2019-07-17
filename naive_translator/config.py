import logging
import os

# path
_CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PACKAGE_ROOT = _CURRENT_PATH
DATA_ROOT = os.path.join(_CURRENT_PATH, 'data')
DICT_PATH = {
    'traditional2simple': os.path.join(DATA_ROOT, 'dictionary')
    # add more dictionaries here
    # name: dictionary path
}

# log
LOG_PATH = os.path.join(DATA_ROOT, 'logs')
LOG_LEVEL = logging.INFO
LOG_FORMAT = logging.Formatter('[%(thread)d] %(levelname)s (%(asctime)s) %(filename)s > %(funcName)s > line %(lineno)d: %(message)s')  # noqa

# server
DEFAULT_PORT = 8888
