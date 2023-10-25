#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Takes in the name of a state as an argument and lists all
    cities of that state, using the database 'hbtn_0e_4_usa'.
    """
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]
    database = MySQLdb.connect(user=username,
                               passwd=password,
                               db=database_name,
                               host="localhost",
                               port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id IN (SELECT id \
                   FROM states WHERE name = %s) ORDER BY id", (state_name,))
    cities = cursor.fetchall()

    for city in cities:
        print(city)
