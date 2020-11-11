from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

from app.database import SessionFabric
from settings import db_settings


metadata = MetaData()

SessionFabric.bind(db_settings)


class ExtendedTable(Table):
    async def add_row(self, row):
        expression = self.insert().values(**row)
        await ExtendedTable.execute(expression)

    async def delete_row(self, id):
        expression = self.delete().where(self.c.id == id)
        await ExtendedTable.execute(expression)

    async def get_row(self, field, value):
        expression = self.select().where(field == value)
        return await ExtendedTable.execute_fetchone(expression)

    async def get_rows(self, field, value):
        expression = self.select().where(field == value)
        return await ExtendedTable.execute_fetchall(expression)

    @staticmethod
    async def execute(expression):
        session = await SessionFabric.create()
        await session.execute(expression)
        await session.close()

    @staticmethod
    async def execute_fetchone(expression):
        session = await SessionFabric.create()
        result = await session.execute(expression)
        row = await result.fetchone()
        await session.close()

        return row

    @staticmethod
    async def execute_fetchall(expression):
        session = await SessionFabric.create()
        result = await session.execute(expression)
        rows = await result.fetchall()
        await session.close()

        return rows


UserTable = ExtendedTable('users', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('email', String, nullable=False, unique=True),
                          Column('username', String, nullable=False, unique=True),
                          Column('password_hash', String(64), nullable=False))


SessionTable = ExtendedTable('sessions', metadata,
                             Column('id', Integer, primary_key=True),
                             Column('user_id', Integer, ForeignKey('users.id')))