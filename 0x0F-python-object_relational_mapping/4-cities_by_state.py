#!/usr/bin/pyhton3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Prepare a query
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    # Fetch the results of the query
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    db.close()
