#!/usr/bin/python3
"""
Prints all City objects by State
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            user, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
