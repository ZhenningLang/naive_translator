import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from naive_translator.server import start_server  # noqa
from naive_translator.utils import setup_logger  # noqa

setup_logger()
start_server()
