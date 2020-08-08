#!/usr/bin/python3
#Lists all cities and theirs states
import MySQLdb as mdb
import sys

if __name__=='__main__':
	con = mdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
	cur = con.cursor()
	sql = """SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"""
	cur.execute(sql)
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	con.close()

