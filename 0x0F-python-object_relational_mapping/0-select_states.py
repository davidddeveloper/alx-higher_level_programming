#!/usr/bin/python3
"""
    this scripts gets all state in a db with mysqldb

"""


import MySQLdb
import sys

args = sys.argv[1:]
username = args[0]
password = args[1]
db_name = args[2]

db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=db_name)

cur = db.cursor()

cur.execute("SELECT * FROM states")

rows = cur.fetchall()
for row in rows:
    print(row)
