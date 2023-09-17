import os
import logging

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    return "local"
    
HOSTED_ON = where_hosted()


logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)