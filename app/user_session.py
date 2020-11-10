from app.tables import SessionTable


async def create_session(user):
    session = await get_session(user)
    if session is None:
        await SessionTable.add_row(dict(user_id=user['id']))


async def get_session(user):
    row = await SessionTable.get_row(SessionTable.c.user_id, user['id'])
    return row if row else None


async def delete_session(user):
    session = await get_session(user)
    if session is not None:
        SessionTable.delete_row(session['id'])
