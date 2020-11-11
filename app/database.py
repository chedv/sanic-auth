from aiopg.sa import create_engine
from aiopg.sa.result import ResultProxy


class Session:
    fetch_one = ResultProxy.fetchone
    fetch_all = ResultProxy.fetchall
    fetch_many = ResultProxy.fetchmany

    def __init__(self, db_config):
        self.db_config = db_config

    async def execute(self, expression, fetch_method=None, **kwargs):
        async with create_engine(**self.db_config) as engine:
            async with engine.acquire() as connection:
                result = await connection.execute(expression)
                if fetch_method:
                    return await fetch_method(result, **kwargs)


class SessionFabric:
    db_config = None

    @classmethod
    def bind(cls, config):
        cls.db_config = config

    @classmethod
    async def create(cls):
        return Session(cls.db_config)
