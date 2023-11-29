#!/usr/bin/python3
"""
    script taking 3 arguments mysql username, mysql password, database name
    lists all states from the database hbtn_0e_0_usa sorted by states_id asc
    using module MySQLdb
    connect to MySQL server running on localhost at port 3306
    code dont be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage : python script.py <username> <password> <database>")

    """ connection to the database """
    db = MySQLdb.connect(host="localhost", port=3306, charset='utf8',
                         user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])

    """ create a cursor to execute sql command  """
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    """ retrieve all the rows of the table states"""
    lines = cur.fetchall()
    for line in lines:
        print(line)

    """  close the cursor and the connection """
    cur.close()
    db.close()