#!/usr/bin/python3
""" Define a student. """


class Student:
    """ A student. """
    def __init__(self, first_name, last_name, age):
        """ A new student.
        Args:
            first_name (str): The student's fist name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """ Return the dictionary representation. """
        return self.__dict__

