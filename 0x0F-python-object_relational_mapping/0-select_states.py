#!/usr/bin/python3
#Lists all states from DB hbtn_0e_0_usa
import MySQLdb as mdb
import sys

if __name__=='__main__':
    con = mdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM 'states'")
        for state in cur.fetchall():
            print(state)
