from ChoiceNode import Node
from Cost import CostFunction
import ChoiceNode
import Cost
import copy

class DFS(object):

#TODO keep a threshold of timing! if moves take over max, decrease depth
#if moves take less than min, increase depth!


#=======================================================================
#	INITIALIZATION
#=======================================================================
	def __init__(self, marker, board, boardLength, dep, ab):
		global depth
		self.depthA  = dep	# Depth will be revalued to adjust for timing
		self.alphaBetaEnabled = ab
		
		self.marker = marker
		self.rootCost = CostFunction(marker, board, boardLength)
		self.boardLength = boardLength
		self.board = board
		ChoiceNode.setLength(self.boardLength)

	def _addChildren(self, parentNode, parentCost, maxOrMin, depth, alpha, beta):
		global length

		breakOut = False

		#Add up to board children to parent
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):

				#My piece on board
				if parentCost.max[i][j] != Cost.illegalSpace:

					#Don't expand too many nodes =================
					if maxOrMin and parentCost.max[i][j] < parentCost.leastMax:
						continue

					if parentCost.alphaBetaTrue:
						if not maxOrMin and parentCost.min[i][j] > parentCost.leastMin:
							continue
					else:
						if not maxOrMin and parentCost.min[i][j] < parentCost.leastMin:
							continue
					#=============================================

					newNode = Node(i, j)
					parentNode.addChild(newNode)

					#Create new cost function
					newCost = copy.deepcopy(parentCost)

					#Modify cost function
					newCost.makeMove(maxOrMin, i, j)
					
					#Don't search if this going to win
					if maxOrMin and newCost.hasLosingMove:
						newNode.setMaxValue(-1000)
					elif not maxOrMin and not newCost.hasLosingMove and newCost.hasWinningMove:
						newNode.setMaxValue(1000)
					else:
						#call this to addchildren with !maxOrMin
						#do not expand on last depth
						if depth > 1:
							self._addChildren(newNode, newCost, not maxOrMin, depth - 1, alpha, beta)

							newBeta  = newNode.beta

							#update alpha and beta
							if parentCost.alphaBetaTrue:
								if maxOrMin:
									alpha = max(alpha, newNode.beta)
									#print alpha #print here should not be -999
								else:
									beta = min(beta, newNode.alpha)
									#print beta #print here should not be 999

								if self.alphaBetaEnabled and alpha >= beta:
									breakOut = True
							#else:
							#	if maxOrMin:
							#		alpha = max(alpha, newNode.beta)
									#print alpha #print here should not be -999
							#	else:
							#		beta = max(beta, newNode.alpha)
									#print beta #print here should not be 999

								#is this logic right??
							#	if self.alphaBetaEnabled:
							#		if maxOrMin and alpha >= beta:
							#			breakOut = True
							#		elif not maxOrMin and alpha <= beta:
							#			breakOut = True

						else:
							newNode.setMaxValue(newCost.findBestMove(True) - newCost.findBestMove(False))
							#newNode.setMinValue(newCost.findBestMove(False))

					newCost.close()

				#Stop searching if alpha beta ended
				if breakOut:
					break
			if breakOut:
				break

		#my cost is the best of my children
		bestValue = 0
		bestI = 0
		for i in range (0, parentNode.size):
			currNode = parentNode.children[i]
			currValue = currNode.MaxValue

			if maxOrMin and currValue > bestValue:
				bestValue = currValue
				bestI = i
			elif not maxOrMin and currValue < bestValue:
				bestValue = currValue
				bestI = i


		if maxOrMin:
			parentNode.setAlpha(bestValue)
		else:
			parentNode.setBeta(bestValue)

		bestNode = parentNode.children[bestI]
		parentNode.copyNodeValues(bestNode)

		return (bestNode.x, bestNode.y)

	#public handle for starting DFS
	def compute(self):
		rootNode = Node(-1, -1)

		if self.rootCost.hasWinningMove:
			return (self.rootCost.bestX, self.rootCost.bestY)
		else:
			return self._addChildren(rootNode, self.rootCost, True, self.depthA, -999, 999)