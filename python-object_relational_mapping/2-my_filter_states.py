#!/usr/bin/python3
"""This script searches for an argument in the database."""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    with MySQLdb.connect(
            host="localhost", user=username, passwd=password, db=database
            ) as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM states WHERE BINARY name = '{}' \
                ORDER BY id ASC".format(search)
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
