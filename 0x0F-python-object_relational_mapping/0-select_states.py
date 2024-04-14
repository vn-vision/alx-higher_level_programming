#!/usr/bin/python3
# connecting MySQL database
import MySQLdb
import sys


if __name__ == "__main__":
    n = len(sys.argv)

    if n != 4:
        print("<usage: file.py username, password, database name")
        sys.exit(1)

    USERNAME = sys.argv[1]
    PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_HOST = "localhost"

    '''
    connecting to the database on port 3306 with the provide credentials
    as well as the database to interact with
    '''
    try:
        db = MySQLdb.connect(host=MY_HOST, port=3306, user=USERNAME, passwd=PASS, db=MY_DB)

        # get the cursor: givrs ability to have multiple separate working
        # enironments through the same connection to db

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")

        res = cur.fetchall()

        for x in res:
            print(x)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL BD: {}".format(e))
        sys.exit(1)
