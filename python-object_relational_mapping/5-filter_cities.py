#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all
cities of that state, using the database 'hbtn_0e_4_usa'.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Takes in the name of a state as an argument and lists all
    cities of that state, using the database 'hbtn_0e_4_usa'.
    """
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3],
                               host="localhost",
                               port=3306)
    cursor = database.cursor()
    state_name = argv[4]
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON \
                   cities.state_id = states.id WHERE states.name =  %s \
                   ORDER BY cities.id", (state_name,))
    cities = cursor.fetchall()

    for city in cities:
        print(city)
