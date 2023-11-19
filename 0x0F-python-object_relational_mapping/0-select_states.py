#!/usr/bin/python3
"""Lists all states form the hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv


db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

c = db.cursor()

c.execute("""SELECT * FROM states ORDER BY states.id ASC""")

results = c.fetchall()

for res in results:
    print(res)
