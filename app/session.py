
def add_entry(session_cls, entry):
    session = session_cls()
    session.add(entry)
    session.commit()


def create_query(session_cls):
    session = session_cls()
    return session.query
