#!/usr/bin/python3
<<<<<<< HEAD
"""Define a MagicClass that does exactly as the bytecode provided."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

         Arg:
         radius (float or int): The radius of the new MagicClass.
         """
         self.__radius = 0
         if type(radius) is not int and type(radius) is not float:
             raise TypeError("radius must be a number")
         self.__radius = radius

         def area(self):
             """Return the area of the MagicClass."""
             return (self.__radius ** 2 * math.pi)

         def circumference(self):
             """Return The circumference of the MagicClass."""
             return (2 * math.pi * self.__radius)
=======
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> febd46b1dd16a057b5e3536bc42e607f26071786
