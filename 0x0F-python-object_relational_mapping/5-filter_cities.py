#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of the given state from the hbtn_0e_4_usa database.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name"
    "FROM cities"
    "JOIN states ON cities.state_id = states.id"
    "WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
