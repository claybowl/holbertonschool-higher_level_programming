#!/usr/bin/python3
"""
List every state in the databasse
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", post=3306, user=argv[1], passwd=argv[2],
        database=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    results = cur.fetchall()
    for item in results:
        print(item)

    cur.close()
    db.close()
