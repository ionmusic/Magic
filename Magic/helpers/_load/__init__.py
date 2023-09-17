import os
import logging

from .clients import *

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    return "local"
    
HOSTED_ON = where_hosted()

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)