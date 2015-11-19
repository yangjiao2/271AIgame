import sys
from PyQt4 import QtGui, QtCore
#from numpy import *
from math import *
import random,time
import Queue
import ConnectFourGame
NONE = '.'
PLAYER1 = 'x'
PLAYER2 = 'o'
LENGTH = 8
VSMode = 1

# pvp, cvp, turn, (row, column)
class Modeselect(QtGui.QWidget):
	def __init__(self):
		super(Modeselect, self).__init__()
		self.VSMode = -1
		self.initUI()
	def initUI(self):
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('ModesSelection')
		gridlayout = QtGui.QGridLayout()
		button1 = QtGui.QPushButton( "Player V.S. Player",self)
		gridlayout.addWidget(button1,60,0,10,10)
		button2 = QtGui.QPushButton("Player V.S. Computer",self)
		gridlayout.addWidget(button2,60,20,10,10)
		button3 = QtGui.QPushButton( "Computer V.S. Computer",self)
		gridlayout.addWidget(button3,60,40,10,10)
		button4 = QtGui.QPushButton("quit",self)
		gridlayout.addWidget(button4,60,60,10,10)
		self.setLayout(gridlayout)
		button1.clicked.connect(self.mode1)
		button2.clicked.connect(self.mode2)
		button3.clicked.connect(self.mode3)
		button4.clicked.connect(self.close)
		self.show()
	def mode1(self):
		VSMode = 1
		self.puzzle = Puzzle(LENGTH)
		#self.close()
	def mode2(self):
		VSMode = 2
		self.puzzle = Puzzle(LENGTH)
		#self.close()
	def mode3(self):
		VSMode = 3
		self.puzzle = Puzzle(LENGTH)
		#self.close()

class Puzzle(QtGui.QWidget):
	def __init__(self,length):
		super(Puzzle, self).__init__()
		self.chessboard = ConnectFourGame.ConnectFourGame(length,length)
		self.VSMode = VSMode
		self.initUI()
	def initUI(self):
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('Puzzle')
		gridlayout = QtGui.QGridLayout()
		self.row = QtGui.QLineEdit()
		self.column = QtGui.QLineEdit()
		gridlayout.addWidget(self.row,60,120,10,10)
		gridlayout.addWidget(self.column,60,100,10,10)
		button1 = QtGui.QPushButton( "move",self)
		gridlayout.addWidget(button1,60,0,10,10)
		button2 = QtGui.QPushButton("2",self)
		gridlayout.addWidget(button2,60,20,10,10)
		button3 = QtGui.QPushButton( "3",self)
		gridlayout.addWidget(button3,60,40,10,10)
		button4 = QtGui.QPushButton("4",self)
		gridlayout.addWidget(button4,60,60,10,10)
		button5 = QtGui.QPushButton("quit",self)
		gridlayout.addWidget(button5,60,80,10,10)
		self.setLayout(gridlayout)
		button1.clicked.connect(self.turn)
		button1.clicked.connect(self.update)
		button2.clicked.connect(self.chessboard.print_board)
		button2.clicked.connect(self.update)
		button3.clicked.connect(self.chessboard.print_board)
		button3.clicked.connect(self.update)
		button4.clicked.connect(self.chessboard.print_board)
		button4.clicked.connect(self.update)
		button5.clicked.connect(self.close)
		self.show()	
	def paintEvent(self,event=None):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()
	def drawRectangles(self, qp):
		color = QtGui.QColor(0,0,0)
		color.setNamedColor('#d4d4d4')
		qp.setPen(color)
		for i in range(0,8):
			for j in range(0,8):
				if self.chessboard.board[j][i] == NONE:
					qp.setBrush(QtGui.QColor(255,0,0))
				elif self.chessboard.board[j][i] == PLAYER1:
					qp.setBrush(QtGui.QColor(0,255,0))
				elif self.chessboard.board[j][i] == PLAYER2:
					qp.setBrush(QtGui.QColor(0,0,255))
				qp.drawRect(10+20*j,10+i*20,20,20)
	def turn(self,qp):
		row = int(self.row.text())
		column = int(self.column.text())
		if self.chessboard.check_within_boundary(column, row):
			self.chessboard.drop_piece(row-1,column-1)
		else:
			print "out of boundary"
		if self.chessboard.check_winner_exist():
			print "winner"
		
def main():
	app = QtGui.QApplication(sys.argv)
	mode = Modeselect()
	#puzzle = Puzzle(LENGTH)
	sys.exit(app.exec_())
if __name__ == "__main__":
	main()
