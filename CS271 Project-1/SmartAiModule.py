from Cost import CostFunction
import GameBoard
import legalMovesList
#import Cost

freeTiles = [[0] * GameBoard.boardLength for i in range(GameBoard.boardLength)]
isDebugMode = False
i = 0

#Make  a super class called AI? for inheritance?
class Ai2(object):
	
	#=======================================================================
	#				Initialization
	#=======================================================================
	def __init__(self, marker):
		self.marker = marker
		self.bestMoveX = -1
		self.bestMoveY = -1
		
	def takeMove(self, x, y):
		GameBoard.takeTile(x, y, self.marker)
		legalMovesList.takeTile(y, x, self.marker)
		
class BasicAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def takeDumbMove(self):
		cost = CostFunction(self.marker)
		cost.findBestMove()
		self.bestMoveX = cost.bestX
		self.bestMoveY = cost.bestY
	
		self.takeMove(cost.bestX, cost.bestY)
		cost.close()

class AdvAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def takeDumbMove(self):
		pass
