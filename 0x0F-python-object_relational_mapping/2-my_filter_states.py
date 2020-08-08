#!/usr/bin/python3
"""
Lists all states from DB where name is equal to input
"""
import MySQLdb
import sys


def filter_states_input():
    """Select name according input"""
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    sql = """SELECT * FROM states WHERE name LIKE BINARY '{:s}'\
             ORDER BY states.id ASC""".format(sys.argv[4])
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

if __name__ == '__main__':
    filter_states_input()
