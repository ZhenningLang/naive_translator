import sys

from .server import start_server
from .utils import setup_logger


def main():
    setup_logger()
    if len(sys.argv) > 1:
        start_server(sys.argv[1])
    else:
        start_server()
