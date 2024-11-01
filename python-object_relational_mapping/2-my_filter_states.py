#!/usr/bin/python3
"""
search_states.py
This script connects to a MySQL database and retrieves all states
that match a specified name from the states table.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the main function
def main():
    """
    Main function that executes the database query to find states by name.
    It takes command line arguments for database connection and state name.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the database connection string
    connection_string = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}"
    
    # Create an engine and session
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states table
    states = session.execute(
        f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id ASC"
    ).fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the session
    session.close()

if __name__ == "__main__":
    main()