#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

from __future__ import division
from math import sqrt
from traceylib.vector import *


class RaytracableObject(object):
	def __init__(self, color):
		self.color = color

	def intersect(self, origin, direction):
		return False

	def getDiffuse(self, intersection):
		return self.color


class Light(RaytracableObject):
	def __init__(self, px, py, pz, color):
		self.color = color
		self.x = px
		self.y = py
		self.z = pz

class Sphere(RaytracableObject):
	def __init__(self, sx, sy, sz, radius, color):
		self.pos = Vector(sx, sy, sz)
		self.radius = radius
		self.color = color

		self.normal = Vector(0,0,0)

	def __repr__(self):
		return "Sphere %f,%f,%f r=%f" % (self.pos.x, self.pos.y, self.pos.z, self.radius)

	def intersect(self, origin, direction):
		sx=self.pos.x
		sy=self.pos.y
		sz=self.pos.z
		sr=self.radius

		B = 2*(direction.x*(origin.x-sx) + direction.y*(origin.y-sy) + direction.z*(origin.z-sz))
		C = (origin.x-sx)**2 + (origin.y-sy)**2 + (origin.z-sz)**2 - sr**2

		d = B**2 - 4*C

		if d==0:
			return -B / (2)
		
		if (d > 0):
			dd = sqrt(d)

			t0 = ( -B - dd ) / (2)
			return t0

		return False

	def computeNormal(self, intersection):
		sri = 1/self.radius

		self.normal.x = (intersection.x-self.pos.x)*sri
		self.normal.y = (intersection.y-self.pos.y)*sri
		self.normal.z = (intersection.z-self.pos.z)*sri
		return self.normal

class Plane(RaytracableObject):
	def __init__(self, A,B,C, D, color):
		self.A=A
		self.B=B
		self.C=C
		self.D=D
		self.normal = Vector(-self.A, -self.B, -self.C)
		self.color = color

	def __repr__(self):
		return "Plane %f %f, %f %f" % (self.A, self.B, self.C, self.D)

	def intersect(self, origin, direction):
		vd = self.A*direction.x + self.B*direction.y + self.C*direction.z
		if vd >= 0:
			return False

		v0 = -(self.A*origin.x + self.B*origin.y + self.C*origin.z + self.D)

		t=v0/vd
		return t

	def computeNormal(self, intersection):
		return self.normal

	def getDiffuse(self, intersection):
		return self.color
