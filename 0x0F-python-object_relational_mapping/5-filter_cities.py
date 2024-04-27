#!/usr/bin/python3
""" Takes the name of a state as arguments and lists all the cities
of that state """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name)

    cur = conn.cursor()

    query = "SELECT cities.name \
            FROM cities \
            LEFT JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = '{}' \
            ORDER BY cities.id".format(state_name)

    cur.execute(query)

    query_result = cur.fetchall()
    for i in range(len(query_result) - 1):
        print(query_result[i][0], end=", ")
    if len(query_result) > 0:
        print(query_result[len(query_result) - 1][0])

    cur.close()
    conn.close()
