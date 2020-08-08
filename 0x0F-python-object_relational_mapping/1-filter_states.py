#!/usr/bin/python3
#Lists all states from DB where name start with N
import MySQLdb as mdb
import sys

if __name__=='__main__':
	con = mdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
	cur = con.cursor()
	sql = """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"""
	cur.execute(sql)
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	con.close()

