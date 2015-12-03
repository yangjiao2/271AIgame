from SmartAiModule import BasicAi
import ConnectFourGame
import SmartAiModule

# #=======================================================================
# #				MAIN
# #=======================================================================
# #Debugging method to print stuff
# if False:
# 	for i in range(0, boardLength):
# 		for j in range(0, boardLength):
# 			takeTile(i, j, 1)
# 			#printMatrix(freeTiles)
# 			if isGameOver == True:
# 					break

# 		if isGameOver == True:
# 			break

# #End Debug! Here is the game!
# a = BasicAi(1)
# b = BasicAi(2)

# while(GameBoard.isGameOver == False):
# 	a.takeDumbMove()
# 	print "Player 1: Takes Turn: [%d, %d]" % (a.bestMoveX, a.bestMoveY)
# 	GameBoard.printMatrix(GameBoard.freeTiles)
# 	if (GameBoard.isGameOver == True):
# 		break
		
# 	b.takeDumbMove()
# 	print "Player 2: Takes Turn: [%d, %d]" % (b.bestMoveX, b.bestMoveY)
# 	GameBoard.printMatrix(GameBoard.freeTiles)
	
#endWhile




if __name__ == "__main__":
        # test for computer vs. comptuter
        # for human vs. computer, human drop their pieces first
        # can change Ai in ConnectFourGame __init__
        mode = 3
        cfg = ConnectFourGame.ConnectFourGame(8,8,mode) # 8 * 8
        cfg.print_board()
        print "-------------------"
        while(not cfg.check_winner_exist()):
                cfg.drop_piece(-1, -1)
                cfg.print_board()
        print "-------------------"

