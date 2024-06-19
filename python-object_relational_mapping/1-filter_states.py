#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establishing the connection to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    
    # Creating a cursor object to interact with the database
    cur = conn.cursor()
    
    # Executing the SQL query to select all states ordered by their ID
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    # Fetching all the rows from the executed query
    query_rows = cur.fetchall()
    
    # Iterating over the fetched rows
    for row in query_rows:
        # Checking if the state name starts with 'N'
        if row[1].startswith("N"):
            print(row)
    
    # Closing the cursor
    cur.close()
    
    # Closing the connection to the database
    conn.close()
