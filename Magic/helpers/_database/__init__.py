
import ast
import os
import sys

import config
from Magic.helpers._load import HOSTED_ON, LOGGER
from redis import Redis

Redis = None

class Database:
    def __init__(self, *args, **kwargs):
        self._cache = {}

    def get_var(self, var):
        if var in self._cache:
            return self._cache[var]
        value = self._get_data(var)
        self._cache.update({var: value})
        return value

    def re_cache(self):
        self._cache.clear()
        for var in self.vars():
            self._cache.update({var: self.get_var(var)})

    def ping(self):
        return 1

    @property
    def usage(self):
        return 0

    def vars(self):
        return []

    def del_var(self, var):
        if var in self._cache:
            del self._cache[var]
        self.delete(var)
        return True

    def _get_data(self, var=None, data=None):
        if var:
            data = self.get(str(var))
        if data:
            try:
                data = ast.literal_eval(data)
            except BaseException:
                pass
        return data

    def set_var(self, var, value):
        value = self._get_data(data=value)
        self._cache[var] = value
        return self.set(str(var), str(value))

    def rename(self, var1, var2):
        _ = self.get_var(var1)
        if _:
            self.del_var(var1)
            self.set_var(var2, _)
            return 0
        return 1
        
class DBRedis(Database):
    def __init__(
        self,
        host,
        port,
        password,
        platform="",
        logger=LOGGER,
        *args,
        **kwargs,
    ):
        if host and ":" in host:
            spli_ = host.split(":")
            host = spli_[0]
            port = int(spli_[-1])
            if host.startswith("http"):
                LOGGER(__name__).error("REDIS_URI tidak perlu menggunakan https://")
                import sys

                sys.exit()
        elif not host or not port:
            LOGGER(__name__).error("Port tidak ditemukan.")
            import sys

            sys.exit()
        kwargs["host"] = host
        kwargs["password"] = password
        kwargs["port"] = port

        if platform.lower() == "qovery" and not host:
            var, hash_, host, password = "", "", "", ""
            for vars_ in os.environ:
                if vars_.startswith("QOVERY_REDIS_") and vars.endswith("_HOST"):
                    var = vars_
            if var:
                hash_ = var.split("_", maxsplit=2)[1].split("_")[0]
            if hash:
                kwargs["host"] = os.environ.get(f"QOVERY_REDIS_{hash_}_HOST")
                kwargs["port"] = os.environ.get(f"QOVERY_REDIS_{hash_}_PORT")
                kwargs["password"] = os.environ.get(f"QOVERY_REDIS_{hash_}_PASSWORD")
        self.db = Redis(**kwargs)
        self.set = self.db.set
        self.get = self.db.get
        self.vars = self.db.vars
        self.delete = self.db.delete
        super().__init__()

    @property
    def name(self):
        return "Redis"

    @property
    def usage(self):
        return sum(self.db.memory_usage(x) for x in self.vars())
        
def DBMagic():
    try:
        return DBRedis(
                host=config.REDIS_URI,
                password=config.REDIS_PASSWORD,
                platform=HOSTED_ON,
                port=config.REDISPORT,
                decode_responses=True,
                socket_timeout=5,
                retry_on_timeout=True,
            )
    except BaseException as e:
        LOGGER(__name__).exception(e)
    exit()
    
    
MDB = DBMagic()