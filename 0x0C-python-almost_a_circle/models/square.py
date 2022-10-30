#!/usr/bin/python3
""" A module for Square class that inherits from Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square class with several attributes """
    def __init__(self, size, x=0, y=0, id=None):
        """ an instansiation for rectanlge class

            Args:
                width: an int type private instance attribute
                height: an int type private instance attribute
                x: an int type private instance attribute that defaults to 0
                y: an int type private instance attribute that defaults to 0
                id: an instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ A string prinitng the bject chractersitcs """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, super().y, self.height)

    @property
    def size(self):
        """ A getter for the size of the Square """
        return self.width

    @size.setter
    def size(self, size):
        """ A Setter for the size of the Square """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ takes a variable number of arguments to update class attribute """
        if args:
            if len(args) >= 1:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for i in kwargs:
                if i == "id":
                    super().__init__(
                        self.size, self.size, self.x, self.y, kwargs[i])
                elif i == "size":
                    self.width = kwargs[i]
                    self.height = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]

    def to_dictionary(self):
        """ returns a dictionary representation of the class Square """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
