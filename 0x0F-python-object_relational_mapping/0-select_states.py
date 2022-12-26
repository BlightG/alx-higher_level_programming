#!/usr/bin/python3
""" first sqldb trial """
import MySQLdb
from sys import argv

if __name__ == "__main__" and len(argv) == 4:
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    db.close()
