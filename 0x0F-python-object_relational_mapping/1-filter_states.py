#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database"""


import sys
import MySQLdb
import sqlalchemy


def list_nstates(username, password, database):
    """
    lists states starting with N
    """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
    )

    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id"
            )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.closse()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    list_nstates(username, password, database)
