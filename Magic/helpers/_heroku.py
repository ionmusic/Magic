
import asyncio
import shlex
import socket
from typing import Tuple

import dotenv
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from config import HEROKU_API, HEROKU_NAME

HAPP = None

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API),
    "https",
    str(HEROKU_NAME),
    "HEAD",
    "magic",
]


def is_heroku():
    return "heroku" in socket.getfqdn()


def heroku():
    global HAPP
    if is_heroku:
        if HEROKU_API and HEROKU_NAME:
            try:
                Heroku = heroku3.from_key(HEROKU_API)
                HAPP = Heroku.app(HEROKU_NAME)
                print(f"Heroku App Configured")
            except BaseException as e:
                print(f"{e}")
                print(
                    f"Pastikan HEROKU_API dan HEROKU_NAME anda dikonfigurasi dengan benar di config vars heroku."
                )