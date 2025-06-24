# dipoll/logconf.py

# Base libs
import sys
import logging

# DiPoll custom files
from config import Globals

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        stream=sys.stdout)

for name in Globals.LOGGERS:
    logging.getLogger(name).setLevel(logging.WARNING)

# Universall logger for the whole application
logger = logging.getLogger(__name__)