class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant delete attribute")


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


# repeating property
class BadPerson:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant delete attribute")

    # Repeated property code, but for a different name (bad!)
    @property
    def last_name(self):
        return self._last_name

    # Setter function
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string")
        self._last_name = value

    # Deleter function (optional)
    @last_name.deleter
    def last_name(self):
        raise AttributeError("Cant delete attribute")
