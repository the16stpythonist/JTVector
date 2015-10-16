__author__ = 'Jonas'
from JTVector.dimensions import DimensionalObject
import math


class Vertex(DimensionalObject):
    """
    An abstract base Object, representing all objects, that inherit clearly defined coordinates within a 3 dimensional
    space
    :var dimensions: (int) the amount of dimensions, the object is represented in
    :var x1: (double) the x coordinate of the Vertex object
    :var x2: (double) the y coordinate of the Vertex object
    :var x3: (double) the z coordinate of the Vertex object
    """
    def __init__(self):
        super(Vertex, self).__init__()
        self.dimensions = 3
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0

    def __getattr__(self, item):
        """
        behaviour in case the indexing operator is used on the object
        :param item: (int) the number of the dimension, whose coordinate is requested
        :return: (double) the coordinate
        """
        if item is int or item is str:
            if item == 1 or item == "x":
                return self.x1
            elif item == 2 or item == "y":
                return self.x2
            elif item == 3 or item == "z":
                return self.x3
            else:
                raise IndexError()
        else:
            raise IndexError()


class Point(Vertex):
    """
    a class representing a point within an 3 dimensional space
    :var dimensions: (int) the amount of dimensions, the object is represented in
    :var x1: (double) the x coordinate of the Vertex object
    :var x2: (double) the y coordinate of the Vertex object
    :var x3: (double) the z coordinate of the Vertex object
    """
    def __init__(self, *args, **kwargs):
        super(Point, self).__init__()
        if len(args) >= 1:
            if len(args) == 3:
                for arg in args:
                    if not (isinstance(arg, int) or isinstance(arg, float)):
                        raise ValueError()
                self.x1 = args[0]
                self.x2 = args[1]
                self.x3 = args[2]
            elif len(args) == 1:
                arg = args[0]
                if isinstance(arg, Point) or isinstance(arg, Vector):
                    self.x1 = arg.x1
                    self.x2 = arg.x2
                    self.x3 = arg.x3
        else:
            pass

    def distance(self):
        """
        calculates the distance to the origin
        :return: (int)
        """
        # pythagorean theorem
        return ((self.x1**2)+(self.x2**2)+(self.x3**2))**0.5


class Vector(Vertex):
    """
    An object representing a vector within the 3 dimensional space, not bound to a certain place but inheriting the
    vertex coordinates and a length. Vector objects are able to perform nearly every mathematical operation such as
    addition(+), substraction(-), skalar(*)- and cross(%)-multiplication by operator.
    :var dimensions: (int) the amount of dimensions, the object is represented in
    :var x1: (double) the x coordinate of the Vertex object
    :var x2: (double) the y coordinate of the Vertex object
    :var x3: (double) the z coordinate of the Vertex object
    :var length: (double) the length of the coordinate
    """
    def __init__(self, *args, **kwargs):
        super(Vector, self).__init__()
        if len(args) != 0:

            # assigning the dimensional coordinates
            if len(args) == 3:
                for arg in args:
                    if not (isinstance(arg, int) or isinstance(arg, float)):
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
                    self.x3 = arg2.x3 - arg1.x3
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
            return self + other
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
            return self - other
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
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x1 * other, self.x2 * other, self.x3 * other)
        else:
            raise ValueError()

    def __imul__(self, other):
        """
        when given an integer multiplies it with every coordinate of the Vector
        :param other: (int) a value
        :return: (void)
        """
        if isinstance(other, int) or isinstance(other, float):
            return self * other
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
            return self % other
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
        return math.degrees(math.acos((self * vector)/(self.length * vector.length)))

    def vertical(self, vector):
        """
        returns whether two vectors are vertical to each other or not
        :param vector: (Vector) vector to check with
        :return: (bool)
        """
        return self * vector == 0

    def parallel(self, vector):
        """
        returns whether the given vector is parallel to this vector
        :param vector: (Vector) the vector to test with
        :return: (boolean)
        """
        if isinstance(vector, Vector):
            # checks for a linear dependency of the two vectors
            t1 = self.x1 / vector.x1
            t2 = self.x2 / vector.x2
            t3 = self.x3 / vector.x3
            return t1 == t2 and t2 == t3
        else:
            raise ValueError()

    def normalize(self):
        """
        normalizes the vector, so it sets its length to 1
        :return: (void)
        """
        self.x1 /= self.length
        self.x1 /= self.length
        self.x1 /= self.length
