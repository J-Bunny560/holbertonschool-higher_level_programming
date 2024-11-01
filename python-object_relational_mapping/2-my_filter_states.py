#!/usr/bin/python3
""" A script that utilizes MySQLdb package to list states in a database."""
import MySQLdb

def get_states(username, password, database, state_name):
    """
    Retrieves and displays all values in the states table of hbtn_0e_0_usa 
    where name matches the given state name.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): State name to search for

    Returns:
        None
    """

    # Establish a connection to the MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Create the SQL query with the user input
    query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY id ASC
    """

    # Execute the SQL query with the state name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all the rows from the query result
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Example usage:
    get_states('username', 'password', 'hbtn_0e_0_usa', 'California')