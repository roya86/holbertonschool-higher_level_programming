#!/usr/bin/python3
"""
Displays all states where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # إزالة علامات الاقتباس
    state_name = state_name.strip("'")

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name = BINARY '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
