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

    def to_json(self, attrs=None):
        """ Return the dictionary representation.
        Args:
            attrs (list): A list of attribute names as strings.
        """
        dictionary = dict()
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        return self.__dict__
