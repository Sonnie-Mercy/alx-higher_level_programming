#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """
    Lists all cities from the hbtn_0e_4_usa database.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN
    states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
