#!/usr/bin/python3
"""
Lists all states from DB hbtn_0e_0_usa
"""
import MySQLdb
import sys


def select_states():
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

if __name__ == '__main__':
    select_states()
