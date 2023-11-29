#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Extracting command-line arguments
    username, password, database = argv[1], argv[2], argv[3]

    try:
        # Establishing a connection to the database
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Creating a cursor object to execute SQL queries
        with connection.cursor() as cursor:
            # Executing the SQL query to select all states
            cursor.execute("SELECT * FROM states ORDER BY id ASC")

            # Fetching and printing the results
            states = cursor.fetchall()
            for state in states:
                print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

    finally:
        # Closing the database connection
        if connection:
            connection.close()
