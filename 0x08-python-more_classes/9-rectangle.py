#!/usr/bin/python3
""" Define a square """


class Rectangle:
    """ a Class representing a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ an instantiation function"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

        Rectangle.print_symbol = '#'
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the value of the height """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the value of the width """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    def perimeter(self):
        """ a function that calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def area(self):
        """ a function that calculates the are of a rectangle"""
        return self.__width * self.__height

    @classmethod
    def print_symbol(cls, value="#"):
        """ change the value of print_symbol """
        cls.print_symbol = value

    def __str__(self):
        """ is string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = [[0 for j in range(self.__width)]
                    for i in range(self.__height)]
            for i in range(self.__height):
                for j in range(self.__width):
                    rect[i][j] = str(self.print_symbol)
            string = "\n".join("".join(num for num in i) for i in rect)
            return string

    def __repr__(self):
        """ a string represtenation of the formal input method"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ A magic function to delete a class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ checks area of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1 < rect_2:
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """ creting alternative class constructor """
        return cls(size, size)

    def __lt__(self, rect):
        """ adds less than comparsion"""
        if self.area() < rect.area():
            return True
        else:
            return False

    def __eq__(self, rect):
        """ adds equality comparison """
        if self.area == rect.area:
            return True
        else:
            return False
