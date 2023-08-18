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
            user=username,
            passwd=password,
            db=database,
            port=3306
    )

    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states ORDER BY states.id ASC;"
            )
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_nstates(username, password, database)
