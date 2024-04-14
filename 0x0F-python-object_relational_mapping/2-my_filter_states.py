#!/usr/bin/python3
''' Script takes in an argument
displays all values in the states table
where name matches the argument
'''

import MySQLdb
import sys

if __name__ == "__main__":

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    STATE = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=USER, passwd=PASS
                         db=DB, state=STATE)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=STATE ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
