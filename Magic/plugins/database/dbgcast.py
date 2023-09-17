
from Magic import *


def get_all():
    return udB.get_key("BLACKLIST_GCAST") or []


def add_bl(id):
    x = get_all()
    if id not in x:
        x.append(id)
        return udB.set_key("BLACKLIST_GCAST", x)


def un_bl(id):
    x = get_all()
    if id in x:
        x.remove(id)
        return udB.set_key("BLACKLIST_GCAST", x)


def isbl(id):
    return id in get_all()

def black_aja():
    return udB.get_key("BLACKLIST_GCAST") or {}

def list_bl(id):
    x = black_aja()
    for id in x:
        return "".join(f"**๏** `{z}`\n" for z in x)