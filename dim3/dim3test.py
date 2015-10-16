__author__ = 'Jonas'
from JTVector.dim3.vertex import Vector
from JTVector.dim3.vertex import Point
import unittest


class TestPoint(unittest.TestCase):

    def test_construction(self):
        with self.assertRaises(ValueError):
            Point(1, 2, "string")
        point1 = Point(1, 2, 3)
        self.assertEqual(point1.x1, 1)
        self.assertEqual(point1.x2, 2)
        self.assertEqual(point1.x3, 3)

        point2 = Point(point1)
        self.assertEqual(point2.x1, 1)
        self.assertEqual(point2.x2, 2)
        self.assertEqual(point2.x3, 3)

    def test_distance(self):
        point = Point(2, 2, 1)
        self.assertEqual(point.distance(), 3)


class TestVector(unittest.TestCase):

    def test_construction(self):
        with self.assertRaises(ValueError):
            Vector("str", 0, 0)
        vector1 = Vector(2, 2, 1)
        self.assertEqual(vector1.x1, 2)
        self.assertEqual(vector1.x2, 2)
        self.assertEqual(vector1.x3, 1)
        self.assertEqual(vector1.length, 3)

        vector2 = Vector(vector1)
        self.assertEqual(vector2.x1, 2)
        self.assertEqual(vector2.x2, 2)
        self.assertEqual(vector2.x3, 1)
        self.assertEqual(vector2.length, 3)

        vector3 = Vector(Point(2, 2, 1))
        self.assertEqual(vector3.x1, 2)
        self.assertEqual(vector3.x2, 2)
        self.assertEqual(vector3.x3, 1)
        self.assertEqual(vector3.length, 3)

        vector4 = Vector(Point(1, 1, 1), Point(2, 2, 2))
        self.assertEqual(vector4.x1, 1)
        self.assertEqual(vector4.x2, 1)
        self.assertEqual(vector4.x3, 1)

    def test_addition(self):
        with self.assertRaises(ValueError):
            Vector(1, 1, 1) + "string"
        vector1 = Vector(1, 1, 1)
        vector2 = Vector(3, 3, 3)
        vector_result = vector1 + vector2
        self.assertEqual(vector_result.x1, 4)
        self.assertEqual(vector_result.x2, 4)
        self.assertEqual(vector_result.x3, 4)

        vector1 += vector2
        self.assertEqual(vector1.x1, 4)
        self.assertEqual(vector1.x2, 4)
        self.assertEqual(vector1.x3, 4)

    def test_difference(self):
        with self.assertRaises(ValueError):
            Vector(1, 1, 2) - "string"
        vector1 = Vector(1, 1, 0)
        vector2 = Vector(1, 1, 1)
        vector_result = vector1 - vector2
        self.assertEqual(vector_result.x1, 0)
        self.assertEqual(vector_result.x2, 0)
        self.assertEqual(vector_result.x3, -1)

        vector1 -= vector2
        self.assertEqual(vector1.x1, 0)
        self.assertEqual(vector1.x2, 0)
        self.assertEqual(vector1.x3, -1)

    def test_multiplication(self):
        with self.assertRaises(ValueError):
            Vector() * "string"
        vector1 = Vector(2, 2, 2)
        vector2 = Vector(3, 3, 3)
        vector_result = vector1 * 2
        self.assertEqual(vector_result.x1, 4)
        self.assertEqual(vector_result.x2, 4)
        self.assertEqual(vector_result.x3, 4)

        result = vector1 * vector2
        self.assertEqual(result, 18)

        vector1 *= 2
        self.assertEqual(vector1.x1, 4)
        self.assertEqual(vector1.x2, 4)
        self.assertEqual(vector1.x3, 4)

    def test_modulo(self):
        with self.assertRaises(ValueError):
            Vector() % "string"
        vector1 = Vector(2, 1, 2)
        vector2 = Vector(3, 3, 3)
        vector_result = vector1 % vector2
        self.assertEqual(vector_result.x1, -3)
        self.assertEqual(vector_result.x2, 0)
        self.assertEqual(vector_result.x3, 3)

    def test_parallel(self):
        self.assertTrue(Vector(1, 2, 4).parallel(Vector(3, 6, 12)))
        self.assertFalse(Vector(1, 1, 1).parallel(Vector(1, 2, 5)))

    def test_vertical(self):
        self.assertTrue(Vector(1, 1, 1).vertical(Vector(2, 3, 7) % Vector(1, 1, 1)))
        self.assertFalse(Vector(1, 1, 1).vertical(Vector(3, 3, 7)))

    def test_angle(self):
        self.assertEqual(Vector(2, 1, 2).angle(Vector(2, 1, 2) % Vector(7, 3, 16)), 90)

if __name__ == '__main__':
    unittest.main()
