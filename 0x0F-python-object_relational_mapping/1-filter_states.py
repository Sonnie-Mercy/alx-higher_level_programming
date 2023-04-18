#!/usr/bin/python3
"""
a python script that lists all states starting with N from the database
"""

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

    # Execute a SQL query to select states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch the results of the query
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the database connection
    db.close()
