#!/usr/bin/python3
"""
Takes in an argument and displays all values in the
'states' table where 'name' matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Takes in an argument and displays all values in the
    'states' table where 'name' matches the argument.
    """
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               host="localhost",
                               port=3306)

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE \
                   '{}' ORDER BY id".format(argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
