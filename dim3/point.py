__author__ = 'Jonas'
from JTVector.dim3.vertex import Vertex
from JTVector.dim3.vector import Vector


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
                    if arg is not int:
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



