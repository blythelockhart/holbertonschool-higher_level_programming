#!/usr/bin/python3
""" Lists all cities from the database 'hbtn_0e_4_usa'. """


import sys
import MySQLdb


if __name__ == "__main__":
    """ Lists all cities from the database 'hbtn_0e_4_usa'. """
    database = MySQLdb.connect(user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               host="localhost",
                               port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN \
                   states AS s ON c.state_id = s.id ORDER BY c.id")
    cities = cursor.fetchall()

    for city in cities:
        print(city)
