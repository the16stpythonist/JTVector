__author__ = 'Jonas'
from JTVector.dimensions import DimensionalObject
from JTVector.dim3.vertex import Point
from JTVector.dim3.vertex import Vector


class MultivectorialObject(DimensionalObject):
    """
    a base class for objects consisting of multiple vectors rather than coordinates alone
    :var dimensions: (int) the amount of dimensions, the object is represented in
    :var support_vector: (Vector) the Vector pointing from the origin to the point at which the directional vectors of
                                  the object starts
    """
    def __init__(self):
        super(MultivectorialObject, self).__init__()
        self.dimensions = 3
        self.support_vector = None


class InfiniteObject:
    """
    An interface like object that is extended by vectorial objects, that are infinite within the coordinate space
    """
    pass


class Line(MultivectorialObject, InfiniteObject):
    """
    :var dimensions: (int) the amount of dimensions, the object is represented in
    :var support_vector: (Vector) the Vector pointing from the origin to the point at which the directional vectors of
                                  the object starts
    :var direction_vector: (Vector) the vector giving the direction into which the line is going
    """
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__()
        self.direction_vector = None
        if len(args) == 2:
            arg1 = args[0]
            arg2 = args[1]

            if isinstance(arg1, Vector) and isinstance(arg2, Vector):
                self.support_vector = arg1
                self.direction_vector = arg2

            elif isinstance(arg1, Point) and isinstance(arg2, Vector):
                self.support_vector = Vector(arg1)
                self.direction_vector = arg2

            elif isinstance(arg1, Vector) and isinstance(arg2, Point):
                self.support_vector = Vector(arg2)
                self.direction_vector = arg1

            elif isinstance(arg1, Point) and isinstance(arg2, Point):
                self.support_vector = Vector(arg1)
                self.direction_vector = Vector(arg1, arg2)

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, other):
        """
        returns whether the given Point is on the line
        :param other: (Point) the point to check
        :return: (boolean)
        """
        if isinstance(other, Point):
            # using the abstract procedure of placing the Line and the Point equal and checking whether the parameter
            # t is giving the same result in all three equations
            t1 = (other.x1 - self.support_vector.x1) / self.direction_vector.x1
            t2 = (other.x2 - self.support_vector.x2) / self.direction_vector.x2
            t3 = (other.x3 - self.support_vector.x3) / self.direction_vector.x3
            return t1 == t2 and t1 == t3

        else:
            raise ValueError()

