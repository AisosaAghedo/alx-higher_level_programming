#!/usr/bin/python3
"""a script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)

    for instance in session.query(State).filter(State.name.ilike('%a%')):
        session.delete(instance)
    session.commit()
