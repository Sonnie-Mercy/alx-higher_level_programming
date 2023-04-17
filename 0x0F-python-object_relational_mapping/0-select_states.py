#!/usr/bin/python3
"""lists all the states from the database """
import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to retrieve all states, sorted by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Print the rows in the specified format
    for row in rows:
        print(row)

    # Close the database connection
    db.close()
