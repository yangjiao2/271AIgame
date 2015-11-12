import sys
from PyQt4 import QtGui, QtCore
from numpy import *
from math import *
import random,time
import Queue
import ConnectFourGame

# pvp, cvp, turn, (row, column)

class Puzzle(QtGui.QWidget):
	def __init__(self,length):
		super(Puzzle, self).__init__()
		self.chessboard = ConnectFourGame.ConnectFourGame(length,length)
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
		button5 = QtGui.QPushButton("Reset",self)
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
		button5.clicked.connect(self.chessboard.print_board)
		button5.clicked.connect(self.update)
		button5.clicked.connect(self.chessboard.print_board)
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
				if self.chessboard.board[j][i] == '.':
					qp.setBrush(QtGui.QColor(255,0,0))
				elif self.chessboard.board[j][i] == 'x':
					qp.setBrush(QtGui.QColor(0,255,0))
				elif self.chessboard.board[j][i] == 'o':
					qp.setBrush(QtGui.QColor(0,0,255))
				qp.drawRect(10+20*j,10+i*20,20,20)
	def turn(self,qp):
		row = int(self.row.text())
		column = int(self.column.text())
		self.chessboard.drop_piece(row-1,colum-1)
def main():
	app = QtGui.QApplication(sys.argv)
	puzzle = Puzzle()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()