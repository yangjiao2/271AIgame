
import GameBoard

illegalSpace = -999
opponentMove = -1
boardLength = 0

class CostFunction(object):

#=======================================================================
#	INITIALIZATION
#=======================================================================	
	def __init__(self, marker):
		global boardLength
		self.marker = marker
		boardLength = GameBoard.boardLength
		self.tiles = [[0] * boardLength for i in range(boardLength)]
		for i in range(0, boardLength):
			for j in range(0, boardLength):
			
				#My piece on board
				if GameBoard.freeTiles[i][j] == marker:
					self.tiles[i][j] = illegalSpace
					self.upValues(i, j, 1)	#for now....
				
				#Empty Space on board
				elif GameBoard.freeTiles[i][j] == 0:
				
					#Empty Space not on sides of board is better
					if (i > 0) and i < (boardLength - 1):
						if (j > 0) and j < (boardLength - 1):
							self.tiles[i][j] = self.tiles[i][j] + 1
				
				#Opp space on board
				else:
					self.tiles[i][j] = illegalSpace
					#self.upValues(i, j, -1)	#for now....
					
		self.bestX = -1
		self.bestY = -1	
				
#=======================================================================
#	METHOD TO FIND BEST MOVE
#=======================================================================					
	def findBestMove(self):
		bestValue = -1
		
		for i in range(0, boardLength):
			for j in range(0, boardLength):
				if self.tiles[i][j] == illegalSpace:
					continue
					
				absValue = abs(self.tiles[i][j])

				if absValue > bestValue:
					bestValue = absValue
					self.bestX = i
					self.bestY = j	
	
	def close(self):
		self.tiles = -1
					
#=======================================================================
#	PRIVATE METHOD TO CHANGE COST FUNCTIONS
#=======================================================================			
	def upValues(self, x, y, value):
		for i in range(0, boardLength):
			for j in range(0, boardLength):
				if self.tiles[i][j] == illegalSpace:
					continue
			
				xDiff = abs(x - i)
				yDiff = abs(y - j)
			
				#Same Row
				if yDiff == 0 and xDiff < 5:
						self.tiles[i][j] = self.tiles[i][j] + value
				
				#Same Column
				if xDiff == 0 and yDiff < 5:
						self.tiles[i][j] = self.tiles[i][j] + value		
						
				#Same Diagonal
				if xDiff == yDiff and yDiff < 5:
					self.tiles[i][j] = self.tiles[i][j] + value