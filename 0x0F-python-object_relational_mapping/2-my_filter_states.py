#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that match
the provided state name."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} < usr > < psswd > < db > < stt >".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db, state = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=psswd, db=db)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
