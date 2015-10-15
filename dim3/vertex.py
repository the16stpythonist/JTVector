__author__ = 'Jonas'
from JTVector.dimensions import DimensionalObject


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
