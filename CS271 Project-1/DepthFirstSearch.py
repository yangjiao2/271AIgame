
from ChoiceNode import Node
from Cost import CostFunction
import ChoiceNode
import Cost

depth  = 2	# Depth will be revalued to adjust for timing


class DFS(object):



#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker, board, boardLength):
		global depth

		self.marker = marker
		self.rootCost = CostFunction(marker, board, length)
		self.boardLength = boardLength
		self.board = board
		ChoiceNode.setLength(length)
		
		rootNode = Node(-1, -1)		# root has no choice

		self.addChildren(rootNode, self.rootCost, True, depth)

	def addChildren(self, parentNode, parentCost, maxOrMin, depth):
		global length
		
		#Add up to board children to parent
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
			
				#My piece on board
				if parentCost.max[i][j] != Cost.illegalSpace:
					
					#Don't expand too many nodes =================
					if maxOrMin and parentCost.max[i][j] <= 1:
						continue
						
					if not maxOrMin and parentCost.min[i][j] <= 1:
						continue	
					
					#=============================================
					
					newNode = Node(i, j)
					
					#Set value now?
					#newNode.setValue(parentCost.max[i][j])
					
					parentNode.addChild(newNode)
					
					#Make a new costfunction with change adjusted with just one move! occupied by max/min
					newCost = parentCost	#make a new modified one!
					
					#call this to addchildren with !maxOrMin
					#do not expand on last depth
					if depth > 1:
						self.addChildren(newNode, newCost, not maxOrMin, depth - 1)