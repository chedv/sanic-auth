from app import models


def create_session(user):
    session = get_session(user)
    if session is None:
        session = models.Session(user_id=user.id)
        models.Session.add(session)


def get_session(user):
    query = models.Session.query()
    session = query.filter_by(user_id=user.id).first()
    query.session.close()

    return session


def delete_session(user):
    session = get_session(user)
    if session is not None:
        models.Session.delete(session)
