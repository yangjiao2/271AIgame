

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
		self.value = 0
		
		#points to end of child list, is current count
		self.size  = 0
		
		self.children = [None] * (length * length)
	
	#Debug printing
	def description(self):
		print self.x, self.y, self.value
	
	# add child to list
	def addChild(self, child):
		self.children[self.size] = child
		self.size = self.size + 1
		
	#set value	
	def setValue(self, value):
		self.value = value
		

#root = Node(3, 4)
#root.description()		