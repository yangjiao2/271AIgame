

length = 0

def setLength(x):
	global length
	length = x

class Node(object):
	def __init__(self, x, y):
		global length
		self.x = x
		self.y = y
		
		# Value of this node
		self.MaxValue = 0
		self.MinValue = 0
		
		#points to end of child list, is current count
		self.size  = 0
		
		self.children = [None] * (length * length)
		
		#Alpha-Beta pruning
		self.alpha = -999
		self.beta = 999
	
	#Debug printing
	def description(self):
		print self.x, self.y, self.MaxValue, self.MinValue
	
	# add child to list
	def addChild(self, child):
		self.children[self.size] = child
		self.size = self.size + 1
		
	#set value	
	def setMaxValue(self, value):
		self.MaxValue = value
		
	#def setMinValue(self, value):
	#	self.MinValue = value
	
	def copyValues(self, max, min):
		self.MaxValue = max
		self.MinValue = min
		
	def copyNodeValues(self, node):
		self.copyValues(node.MaxValue, node.MinValue)	
		
	def setAlpha(self, value):
		self.alpha = value

	def setBeta(self, value):
		self.beta = value		
		
#root = Node(3, 4)
#root.description()		

