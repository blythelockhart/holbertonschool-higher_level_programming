#!/usr/bin/python3
""" Base class. """
import json
from os import path


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base
        Args:
            id (int): The id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of 'list_dictionaries'. """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string rep. of 'list_objs' to a file.
        Args:
            list_objs (list): List of objects.
        """
        lst = []
        fle = cls.__name__ + ".json"
        if list_objs is None:
            return lst
        else:
            for i in list_objs:
                lst.append(i.to_dictionary())
        with open(fle, "w", encoding="utf-8") as j:
            j.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string rep. """
        lst = []
        if json_string is None:
            return lst
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes set.
        Args:
            dictionary (dict): A dictionary.
        """
        if cls.__name__ == 'Rectangle':
            diction = cls(1, 1)
        else:
            diction = cls(1)
        diction.update(**dictionary)
        return diction

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances. """
        lst = []
        fle = cls.__name__ + '.json'
        if path.exists(fle):
            with open(fle, "r", encoding="utf-8") as i:
                readme = i.read()
        else:
            return lst
        for j in cls.from_json_string(readme):
            lst.append(cls.create(**j))
        return lst
