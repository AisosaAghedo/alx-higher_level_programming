#!/usr/bin/python3
""" that prints all City objects from the database hbtn_0e_14_usa"""
if __name__ == '__main__':
    from sys import argv
    from model_state import State, Base
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State.name, City.id, City.name).join(
            City).order_by(City.id).all()
    for row in rows:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))
