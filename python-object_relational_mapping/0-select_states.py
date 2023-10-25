#!/usr/bin/python3
""" Lists all States from the database 'hbtn_0e_0_usa'. """


import sys
import MySQLdb


if __name__ == "__main__":
    """ Lists all States from the database 'hbtn_0e_0_usa'. """
    database = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall()]
