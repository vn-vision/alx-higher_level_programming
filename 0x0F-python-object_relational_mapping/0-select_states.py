#!/usr/bin/python3
# connecting MySQL database
import MySQLdbi
import sys

n = len(sys.argv)

if n < 3:
    print("<usage: file.py username, password, database name")

USERNAME = sys.argv[0]
PASS = sys.argv[1]
MY_DB = sys.argv[2]
MY_HOST = "http://localhost:3306"

''' connecting to the database on port 3306 with the provide credentials
as well as the database to interact with '''

db = MySQLdb.connect(host=MY_HOST, user=USERNAME, passwd=PASS, db=MY_DB)

# get the cursor: givrs ability to have multiple separate working
# enironments through the same connection to db

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")

res = cur.fetchall()

for x in res:
    print(x)
