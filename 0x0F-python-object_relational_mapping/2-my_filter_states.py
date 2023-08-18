#!/usr/bin/python3
"""displays all values in the states table that match argument"""


import sys
import MySQLdb


def display_states(username, password, database, search_name):
    """
    displays values where name matches argument"""
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
    )

    cursor = db.cursor()
    query = "SELECT * FROM states where name LIKE %s ORDER BY states.id ASC"
    cursor.execute(query, (search_name,))

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
    search_name = sys.argv[4]

    display_states(username, password, database, search_names)
