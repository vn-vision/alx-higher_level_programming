#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    ''' pass the credentials from the command line'''

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=USERNAME,
                         passwd=PASSWORD, db=DB, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    db.close()
