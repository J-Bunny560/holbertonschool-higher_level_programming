#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the SQL query to select all states sorted by id
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
    
    # Fetch all the rows from the executed query
    rows = cursor.fetchall()
    
    # Loop through the rows and print each one
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    cursor.close()
    db.close()
