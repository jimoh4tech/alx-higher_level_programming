#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv;
    db = MySQLdb.connect(user=args[1], port=3306, host="localhost",
                         passwd=args[2], db=args[3], charset="utf8")
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(args[4])
    cur.execute(sql)
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
