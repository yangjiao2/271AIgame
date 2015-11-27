
NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'

# from Gui import NONE, PLAYER1, PLAYER2
import random

illegalSpace = -999
MOVES_TO_WIN = 4

#How many best nodes to track?
maxBranchingFactor = 16

class CostFunction(object):


#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker, board, length):
		global NONE, PLAYER2, PLAYER1
		self.alphaBetaTrue = False
		self.marker = marker
		self.board  = board
		self.boardLength = length
		self.hasWinningMove = False
		self.max = [[0] * self.boardLength for i in range(self.boardLength)]
		self.min = [[0] * self.boardLength for i in range(self.boardLength)]

		self.bestX = -1
		self.bestY = -1	
		self._checkWinningMove()

		#No point in search if we know the winning move
		if not self.hasWinningMove:
			for i in range(0, self.boardLength):
				for j in range(0, self.boardLength):
				
					#My piece on board
					if self.board[i][j] == marker:
						self.max[i][j] = illegalSpace
						self.min[i][j] = illegalSpace
						self.upMaxValues(i, j, 1)
					
					#Empty Space on board
					elif self.board[i][j] == NONE:
					
						#Empty Space not on sides of board is better
						if (i > 0) and i < (self.boardLength - 1):
							if (j > 0) and j < (self.boardLength - 1):
								self.max[i][j] = self.max[i][j] + 1
								self.min[i][j] = self.min[i][j] + 1
					
					#Opp space on board
					else:
						self.max[i][j] = illegalSpace
						self.min[i][j] = illegalSpace
						self.upMinValues(i, j, 1)
						

		
		#So we don't expand too many nodes, track some min value to expand
		self.leastMax = 2
		self.leastMin = 2

	def _checkWinningMove(self):
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
			
				#My piece on board
				if self.board[i][j] != NONE:
					self._checkWin(i ,j)
					if self.bestX != -1 and self.bestY != -1:
						self.hasWinningMove = True
						return
					

	def _checkWin(self, i, j):
		#Check if there's a winning x 
		if i + 2 < self.boardLength:
			if self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j]:
				if i - 1 >= 0 and self.board[i-1][j] == NONE:
					self.bestX = i - 1
					self.bestY = j
					return
				elif i + 3 < self.boardLength and self.board[i+3][j] == NONE:
					self.bestX = i + 3
					self.bestY = j
					return
		#Check if there's a winning y			
		if j + 2 < self.boardLength:
			if self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j+2]:
				if j - 1 >= 0 and self.board[i][j-1] == NONE:
					self.bestX = i
					self.bestY = j - 1
					return
				elif j + 3 < self.boardLength and self.board[i][j+3] == NONE:
					self.bestX = i
					self.bestY = j + 3
					return			
		#Check if there's a winning diag			
		if i + 2 < self.boardLength and j + 2 < self.boardLength:
			if self.board[i][j] == self.board[i+1][j+1] and self.board[i][j] == self.board[i+2][j+2]:
				if i - 1 >= 0 and j - 1 >= 0 and self.board[i-1][j-1] == NONE:
					self.bestX = i - 1
					self.bestY = j - 1
					return
				elif i + 3 < self.boardLength and j + 3 < self.boardLength and self.board[i+3][j+3] == NONE:
					self.bestX = i + 3
					self.bestY = j + 3
					return
		if i + 2 < self.boardLength and j - 2 >= 0:
			if self.board[i][j] == self.board[i+1][j-1] and self.board[i][j] == self.board[i+2][j-2]:
				if i - 1 >= 0 and j + 1 < self.boardLength and self.board[i-1][j+1] == NONE:
					self.bestX = i - 1
					self.bestY = j + 1
					return
				elif i + 3 < self.boardLength and j - 3 >= 0 and self.board[i+3][j-3] == NONE:
					self.bestX = i + 3
					self.bestY = j - 3
					return					
				
#=======================================================================
#	METHOD TO FIND BEST MOVE
#=======================================================================					
	#Make quick adjustment to board for 1 single move
	def makeMove(self, maxOrMin, i, j):
		self.max[i][j] = illegalSpace
		self.min[i][j] = illegalSpace
		if maxOrMin:
			self.upMaxValues(i, j, 1)
		else:
			self.upMinValues(i, j, 1)
			
		self.leastMax = self._findLowerBoundValue(self.max)
		self.leastMin = self._findLowerBoundValue(self.min)	
	
	def findBestQuickMove(self):
		if self.hasWinningMove:
			return

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

	def findBestMove(self, maxOrMin):
		if maxOrMin:
			return self.findBestQuickValue (self.max)
		else:
			return self.findBestQuickValue (self.min)
	
	def findBestQuickValue(self, matrix):
		bestValue = -1
		
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
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
		
	#Used to find the min value to search in branching
	#will not open nodes below a threshold
	def _findLowerBoundValue(self, matrix):
		global maxBranchingFactor
		valueList = [0] * maxBranchingFactor
		
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
				if matrix[i][j] == illegalSpace:
					continue
					
				absValue = abs(matrix[i][j])

				#replace min value
				min = self._findMin(valueList)
				if absValue > min:
					self._replaceMin(valueList, min, absValue)
		
		#Return the lowest acceptable value
		return self._findMin(valueList)

	def _findMin(self, valueList):
		min  = 999
		for i in range(0, len(valueList)):
			if valueList[i] < min:
				min = valueList[i]
		return min

	def _replaceMin(self, valueList, oldValue, newValue):
		for i in range(0, len(valueList)):
			if valueList[i] == oldValue:
				valueList[i] = newValue
				break
	
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
		for i in range(0, self.boardLength):
			for j in range(0, self.boardLength):
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
					
