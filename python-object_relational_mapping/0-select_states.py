#!/usr/bin/python3
""" A script that utilizes MySQLdb package to list states in a database."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    with MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        result = cursor.fetchall()
        for row in result:
            print(row)
