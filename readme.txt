
Tracey - The beam splitter
==========================

About
-----

Tracey is a simplistic raytracer implemented in Python.

Goals
-----

Tracy is made because raytracers are cool, and the author also want to
implement one.

The intention is to implement features that will make the raytracer
better and faster while the code is still understanable.

Requirements
------------

Python 2.x
PIL for image output
psyco for improved performance

Supported features
------------------

Tracey supports:

- Rendering output:
   * image file (using PIL)
   * terminal (ASCII)
- Primitives:
   * Plane
   * Sphere
- Lights:
   * Ambient
   * Omnidirectional
- Reflection
- Camera:
   * Fixed position

Coordinate system
-----------------

The coordinate system used in Tracey is:

 z-----> x
 | (positive z into screen)
 |
 y


Ideas
-----

The following are ideas for what to implement next:

- Material support (solid color material, checkerboard material, texture)
- Procedural generation of textures/materials
- Improve screen support (ansi, pygame)
- Polygon support
- Scene loading from file (special format or povray?)
- Better demo scene
- Refraction (glass spheres over checkerboard!)
