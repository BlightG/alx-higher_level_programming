#!/usr/bin/python3
""" print a docstring """


class Student:
    """ a student class """
    def __init__(self, first_name, last_name, age):
        """ instanciation of the student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a JSON serialization of the class student """
        return self.__dict__
