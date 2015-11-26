# from SmartAiModule import BasicAi
# import GameBoard
# import SmartAiModule

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
	cfg = ConnectFourGame.ConnectFourGame(8,8) # 8 * 8 
	cfg.print_board()
	while(not cfg.check_winner_exist()):
		# TODO: 
		# determine move, check if the tile is free, make move
		# below is a sample code, does only drop and print
	
		cfg.ask_ai_drop_piece()
		cfg.print_board()
	
		
