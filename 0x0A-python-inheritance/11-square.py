#!/usr/bin/python3


class BaseGeometry:
    """ Creates an empty class called BaseGeometry"""
    def __init__(self):
        pass

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle that inherits BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """description"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Area"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square that inherits Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area"""
        return self.__size * self.__size

    def __str__(self):
        """description"""
        return("[Square] {}/{}".format(self.__size, self.__size))
