#!/usr/bin/python3
#Lists all states from DB where name is arg order by name
import MySQLdb as mdb
import sys

if __name__=='__main__':
	con = mdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
	cur = con.cursor()
	cur.execute("SELECT * FROM states WHERE name = {} ORDER BY states.id ASC;".format(sys.argv[4]))
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	con.close()

