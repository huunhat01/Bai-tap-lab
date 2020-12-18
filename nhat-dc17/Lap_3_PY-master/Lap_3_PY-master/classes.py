class Greeter(object):
	# Constructor
	def __init__(self, name):
		self.name = name
	# Instance mathod
	def greet(self, loud = False):
		if loud:
			print('HELLO, %s!' % self.name.upper())
		else:
			print('hello, %s' % self.name)
g = Greeter('Fred')
g.greet()
g.greet(loud = True)