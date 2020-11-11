from app import models


async def create_session(user):
    session = await get_session(user)
    if session is None:
        session = models.Session(user_id=user.id)
        await session.create()


async def get_session(user):
    return await models.Session.query.where(models.Session.user_id == user.id).gino.first()


async def delete_session(user):
    session = await get_session(user)
    if session is not None:
        await session.delete()
