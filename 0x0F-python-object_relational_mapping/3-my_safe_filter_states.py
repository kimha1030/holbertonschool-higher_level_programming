#!/usr/bin/python3
"""
Lists all states from DB, of safe way from MySQL injections
"""
import MySQLdb
import sys


def filter_states_safe():
    """Select name according input"""
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
                 ORDER BY states.id ASC", [sys.argv[4]])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

if __name__ == '__main__':
    filter_states_safe()
