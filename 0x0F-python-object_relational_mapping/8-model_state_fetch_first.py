#!/usr/bin/python3
"""  a script that prints the first State object from the
database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    instance = session.query(State).order_by(State.id).first()
    if (instance is None):
        print("Nothing")
    else:
        print("{}: {}".format(instance.id, instance.name))
