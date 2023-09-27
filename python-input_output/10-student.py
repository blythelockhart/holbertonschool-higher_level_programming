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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return the dictionary representation.
        Args:
            attrs (list): A list of attribute names as strings.
        """
        dictionary = {}
        if type(attrs) is list and attrs is not None
        and all(type(i) is str for i in attrs):
            dictionary = {j: getattr(self, j) for j in attrs if hasattr(self, j)}
            return dictionary
        return self.__dict__
