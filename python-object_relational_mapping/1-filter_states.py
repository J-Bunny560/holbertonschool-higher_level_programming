#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
from MySQLdb import connect

if __name__ == "__main__":
    arg = sys.argv
    username = arg[1]
    passwd = arg[2]
    db = arg[3]          # database name
    if len(arg) == 4:
        with connect(
                host="localhost", user=username,
                password=passwd, database=db,
                port=3306
                ) as mysql_db:
            cursor = mysql_db.cursor()
            cursor.execute(
                    "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
                    )
            result = cursor.fetchall()
            for i in result:
                print(i)