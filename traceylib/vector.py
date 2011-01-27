#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

from math import sqrt
import unittest

class Vector(object):
	def __init__(self, x,y,z):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)

	def __repr__(self):
		return "v=(%f %f %f)" % (self.x, self.y, self.z)

	def normalize(self):
		length = sqrt(self.x**2 + self.y**2 + self.z**2)
		self.x = self.x / length
		self.y = self.y / length
		self.z = self.z / length

	def dot_product(self, other):
		return self.x * other.x + self.y * other.y + self.z * other.z

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def __mul__(self, scale):
		return Vector(self.x * scale, self.y * scale, self.z * scale)

	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)


class TestVector(unittest.TestCase):

	def test_add(self):
		v1 = Vector(2, 2, 2)
		v2 = Vector(1, 0, 0)
		res = v1 + v2

		self.assertEquals(res, Vector(3, 2, 2))

	def test_mul(self):
		v1 = Vector(1, 1, 1)
		res = v1 * 5

		self.assertEquals(res, Vector(5, 5, 5))

	def test_normal(self):
		res = Vector(0, 15, 0)

		res.normalize()
		self.assertEquals(res, Vector(0, 1, 0))

	def test_dotp(self):
		v1 = Vector(1, 2, 3)
		v2 = Vector(4, 5, 6)

		self.assertEquals(v1.dot_product(v2), 32)


if __name__=="__main__":
	unittest.main()
