#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

from __future__ import division
from math import sqrt
from traceylib import primitive
from traceylib.vector import Vector

version_string = "Tracey - the beam splitter v1.0"

class Raytracer(object):
	def __init__(self, screen, scene):
		self.screen = screen
		self.scene = scene

	def intersect(self, origin, direction):
		boundary = 99999
		hit = boundary
		hit_object = False

		# Find object closest to the camera that intersects
		for current_object in self.scene.objects:
			t = current_object.intersect(origin, direction)

			if t and t>0.000000001:
				if t < hit:
					hit = t
					hit_object = current_object

		# Check if we did not hit anything
		if hit == boundary:
			return (False, False)

		return (hit, hit_object)


	def trace_ray(self, origin, direction, depth):
		color = (0,0,0)

		# Find closest object that intersects
		(t, hit_object) = self.intersect(origin, direction)
		if t:
			intersection = Vector(
						origin.x + direction.x*t,
						origin.y + direction.y*t,
						origin.z + direction.z*t )

			intersection_normal = hit_object.computeNormal(intersection)

			# Ambient lighting:
			dff=hit_object.getDiffuse(intersection)

			color = (dff[0]*0.0,
					 dff[1]*0.0,
					 dff[2]*0.0)

			# Diffuse lighing
			for light in self.scene.lights:
				lightvec = Vector(
					light.x - intersection.x,
					light.y - intersection.y,
					light.z - intersection.z)

				lightvec.normalize()

				dot = lightvec.dot_product(intersection_normal)

				# Add color if vectors are pointing in the same direction
				if dot>0:
					color = (
							color[0] + light.color[0]*dff[0] * dot,
							color[1] + light.color[1]*dff[1] * dot,
							color[2] + light.color[2]*dff[2] * dot
							)

			# Reflection
			refl=0.2 # Fixed reflections for all materials. Pretty awesome!
			if depth>1 and refl>0:

				# Find direction for reflection
				dotp = direction.dot_product(intersection_normal)
				refVect = Vector(
					direction.x - 2 * dotp * intersection_normal.x,
					direction.y - 2 * dotp * intersection_normal.y,
					direction.z - 2 * dotp * intersection_normal.z
					)

				# Trace reflection to get reflected color
				refc = self.trace_ray(intersection, refVect, depth-1);

				# If hit, we blend colors together
				invref=1-refl
				cc =  ( invref*color[0] + refl*refc[0],
						invref*color[1] + refl*refc[1],
						invref*color[2] + refl*refc[2] )
				color = cc

		return color

	def run(self):
		# Camera:
		origin = Vector(0,0,-255)
		direction = Vector(0,0,0)

		centerX = self.screen.width / 2
		centerY = self.screen.height / 2

		for y in range(self.screen.height):
			for x in range(self.screen.width):

				pixel_x = x - centerX
				pixel_y = y - centerY

				# Calculate direction
				direction.x = pixel_x
				direction.y = pixel_y
				direction.z = 255
				direction.normalize()

				# Trace ray
				color = self.trace_ray(origin, direction, 3)

				# Draw resulting color
				color = (int(color[0]*255), int(color[1]*255), int(color[2]*255))
				self.screen.putpixel(x, y, color)

