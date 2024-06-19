#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Establishing the connection to the database
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        
        # Using parameterized queries to prevent SQL injection
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
        cur.execute(query, (argv[4],))
        
        # Fetching and printing the results
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensuring the cursor and connection are closed properly
        if cur:
            cur.close()
        if conn:
            conn.close()
