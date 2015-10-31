from DumbAiModule import MidAi
from DumbAiModule import RandomAi
from SmartAiModule import BasicAi
import GameBoard
import DumbAiModule
import SmartAiModule

#=======================================================================
#				MAIN
#=======================================================================
#Debugging method to print stuff
if False:
	for i in range(0, boardLength):
		for j in range(0, boardLength):
			takeTile(i, j, 1)
			#printMatrix(freeTiles)
			if isGameOver == True:
					break

		if isGameOver == True:
			break

#End Debug! Here is the game!
a = MidAi(1)
b = BasicAi(2)

while(GameBoard.isGameOver == False):
	a.takeDumbMove()
	print "Player 1: Takes Turn: [%d, %d]" % (a.bestMoveX, a.bestMoveY)
	GameBoard.printMatrix(GameBoard.freeTiles)
	if (GameBoard.isGameOver == True):
		break
		
	b.takeDumbMove()
	print "Player 2: Takes Turn: [%d, %d]" % (b.bestMoveX, b.bestMoveY)
	GameBoard.printMatrix(GameBoard.freeTiles)
	
#endWhile
