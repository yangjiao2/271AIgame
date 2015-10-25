class ChoiceNode(object):

	# Value of this node
	value = 0
	
	# List of children at most 63
	children = [None] * 63
	
	#points to end of child list, is current count
	size = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	#Debug printing
	def description(self):
		print self.x, self.y, self.value
	
	# add child to list
	def addChild(self, child):
		self.children[size] = child
		self.size = self.size + 1
		
	#set value	
	def setValue(self, value):
		self.value = value
		

#root = Node(3, 4)
#root.description()		