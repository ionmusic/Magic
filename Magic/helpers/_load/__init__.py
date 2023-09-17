import os

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    return "local"
    
HOSTED_ON = where_hosted()