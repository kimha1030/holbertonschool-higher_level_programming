#!/usr/bin/python3
"""
Take state as an argument and lists all cities of state
"""
import MySQLdb
import sys


def filter_states_cities_input():
    """List cities and states according input"""
    con = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    sql = """SELECT cities.name FROM cities WHERE cities.state_id IN\
             (SELECT id FROM states WHERE name = '{:s}') ORDER BY\
             cities.id ASC""".format(sys.argv[4])
    cur.execute(sql)
    my_list = []
    for row in cur.fetchall():
        my_list.append(row[0])
    print(", ".join(my_list))
    cur.close()
    con.close()

if __name__ == '__main__':
    filter_states_cities_input()
