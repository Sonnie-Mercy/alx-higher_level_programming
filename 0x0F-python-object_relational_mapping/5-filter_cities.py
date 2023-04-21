#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SQL query to select cities of that state
    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
                    cities.state_id = states.id WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name, ))

    # get results
    results = cursor.fetchall()

    # print results
    print(", ".join(city[0] for city in results))

    # close connections
    cursor.close()
    db.close()
