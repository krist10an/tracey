#
# Tracey - the beam splitter
# --------------------------
# A Python Raytracer
#
# (c) kh 2011

class Screen(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	def putpixel(self, x, y, color):
		pass

	def show(self):
		pass

class TextScreen(Screen):
	def __init__(self, width, height):
		super(TextScreen, self).__init__(width, height)
		self.chars = [' ','.','-','~','=','c','o','*','x','X','@','#']
		self.delta = 256*3 / len(self.chars)

		self.buffer = [self.chars[0] for row in range(width * height)]

	def _get_char_index(self, color):
		color_index = (color[0] + color[1] + color[2])
		char_index = int(color_index / self.delta)

		if char_index > len(self.chars):
			#print "uh oh",color_index, self.delta, char_index, len(self.chars)
			char_index = len(self.chars) - 1

		return char_index

	def putpixel(self, x, y, color):
		self.buffer[y*self.width + x] = self.chars[self._get_char_index(color)]

	def show(self):
		str = ""
		for y in range(self.height - 1):
			for x in range(self.width - 1):
				char = self.buffer[y*self.width + x]
				str += char
			str += "\n"
		print str

class PILImageScreen(Screen):
	def __init__(self, width, height):
		from PIL import Image
		super(PILImageScreen, self).__init__(width, height)

		self.im = Image.new("RGB",(width, height))
		self.pix = self.im.load()

	def putpixel(self, x, y, color):
		self.pix[x,y] = color

	def show(self):
		output_filename = "output.png"
		self.im.save(output_filename)
		print "Saved result to", output_filename

if __name__=="__main__":
	text = TextScreen(40, 20)
	text.putpixel(4, 4, (255, 0, 0))
	text.putpixel(5, 4, (255, 255, 0))
	text.putpixel(6, 4, (255, 255, 255))
	text.putpixel(10, 15, (100, 100, 100))

	text.show()

	try:
		from PIL import Image
		image = PILImageScreen(160, 400)
		image.putpixel(4, 4, (255, 0, 0))
		image.putpixel(5, 4, (255, 255, 0))
		image.putpixel(6, 4, (255, 255, 255))
		image.putpixel(10, 15, (100, 100, 100))
		image.show()
	except:
		print "PIL not installed"
