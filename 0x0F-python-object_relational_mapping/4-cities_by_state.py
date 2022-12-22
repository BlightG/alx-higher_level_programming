#!/usr/bin/python3
""" first sqldb trial """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELEECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
