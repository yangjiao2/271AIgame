#Keep tracks of which moves are still legal, AI and Players can search the lists
#legalMovesY and legalMovesX for easily getting a list of children nodes to init
import GameBoard


#Static variables
boardLength = GameBoard.boardLength
isPlayerError = False

#the previous move!
prevY = -1
prevX = -1

#=======================================================================
#				Initialization
#=======================================================================
#create a copy of 64 tiles
#these will be used to determine legal moves
#and will remove nodes from here as moves take place
freeTiles = [[0] * boardLength for i in range(boardLength)]

#These are for constructing the list of legal moves in the tree, do not search this!
#Search in freeTiles instead! These lists are too slow to search!
legalMovesAvailable = boardLength * boardLength
legalMovesY = []
legalMovesX = []

#Index all free tiles
for x in range(0, boardLength):
    for y in range(0, boardLength):
        freeTiles[x][y] = x * boardLength + y

def initLegalMoves():
	tempCol = [0] * boardLength
	for i in range(1, boardLength):
		tempCol[i] = i

	for i in range(0, boardLength):
		legalMovesY.extend(tempCol)

	for i in range(0, boardLength):
		tempCol = [i] * boardLength
		legalMovesX.extend(tempCol)
initLegalMoves()
#=======================================================================
#				End Initialization
#=======================================================================

#=======================================================================
#				Functions
#=======================================================================

def isTileFree(y, x):
	if freeTiles[y][x] == -1:
		return False
	else:
		return True
		
def takeTile(y, x, player):
	global legalMovesAvailable

	if isTileFree(x, y) == True:
		index = freeTiles[x][y]
		freeTiles[x][y] = -1

		#Removes a move from the list of legal moves
		legalMovesY[index] = legalMovesY[legalMovesAvailable - 1]
		legalMovesX[index] = legalMovesX[legalMovesAvailable - 1]

		freeTiles[legalMovesX[index]][legalMovesY[index]] = index
		legalMovesAvailable = legalMovesAvailable - 1
		legalMovesY[legalMovesAvailable] = -1
		legalMovesX[legalMovesAvailable] = -1

	else:
		print "LegalMoveList: Tile [%d,%d] is not free!" % (x, y)
		isPlayerError = True
		
def takeTileByIndex(move, player):
	global prevX, prevY
	prevY = legalMovesY[move]
	prevX = legalMovesX[move]
	takeTile(prevY, prevX, player)		

#=======================================================================
#				End Functions
#=======================================================================

#Debugging method to print stuff
#for i in range(0, boardLength):
#    for j in range(0, boardLength):
#        takeTile(i, j, 1)
#        if isPlayerError == True:
#                break

#    if isPlayerError == True:
#        break




#while(isPlayerError == False):
#	print legalMovesY
#	print legalMovesX

#root = Node(3, 4)
#root.description()


