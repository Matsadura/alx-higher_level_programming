#!/usr/bin/python3
""" Displays all values in the states tables where name matches the argument"""
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

    query = "SELECT * FROM states ORDER BY id;"
    cur.execute(query)

    query_result = cur.fetchall()

    for row in query_result:
        if row[1] == state_name:
            print(row)

    cur.close()
    conn.close()
