
from ChoiceNode import Node
from Cost import CostFunction
import ChoiceNode
import Cost
import copy

depth  = 2	# Depth will be revalued to adjust for timing


class DFS(object):

#TODO keep a threshold of timing! if moves take over max, decrease depth
#if moves take less than min, increase depth!


#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker, board, boardLength):
		global depth

		self.marker = marker
		self.rootCost = CostFunction(marker, board, boardLength)
		self.boardLength = boardLength
		self.board = board
		ChoiceNode.setLength(self.boardLength)

	def _addChildren(self, parentNode, parentCost, maxOrMin, depth):
		global length
		
		#Add up to board children to parent
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
			
				#My piece on board
				if parentCost.max[i][j] != Cost.illegalSpace:
					
					#Don't expand too many nodes =================
					if maxOrMin and parentCost.max[i][j] < parentCost.leastMax:
						continue
						
					if not maxOrMin and parentCost.min[i][j] < parentCost.leastMin:
						continue	
					#=============================================
					
					newNode = Node(i, j)
					parentNode.addChild(newNode)
					
					#Create new cost function
					newCost = copy.copy(parentCost)

					#Modify cost function
					newCost.makeMove(maxOrMin, i, j)

					#call this to addchildren with !maxOrMin
					#do not expand on last depth
					if depth > 1:
						self.addChildren(newNode, newCost, not maxOrMin, depth - 1)
					else:
						newNode.setMaxValue(newCost.findBesMove(True))
						newNode.setMinValue(newCost.findBesMove(False))
						
					newCost.close()	
						
		#my cost is the best of my children
		bestValue = 0
		bestI = 0
		for i in range (0, parentNode.size):
			currNode = parentNode.children[i]
			currValue = 0
			if maxOrMin:
				currValue = currNode.MaxValue
			else:
				currValue = currNode.MinValue
			
			if currValue > bestValue:
				bestValue = currValue
				bestI = i
		
		bestNode = parentNode.children[bestI]
		parentNode.copyNodeValues(bestNode)
		
		return (bestNode.x, bestNode.y)
		
		#public handle for starting DFS
		def compute(self):
			global depth
			rootNode = Node(-1, -1)
			return self._addChildren(rootNode, self.rootCost, True, depth)