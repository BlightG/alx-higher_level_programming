#!/usr/bin/python3
""" a Module for Rectanlge class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that has several attribute """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ an instansiation for rectanlge class

            Args:
                width: an int type private instance attribute
                height: an int type private instance attribute
                x: an int type private instance attribute that defaults to 0
                y: an int type private instance attribute that defaults to 0
                id: an instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width private instance getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Width Private instance Setter """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ height private instance getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height Private instance Setter """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """ x private instance getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x Private instance Setter """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ y private instance getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y Private instance Setter """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """ Pulbice method that returns the area value of a rectangle """
        return self.__height * self.__width

    def display(self):
        """ Is string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print('')
        else:
            rect = [[0 for j in range(self.__x + self.__width)]
                    for i in range(self.__height)]
            for k in range(self.__y):
                print()
            for i in range(self.__height):
                for j in range(self.__x):
                    rect[i][j] = " "
                for j in range(self.__x, self.__x + self.__width):
                    rect[i][j] = '#'

            string = "\n".join("".join(num for num in i) for i in rect)
            print(string)

    def __str__(self):
        """ a string prinitng the bject chractersitcs """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ takes a variable number of arguments to update class attribute """
        if args:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for i in kwargs:
                if i == "id":
                    super().__init__(kwargs[i])
                elif i == "width":
                    self.width = kwargs[i]
                elif i == "height":
                    self.height = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]

    def to_dictionary(self):
        """ returns a dictionary representation of the class Rectangle """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
