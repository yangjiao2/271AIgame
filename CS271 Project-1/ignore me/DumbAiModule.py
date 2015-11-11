#Static init,
#   If there are three peices in a row, by either color, then immediately try to fill it
#		If current player has three in a row, try to make 4, or stop opponent three in a row
#	Improve by only looking for peices that at most distance 4 away from existing peices

#Alternate between these two players and just fill the board
import GameBoard
import random
import legalMovesList

freeTiles = [[0] * GameBoard.boardLength for i in range(GameBoard.boardLength)]
isDebugMode = False
i = 0

#Make  a super class called AI? for inheritance?
class Ai(object):

	bestMoveX = -1
	bestMoveY = -1
	
	#=======================================================================
	#				Initialization
	#=======================================================================
	def __init__(self, marker):
		self.marker = marker

	def takeMove(self, move):
		legalMovesList.takeTileByIndex(move, self.marker)
		self.bestMoveX = legalMovesList.prevX
		self.bestMoveY = legalMovesList.prevY
		if isDebugMode == True:
			if freeTiles[self.bestMoveX][self.bestMoveY] == 0:
				#print "Tile [%d,%d]" % (legalMovesList.prevX, legalMovesList.prevY)
				#print i
				freeTiles[self.bestMoveX][self.bestMoveY] = self.marker
			else:	
				print "Fail! Tile [%d,%d] is already taken!" % (legalMovesList.prevX, legalMovesList.prevY)
		
		#Log the move into the gameboard
		GameBoard.takeTile(self.bestMoveX, self.bestMoveY, self.marker)

class RandomAi(Ai):
	#=======================================================================
	#				Functions
	#=======================================================================
	def takeDumbMove(self):
		move = random.randint(0, legalMovesList.legalMovesAvailable - 1)
		self.takeMove(move)

class MidAi(Ai):
	#=======================================================================
	#				Functions
	#=======================================================================
	def takeDumbMove(self):
		move = legalMovesList.legalMovesAvailable / 2
		self.takeMove(move)

#=======================================================================
#				Debug Main
#=======================================================================
if isDebugMode == True:
	while legalMovesList.legalMovesAvailable > 0:
		i = i + 1
		takeDumbMove()	#can use i for debugging
			
	GameBoard.printMatrix(freeTiles)	
