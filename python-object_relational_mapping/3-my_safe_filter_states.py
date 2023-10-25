#!/usr/bin/python3
"""
Takes in arguments and displays all values in the 'states' table where
'name' matches the argument and is safe from MySQL injections.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Takes in arguments and displays all values in the 'states' table where
    'name' matches the argument and is safe from MySQL injections.
    """
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               host="localhost",
                               port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id", (argv[4],))
    states = cursor.fetchall()

    for state in states:
            print(state)
