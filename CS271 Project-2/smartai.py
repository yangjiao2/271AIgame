#import cost
from cost import costfunction
from main import NONE, PLAYER1, PLAYER2



#Make  a super class called AI? for inheritance?
class Ai2():
	
	#=======================================================================
	#				Initialization
	#=======================================================================
	def __init__(self, board, turn):
		self.turn = turn
		self.board = board
		self.bestMoveX = -1
		self.bestMoveY = -1
		
	def get_best_move(self):
		self.bestMoveX = 0
		self.bestMoveY = 0
		
	def make_move(self):
		self.get_best_move()
		return (self.bestMoveX, self.bestMoveY)
		
class BasicAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def __init__(self, board, turn):
		Ai2.__init(turn)
		
	def get_best_move(self):
		cost = costfunction(self.board, self.turn)
		cost.findBestMove()
		self.bestMoveX = cost.bestX
		self.bestMoveY = cost.bestY
		cost.close()

class AdvAi(Ai2):
	#=======================================================================
	#				Functions
	#=======================================================================
	def __init__(self, board, turn):
		Ai2.__init(board, turn)
		
	def get_best_move(self):
		pass
