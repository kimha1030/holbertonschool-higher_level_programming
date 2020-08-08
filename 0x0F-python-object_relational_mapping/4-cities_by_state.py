#!/usr/bin/python3
"""
Lists all cities according states
"""
import MySQLdb
import sys


def filter_states_cities():
    """List cities according states"""
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    sql = """SELECT cities.id, cities.name, states.name\
             FROM cities JOIN states\
             ON cities.state_id = states.id\
             ORDER BY cities.id ASC"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()

if __name__ == '__main__':
    filter_states_cities()
