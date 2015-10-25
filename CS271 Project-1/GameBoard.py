
#Static variables
boardLength = 8
isGameOver = False
movesLeft = boardLength * boardLength

#=======================================================================
#64 tiles

freeTiles = [[0] * boardLength for i in range(boardLength)]


#=======================================================================
#				Functions
#=======================================================================

def isTileFree(x, y):
	if freeTiles[x][y] == 0:
		return True
	else:
		return False

#TODO game should be over when someone wins!		
		
def takeTile(x, y, player):
	global legalMovesAvailable
	global movesLeft
	global isGameOver

	if isTileFree(x, y) == True:
		freeTiles[x][y] = player

	else:
		print "Tile [%d,%d] is not free!" % (x, y)
		isGameOver = True
		
	movesLeft = movesLeft - 1
	if movesLeft == 0:
		isGameOver = True

def printMatrix(matrix):
	print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in matrix]))
	print ('\n')



