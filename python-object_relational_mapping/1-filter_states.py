#!/usr/bin/python3
""" Lists all states with a name starting with N. """


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ Lists all states with a name starting with N. """
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        print(state)
