#!/usr/bin/python3
""" Displays all values in the states tables where name matches the argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    if state_name == "'":
        pass
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=db_name)

    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id;".format(
            state_name)
    cur.execute(query)

    query_result = cur.fetchall()

    for row in query_result:
        print(row)

    cur.close()
    conn.close()
