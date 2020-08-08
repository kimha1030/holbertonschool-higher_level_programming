#!/usr/bin/python3
"""
Lists all states from DB where name start with N
"""
import MySQLdb
import sys


def select_states_name():
    """Select name that start with N"""
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    sql = """SELECT * FROM states WHERE name\
             LIKE BINARY 'N%' ORDER BY states.id ASC"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

if __name__ == '__main__':
    select_states_name()
