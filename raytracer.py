#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

from __future__ import division
import time
import sys
import traceylib.screen
import traceylib.engine
import traceylib.scene
from optparse import OptionParser

# Speed up rendering if psyco is available
try:
	import psyco
	psyco.full()
except:
	pass

def main():
	profile_file = "tracey_profile.out"

	print ""
	print traceylib.engine.version_string
	print "-"*len(traceylib.engine.version_string)
	print ""

	parser = OptionParser(usage="python %prog")
	parser.add_option("-o", "--output", dest="output", default="ascii",
		help="Render output: ascii [default], pil")

	parser.add_option("-s", "--size", dest="size",
		help="Set render size: hxw Example: 320x240")

	parser.add_option("-p", "--profile", dest="profile", action="store_true",
		default=False, help="Run profiler and output result to" + profile_file)

	(options, args) = parser.parse_args()

	width = None
	height = None
	if options.size:
		try:
			width, height = [int(x) for x in options.size.split("x")]
		except:
			print "Unknown size format '%s'" % (options.size)
			parser.print_help()
			sys.exit(1)

	if options.output == "pil":
		if not width:
			width = 320
			height = 240
		screen = traceylib.screen.PILImageScreen(width, height)
	elif options.output == "ascii":
		if not width:
			width = 80
			height = 25
		screen = traceylib.screen.TextScreen(width, height)
	else:
		print "Unknown output format '%s'" % (options.output)
		parser.print_help()
		sys.exit(1)

	scene = traceylib.scene.DemoScene(screen.width, screen.height)

	raytracer = traceylib.engine.Raytracer(screen, scene)

	starttime = time.time()

	if options.profile:
		import cProfile
		cProfile.run("raytracer.run()", profile_file)
		import pstats
		p = pstats.Stats(profile_file)
		p.sort_stats('time')
		p.print_stats()
	else:
		raytracer.run()

	endtime = time.time()

	screen.show()

	print "Render time %d sec" % (endtime-starttime)

if __name__ == "__main__":
	main()
