#!/usr/bin/python3
''' this script lists all states with a name starting n
from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

if __name__ == "__main__":
    # do not execute if imported

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(user=USER, passwd=PASS, db=DB,
                         host="localhost", port=3306)

    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%' ORDER BY
                states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
