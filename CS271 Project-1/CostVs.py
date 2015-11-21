
from Gui import NONE, PLAYER1, PLAYER2
import random

illegalSpace = -999
boardLength  = 0
MOVES_TO_WIN = 4

#How many best nodes to track?
maxBranchingFactor = 16

class CostFunction(object):


#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker, board, length):
		global boardLength, NONE, PLAYER2, PLAYER1
		self.marker = marker
		self.board  = board
		self.boardLength = length
		self.tiles = [[0] * self.boardLength for i in range(self.boardLength)]
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
			
				#My piece on board
				if self.board[i][j] == marker:
					self.tiles[i][j] = illegalSpace
					self.upMaxValues(i, j, 1)
				
				#Empty Space on board
				elif self.board[i][j] == NONE:
				
					#Empty Space not on sides of board is better
					#if (i > 0) and i < (self.boardLength - 1):
					#	if (j > 0) and j < (self.boardLength - 1):
					#		self.tiles[i][j] = self.tiles[i][j] + 1
				
				#Opp space on board
				else:
					self.tiles[i][j] = illegalSpace
					self.upMinValues(i, j, 1)
					
		self.bestX = -1
		self.bestY = -1	
		
		#So we don't expand too many nodes, track some min value to expand
		self.leastMax = 2
		self.leastMin = 2
				
#=======================================================================
#	METHOD TO FIND BEST MOVE
#=======================================================================					
	#Make quick adjustment to board for 1 single move
	def makeMove(maxOrMin, i, j):
		self.tiles[i][j] = illegalSpace
		if maxOrMin:
			self.upMaxValues(i, j, 1)
		else:
			self.upMinValues(i, j, 1)
			
		self.leastMax = _findLowerBoundValue(True)
		self.leastMin = _findLowerBoundValue(False)
	
	def findBestQuickMove(self):
		self._findBestQuickValue(True)

	def findBestMove(self, maxOrMin):
		if maxOrMin:
			return _findBestQuickValue(True)
		else:
			return _findBestQuickValue(False)
	
	def _findBestQuickValue(self, maxOrMin):
		if maxOrMin:
			bestValue = -1
		else:
			bestValue = 1
		
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
				if self.tiles[i][j] == illegalSpace:
					continue
					
				value = self.tiles[i][j]

				if (maxOrMin and value > bestValue) or (not maxOrMin and value < bestValue):
					bestValue = value
					
					#Start a new array of best moves
					xList = []
					yList = []
				
				if (maxOrMin and value >= bestValue) or (not maxOrMin and value <= bestValue):
					xList.append(i)
					yList.append(j)
		
		#Pick random same index from lists
		index = random.randint(0, len(xList) - 1)
		self.bestX = xList[index]
		self.bestY = yList[index]
		
		return bestValue
		
	#Used to find the min value to search in branching
	#will not open nodes below a threshold
	def _findLowerBoundValue(self, maxOrMin):
		global maxBranchingFactor
		valueList = [0] * maxBranchingFactor
		
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
				if self.tiles[i][j] == illegalSpace:
					continue
					
				value = self.tiles[i][j]

				if maxOrMin:
					#replace min value
					min = _findMin(valueList)
					if value > min:
						_replace(valueList, min, value)
				#Replace max value
				else:
					max = _findMax(valueList)
					if value < max:
						_replace(valueList, max, value)
		
		#Return the lowest acceptable value
		if maxOrMin:
			return _findMin(valueList)
		else:
			return _findMax(valueList)	

	def _findMin(self, valueList):
		min  = 999
		for i in range(0, len(valueList)):
			if valueList[i] < min:
				min = valueList[i]
		return min

	def _replace(self, valueList, oldValue, newValue):
		for i in range(0, len(valueList)):
			if valueList[i] == oldValue:
				valueList[i] = newValue
				break
				
	def _findMax(self, valueList):
		max  = -999
		for i in range(0, len(valueList)):
			if valueList[i] > max:
				max = valueList[i]
		return max

	def close(self):
		self.tiles = -1
					
#=======================================================================
#	PRIVATE METHOD TO CHANGE COST FUNCTIONS
#=======================================================================			
	def upMaxValues(self, x, y, value):
		self.upValues(x, y, value, True)
					
	def upMinValues(self, x, y, value):
		self.upValues(x, y, value, False)
					
	def upValues(self, x, y, value, maxOrMin):
		if maxOrMin:
			mod = value
		else:
			mod = value * -1
		
		matrix = self.tiles
		
		for i in range(0, self.boardLength):
			for j in range(0, boardLength):
				if matrix[i][j] == illegalSpace:
					continue
			
				xDiff = abs(x - i)
				yDiff = abs(y - j)
			
				#Same Row
				if yDiff == 0 and xDiff < MOVES_TO_WIN:
						matrix[i][j] = matrix[i][j] + mod
				
				#Same Column
				if xDiff == 0 and yDiff < MOVES_TO_WIN:
						matrix[i][j] = matrix[i][j] + mod		
						
				#Same Diagonal
				if xDiff == yDiff and yDiff < MOVES_TO_WIN:
					matrix[i][j] = matrix[i][j] + mod				
					
