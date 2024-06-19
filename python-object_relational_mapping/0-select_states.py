#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Connect to the MySQL server running on localhost at port 3306
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        c = db.cursor()
        
        # Execute the query to select all states, sorted by id in ascending order
        c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
        
        # Fetch and print the results
        for state in c.fetchall():
            print(state)
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
    finally:
        # Ensure the cursor and connection are closed
        if c:
            c.close()
        if db:
            db.close()
