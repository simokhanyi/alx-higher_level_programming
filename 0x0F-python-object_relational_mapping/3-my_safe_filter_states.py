#!/usr/bin/python3
"""Lists states from hbtn_0e_0_usa that match state name (safe)."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <user> <passwd> <db> <state>".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db, state = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db)

    # Create a cursor object
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state,))

    # Fetch all rows using fetchall()
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
