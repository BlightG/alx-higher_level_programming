#!/usr/bin/python3
""" first sqldb trial """
import MySQLdb
from sys import argv

if __name__ == "__main__" and len(argv) == 5:
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states ON\
                 cities.state_id = states.id\
                 WHERE states.id = (SELECT states.id FROM states\
                 WHERE states.name = 'texas')\
                 ORDER BY cities.id ASC;")
    rows = cur.fetchall()
    i = 0  # counts no of rows printed to adjust the comma separetor
    for row in rows:
        print("{}".format(row[0]), end="")
        i += 1
        if i != len(rows):
            print(", ", end="")
