__author__ = 'Jonas'


class DimensionalObject:
    """
    An abstract base class representing a multidimensional object
    :var dimensions: (int) the amount of dimensions, the object is represented in
    """
    def __init__(self):
        self.dimensions = 0

    def same_dimension(self, object):
        """
        returns whether this and the given object are present in the same dimensions
        :param object: (DimensionalObject) the object to compare with
        :return: (boolean)
        """
        if isinstance(object, DimensionalObject):
            if object.dimensions == self.dimensions:
                return True
            else:
                return False
        else:
            return False

    def upper_dimension(self, object):
        """
        returns whether this object is within a higher dimension than the other given object
        :param object: (DimensionalObject) the object to compare with
        :return: (boolean)
        """
        if isinstance(object, DimensionalObject):
            if object.dimensions < self.dimensions:
                return True
            else:
                return False
        else:
            raise ValueError()

    def lower_dimension(self, object):
        """
        returns whether this object is within a lower dimension than the other given object
        :param object: (DimensionalObject) the object to compare with
        :return:(boolean)
        """
        if isinstance(object, DimensionalObject):
            if object.dimensions > self.dimensions:
                return True
            else:
                return False
        else:
            raise ValueError()
