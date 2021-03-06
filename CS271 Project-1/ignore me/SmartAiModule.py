from Cost import CostFunction
from DepthFirstSearch import DFS
import GameBoard
import legalMovesList
import DepthFirstSearch
#import Cost


#Make  a super class called AI? for inheritance?
class Ai2(object):
	
	#=======================================================================
	#				Initialization
	#=======================================================================
	def __init__(self, marker):
		self.marker = marker
		self.bestMoveX = -1
		self.bestMoveY = -1
		
	def make_move(self):
		self.get_best_move()
		return (self.bestMoveX, self.bestMoveY)
		
class BasicAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self):
		dfs = DFS(self.marker)
		cost = dfs.rootCost
		cost.findBestQuickMove()
		self.bestMoveX = cost.bestX
		self.bestMoveY = cost.bestY
	
		#note to self get rid of this call in dumb ai
		#self.takeMove(cost.bestX, cost.bestY)
		cost.close()

class AdvAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self):
		pass
		
class RandomAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self):
		move = random.randint(0, legalMovesList.legalMovesAvailable - 1)
		legalMovesList.takeTileByIndex(move, self.marker)
		self.bestMoveX = legalMovesList.prevX
		self.bestMoveY = legalMovesList.prevY

class MidAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self):
		move = legalMovesList.legalMovesAvailable / 2
		legalMovesList.takeTileByIndex(move, self.marker)
		self.bestMoveX = legalMovesList.prevX
		self.bestMoveY = legalMovesList.prevY	
