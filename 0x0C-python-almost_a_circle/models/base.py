#!/usr/bin/python3
"""
    This class will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating the same code
"""
import json


class Base:
    """ a class for managing id """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            An instanciation for Base Object it creates unique ids

            Args:
                id: Takes an int argument but defaluts to None
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convertes list of dictionary to json string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ converts a string representation to list """
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs=[]):
        """that writes the JSON string representation
            of list_objs to a file
        """
        if list_objs is None or len(list_objs) == 0:
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
                newlist = []
                f.write(cls.to_json_string(newlist))
        else:
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
                newlist = [cls.to_dictionary(i) for i in list_objs]
                f.write(cls.to_json_string(newlist))

    @classmethod
    def create(cls, **dictionary):
        ''' a class method to create an instance of the specified class '''
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ A cls method that returns a list of instances """
        str = '{}.json'.format(cls.__name__)
        if str:
            with open(str, 'r', encoding="utf-8") as f:
                newlist = cls.from_json_string(f.read())
                instlist = [cls.create(i) for i in newlist]
                return instlist
        return []
