import sys
from PyQt4 import QtGui, QtCore
#from numpy import *
from math import *
import random,time
import Queue
import ConnectFourGame
import time
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
		button4 = QtGui.QPushButton("test",self)
		gridlayout.addWidget(button4,60,60,10,10)
		button5 = QtGui.QPushButton("quit",self)
		gridlayout.addWidget(button5,60,80,10,10)
		self.setLayout(gridlayout)
		button1.clicked.connect(self.mode1)
		button2.clicked.connect(self.mode2)
		button3.clicked.connect(self.mode3)
		button4.clicked.connect(self.mode4)
		button5.clicked.connect(self.close)
		self.show()
	def mode1(self):
		VSMode = 1
		self.puzzle = Puzzle(LENGTH, 1)
		#self.close()
	def mode2(self):
		VSMode = 2
		self.puzzle = Puzzle(LENGTH, 2)
		#self.close()
	def mode3(self):
		VSMode = 3
		self.puzzle = Puzzle(LENGTH, 3)
		#self.close()
	def mode4(self):
		VSMode = 3
		self.test = Test(LENGTH,3)

class Test(QtGui.QWidget):
	def __init__(self,length,mode):
		super(Test, self).__init__()
		self.chessboard = ConnectFourGame.ConnectFourGame(length,length, mode)
		self.length = length
		self.VSMode = VSMode
		self.timeAI1 = 0
		self.timeAI2 = 0
		self.initUI()
	def initUI(self):
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('TESTMODE')
		gridlayout = QtGui.QGridLayout()
		button1 = QtGui.QPushButton( "move",self)
		gridlayout.addWidget(button1,60,0,10,10)
		button5 = QtGui.QPushButton("quit",self)
		gridlayout.addWidget(button5,60,40,10,10)
		self.setLayout(gridlayout)
		button1.clicked.connect(self.turn)
		button1.clicked.connect(self.update)
		button5.clicked.connect(self.close)
		self.show()
	def paintEvent(self,event=None):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()
	def turn(self):
		row = 1
		column = 1
		start_time = time.time()
		self.turn = self.chessboard.turn
		self.chessboard.drop_piece(row,column)
		end_time = time.time()
		print start_time
		print end_time
		print end_time-start_time
		if self.turn == PLAYER1:
			self.timeAI1 += end_time - start_time
			print "PLAYER1: " + str(self.timeAI1)
		else:
			self.timeAI2 += end_time - start_time
			print "PLAYER2: " + str(self.timeAI2)
			
	def drawRectangles(self, qp):
		color = QtGui.QColor(0,0,0)
		color.setNamedColor('#d4d4d4')
		qp.setPen(color)
		for i in range(0,self.length):
			for j in range(0,self.length):
				if self.chessboard.board[j][i] == NONE:
					qp.setBrush(QtGui.QColor(255,255,255))
					qp.drawRect(10+20*j,10+i*20,20,20)
				elif self.chessboard.board[j][i] == PLAYER1:
					qp.drawPixmap(10+20*j,10+i*20,20,20,QtGui.QPixmap("player1.png"))
				elif self.chessboard.board[j][i] == PLAYER2:
					qp.drawPixmap(10+20*j,10+i*20,20,20,QtGui.QPixmap("cross.jpg"))
				
class Puzzle(QtGui.QWidget):
	def __init__(self,length,mode):
		super(Puzzle, self).__init__()
		self.chessboard = ConnectFourGame.ConnectFourGame(length,length, mode)
		self.length = length
		self.VSMode = VSMode
		self.initUI()
		self.mode = mode
		self.winner = None
	def initUI(self):
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('ConnectFourGame')
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
		if self.winner != None:
			qp.setPen(QtGui.QColor(255,0,0))
			qp.drawText(200,100,self.text)
		qp.end()
	def drawRectangles(self, qp):
		color = QtGui.QColor(0,0,0)
		color.setNamedColor('#d4d4d4')
		qp.setPen(color)
		for i in range(0,self.length):
			for j in range(0,self.length):
				if self.chessboard.board[j][i] == NONE:
					qp.setBrush(QtGui.QColor(255,255,255))
					qp.drawRect(10+20*j,10+i*20,20,20)
				elif self.chessboard.board[j][i] == PLAYER1:
					qp.drawPixmap(10+20*j,10+i*20,20,20,QtGui.QPixmap("player1.png"))
				elif self.chessboard.board[j][i] == PLAYER2:
					qp.drawPixmap(10+20*j,10+i*20,20,20,QtGui.QPixmap("cross.jpg"))
	def turn(self,qp):
		if self.winner == None:
			if self.row.text():
				row = int(self.row.text())
			else:
				row = 0
			if self.column.text():
				column = int(self.column.text())
			else:
				column = 0
			self.chessboard.drop_piece(row-1,column-1)
		if self.chessboard.check_winner_exist():
			self.winner = self.chessboard.winning_player()
			if self.winner == PLAYER1:
				self.text = "winner is : Player1"
			else:
				self.text = "winner is : Player2"
def main():
	app = QtGui.QApplication(sys.argv)
	mode = Modeselect()
	#puzzle = Puzzle(LENGTH)
	sys.exit(app.exec_())
if __name__ == "__main__":
	main()
