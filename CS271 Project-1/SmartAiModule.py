from Cost import CostFunction
from DepthFirstSearch import DFS
# import legalMovesList
import DepthFirstSearch
#import Cost
import random
#Make  a super class called AI? for inheritance?
#from Gui import NONE,PLAYER1,PLAYER2
NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'

class Ai2():

	#=======================================================================
	#				Initialization
	#=======================================================================
	def __init__(self, marker, board, length, firstMove):
		self.marker = marker
		self.bestMoveX = -1
		self.bestMoveY = -1
		self.firstMove = firstMove

	def make_move(self, board, length):
		self.get_best_move(board, length)
		self.firstMove = False
		print "%s [%d %d]" % (self.marker, self.bestMoveY, self.bestMoveX)
		return (self.bestMoveY, self.bestMoveX)

class BasicAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self, board, length):
		dfs = DFS(self.marker, board, length)
		cost = dfs.rootCost
		cost.findBestQuickMove()
		self.bestMoveX = cost.bestX
		self.bestMoveY = cost.bestY
		cost.close()

class AdvAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self, board, length):
		dfs = DFS(self.marker, board, length)
		#Just go to depth 1 for first move
		if self.firstMove:
			cost = dfs.rootCost
			cost.findBestQuickMove()
			self.bestMoveX = cost.bestX
			self.bestMoveY = cost.bestY
			cost.close()

		else:
			self.bestMoveX, self.bestMoveY = dfs.compute()

class TrueAlphaAi(Ai2):

	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self, board, length):
		#Need to create a new Cost2 function!
		dfs = DFS(self.marker, board, length)
		#Just go to depth 1 for first move
		if self.firstMove:
			cost = dfs.rootCost
			cost.findBestQuickMove()
			self.bestMoveX = cost.bestX
			self.bestMoveY = cost.bestY
			cost.close()
		else:
			self.bestMoveX, self.bestMoveY = dfs.compute()

class RandomAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def __init__(self, marker, board, length, firstMove):
		Ai2. __init__(self, marker, board, length, firstMove)
		self.ramdomMoveList = [0, 1, 2, 3, 4, 5, 6, 7]
	def get_best_move(self, board, length):
		row = random.choice(self.ramdomMoveList)
		col = random.choice(self.ramdomMoveList)
		while (board[row][col]!= NONE):
			row = random.choice(self.ramdomMoveList)
			col = random.choice(self.ramdomMoveList)
		self.bestMoveX = col
		self.bestMoveY = row

class MidAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def get_best_move(self, board, length):
		move = legalMovesList.legalMovesAvailable / 2
		legalMovesList.takeTileByIndex(move, self.marker)
		self.bestMoveX = legalMovesList.prevX
		self.bestMoveY = legalMovesList.prevY
