#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

from traceylib.primitive import *

class Scene(object):
	objects = []
	lights = []

class DemoScene(Scene):
	def __init__(self, width, height):
		max_size = 10

		scaleX = width / max_size
		scaleY = height / max_size
		scaleZ = 5*max_size

		self.objects.append( Sphere( 0,0,1*scaleZ, 1*scaleX, (0.0,1.0,0.5) ) )
		self.objects.append( Sphere( 2*scaleX,0,0, 1*scaleX, (1.0,0.1,0.1) ) )
		self.objects.append( Plane( 0,-1,0, 1.5*scaleY, (0,0,1.0) ) )

		self.lights.append( Light( 0, scaleX*50, -scaleX*-50, (1.0,1.0,1.0) ))
		self.lights.append( Light( scaleX*-50, -scaleX*50, scaleX*-50, (1.0,1.0,1.0) ))

