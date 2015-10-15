__author__ = 'Jonas'
from JTVector.dim3.vertex import Vertex
from JTVector.dim3.point import Point
import math


class Vector(Vertex):

    def __init__(self, *args, **kwargs):
        super(Vector, self).__init__()
        if len(args) != 0:

            # assigning the dimensional coordinates
            if len(args) == 3:
                for arg in args:
                    if arg is not int:
                        raise ValueError()
                self.x1 = args[0]
                self.x2 = args[1]
                self.x3 = args[2]
            elif len(args) == 2:
                arg1 = args[0]
                arg2 = args[1]
                if isinstance(arg1, Point) and isinstance(arg2, Point):
                    self.x1 = arg2.x1 - arg1.x1
                    self.x2 = arg2.x2 - arg1.x2
                    self.x3 = arg2.x3 - arg2.x3
            elif len(args) == 1:
                arg = args[0]
                if isinstance(arg, Point) or isinstance(arg, Vector):
                    self.x1 = arg.x1
                    self.x2 = arg.x2
                    self.x3 = arg.x3

            # calculating the length
            self.length = 0
            self._calc_length()

        else:
            self.length = 0

    def __add__(self, other):
        """
        returns a new Vector with the corresponding coordinates added together
        :param other: (Vector) the Vector to add to
        :return: (Vector)
        """
        if isinstance(other, Vector):
            return Vector(self.x1 + other.x1, self.x2 + other.x2, self.x3 + other.x3)
        else:
            raise ValueError()

    def __iadd__(self, other):
        """
        adds the coordinates of the given Vector to the coordinates of this object
        :param other: (Vector) the Vector to add to
        :return: (void)
        """
        if isinstance(other, Vector):
            self.x1 += other.x1
            self.x2 += other.x2
            self.x3 += other.x3
        else:
            raise ValueError()

    def __sub__(self, other):
        """
        returns a new Vector with the corresponding coordinates substracted
        :param other: (Vector) the Vector to substract
        :return: (Vector)
        """
        if isinstance(other, Vector):
            return Vector(self.x1 - other.x1, self.x2 - other.x2, self.x3 - other.x3)
        else:
            raise ValueError()

    def __isub__(self, other):
        """
        substracts the coordinates of the given Vector from the coordinates of this object
        :param other: (Vector) the Vector to substract
        :return: (void)
        """
        if isinstance(other, Vector):
            self.x1 -= other.x1
            self.x2 -= other.x2
            self.x3 -= other.x3
        else:
            raise ValueError()

    def __mul__(self, other):
        """
        either performs a skalar multiplication between two vectors and returns the integer result or returns a
        new vector, when given an integer to multiply every coordinate with
        :param other: (int) the value to multiply every coordinate with
        :param other: (Vector) the Vector to perform skalar multiplication with
        :return: (Vector), (int)
        """
        if isinstance(other, Vector):
            return self.x1 * other.x1 + self.x2 * other.x2 + self.x3 * other.x3
        if other is int:
            return Vector(self.x1 * other, self.x2 * other, self.x3 * other)
        else:
            raise ValueError()

    def __imul__(self, other):
        """
        when given an integer multiplies it with every coordinate of the Vector
        :param other: (int) a value
        :return: (void)
        """
        if other is int:
            self.x1 *= other
            self.x2 *= other
            self.x3 *= other
        else:
            raise ValueError()

    def __mod__(self, other):
        """
        performs a vector multiplication of two objects and returns the created Vector
        :param other: (Vector)
        :return: (Vector)
        """
        if isinstance(other, Vector):
            x1 = self.x2 * other.x3 - self.x3 * other.x2
            x2 = self.x3 * other.x1 - self.x1 * other.x3
            x3 = self.x1 * other.x2 - self.x2 * other.x1
            return Vector(x1, x2, x3)
        else:
            raise ValueError()

    def __imod__(self, other):
        """
        performs a vector multiplication of two vectors and assigns the created coordinates to the object itself
        :param other: (Vector)
        :return: (Vector)
        """
        if isinstance(other, Vector):
            vector = self % other
            self.x1 = vector.x1
            self.x2 = vector.x2
            self.x3 = vector.x3
        else:
            raise ValueError()

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x1 == other.x1 and self.x2 == other.x2 and self.x3 == other.x3
        else:
            return False

    def _calc_length(self):
        """
        calculates the length of the Vector based on the 3 given coordinates
        :return: (void)
        """
        self.length = ((self.x1**2)+(self.x2**2)+(self.x3**2))**0.5

    def angle(self, vector):
        """
        returns the angle between this vector and the vector given
        :param vector: (Vector) the vector to use in the calculation
        :return:(int)
        """
        return math.acos((self * vector)/(self.length * vector.length))

    def vertical(self, vector):
        """
        returns whether two vectors are vertical to each other or not
        :param vector: (Vector) vector to check with
        :return: (bool)
        """
        return self * vector == 0
