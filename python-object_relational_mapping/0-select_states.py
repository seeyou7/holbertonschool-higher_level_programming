#!/usr/bin/python3
'''listing all states from the database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)

    conn.close()