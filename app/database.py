from aiopg.sa import create_engine


class Session:
    def __init__(self, engine, connection):
        self.engine = engine
        self.connection = connection

    async def execute(self, expression):
        return await self.connection.execute(expression)

    async def close(self):
        await self.connection.close()
        self.engine.close()


class SessionFabric:
    db_config = None

    @classmethod
    def bind(cls, config):
        cls.db_config = config

    @classmethod
    async def create(cls):
        engine = await create_engine(**cls.db_config)
        connection = await engine.acquire()

        return Session(engine, connection)
