
import GameBoard
import random

illegalSpace = -999
boardLength  = 0
MOVES_TO_WIN = 4

class CostFunction(object):

#READ ME!
#This requires boardLength + Board [][]! Can be taken statically or by parameter

#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker):
	#	def __init__(self, marker, GameBoard):
		global boardLength
		self.marker = marker
		boardLength = GameBoard.boardLength
		self.max = [[0] * boardLength for i in range(boardLength)]
		self.min = [[0] * boardLength for i in range(boardLength)]
		for i in range(0, boardLength):
			for j in range(0, boardLength):
			
				#My piece on board
				if GameBoard.freeTiles[i][j] == marker:
					self.max[i][j] = illegalSpace
					self.min[i][j]   = illegalSpace
					self.upMaxValues(i, j, 1)
				
				#Empty Space on board
				elif GameBoard.freeTiles[i][j] == 0:
				
					#Empty Space not on sides of board is better
					if (i > 0) and i < (boardLength - 1):
						if (j > 0) and j < (boardLength - 1):
							self.max[i][j] = self.max[i][j] + 1
							self.min[i][j] = self.min[i][j] + 1
				
				#Opp space on board
				else:
					self.max[i][j] = illegalSpace
					self.min[i][j] = illegalSpace
					self.upMinValues(i, j, 1)
					
		self.bestX = -1
		self.bestY = -1	
				
#=======================================================================
#	METHOD TO FIND BEST MOVE
#=======================================================================					
	def findBestQuickMove(self):
		#First see if min can win...
		bestMin = self.findBestQuickValue(self.min)
		bestMinX = self.bestX
		bestMinY = self.bestY
		
		#See if max can win
		bestMax = self.findBestQuickValue(self.max)
		
		#If min can win soon, try to block
		if bestMin >= MOVES_TO_WIN and bestMin > bestMax:
			self.bestX = bestMinX
			self.bestY = bestMinY
		#Otherwise, default will keep Max Best	
	
	def findBestQuickValue(self, matrix):
		bestValue = -1
		
		for i in range(0, boardLength):
			for j in range(0, boardLength):
				if matrix[i][j] == illegalSpace:
					continue
					
				absValue = abs(matrix[i][j])

				if absValue > bestValue:
					bestValue = absValue
					
					#Start a new array of best moves
					xList = []
					yList = []
				
				if absValue >= bestValue:
					xList.append(i)
					yList.append(j)
		
		#Pick random same index from lists
		index = random.randint(0, len(xList) - 1)
		self.bestX = xList[index]
		self.bestY = yList[index]
		
		return bestValue
	
	def close(self):
		self.max = -1
		self.min = -1
					
#=======================================================================
#	PRIVATE METHOD TO CHANGE COST FUNCTIONS
#=======================================================================			
	def upMaxValues(self, x, y, value):
		self.upValues(x, y, value, self.max)
					
	def upMinValues(self, x, y, value):
		self.upValues(x, y, value, self.min)
					
	def upValues(self, x, y, value, matrix):
		for i in range(0, boardLength):
			for j in range(0, boardLength):
				if matrix[i][j] == illegalSpace:
					continue
			
				xDiff = abs(x - i)
				yDiff = abs(y - j)
			
				#Same Row
				if yDiff == 0 and xDiff < MOVES_TO_WIN:
						matrix[i][j] = matrix[i][j] + value
				
				#Same Column
				if xDiff == 0 and yDiff < MOVES_TO_WIN:
						matrix[i][j] = matrix[i][j] + value		
						
				#Same Diagonal
				if xDiff == yDiff and yDiff < MOVES_TO_WIN:
					matrix[i][j] = matrix[i][j] + value				
					
