#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities """
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <user> <password> <db <state>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usern, passwd=password, db=db)
    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
