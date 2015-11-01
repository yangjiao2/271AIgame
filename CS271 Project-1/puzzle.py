import sys
from PyQt4 import QtGui, QtCore
from numpy import *
from math import *
import random,time
import Queue

left = [1,1,1,1,1,1,1,3,2,2,2,2,2,2,2,2,2,2,1,1]
right= [3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,2,3,3]
def LC():
	a=left[19]
	del left[19]
	left.insert(0,a)
	right[17]=left[13]
	right[3]=left[7]
def LCC():
	a=left[0]
	del left[0]
	left.insert(19,a)
	right[17]=left[13]
	right[3]=left[7]
def RC():
	a=right[19]
	del right[19]
	right.insert(0,a)
	left[13]=right[17]
	left[7]=right[3]
def RCC():		
	a=right[0]
	del right[0]
	right.insert(19,a)
	left[7]=right[3]
	left[13]=right[17]
def rotate(x):
	if x == 1:
		LC()
	elif x == 2:
		LCC()
	elif x == 3:
		RC()
	elif x == 4:
		RCC()
def solverotate(x,item):
	templeft=item[1][:]
	tempright=item[2][:]
	if x ==1:
		a=templeft[19]
		del templeft[19]
		templeft.insert(0,a)
		tempright[17]=templeft[13]
		tempright[3]=templeft[7]
	elif x == 2:
		a=templeft[0]
		del templeft[0]
		templeft.insert(19,a)
		tempright[17]=templeft[13]
		tempright[3]=templeft[7]
	elif x == 3:
		a=tempright[19]
		del tempright[19]
		tempright.insert(0,a)
		templeft[13]= tempright[17]
		templeft[7] = tempright[3]
	elif x == 4:
		a=tempright[0]
		del tempright[0]
		tempright.insert(19,a)
		templeft[7]=tempright[3]
		templeft[13]=tempright[17]
	item[1]=templeft[:]
	item[2]=tempright[:]
	return item
def initialize():
	left[:]=[]
	right[:]= []
	newleft = [1,1,1,1,1,1,1,3,2,2,2,2,2,2,2,2,2,2,1,1]
	newright= [3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,2,3,3]
	left.extend(newleft)
	right.extend(newright)
def heuristic(item):
	heulist = [0,0,0,0,0,0,0,0]							
	for j in range(1,3):
		for i in range(0,20):
			heulist[item[j][i]-1+(j-1)*4] += 1
	return min((heulist[0]+heulist[6]),(heulist[2]+heulist[4]))+min((heulist[1]+heulist[7]),(heulist[3]+heulist[5]))
	#heulist = leftring[9B-1,10B-1,9B-2,10B-2],rightring[9B-1,10B-1,9B-2,10B-2]
def printresult(item):
	if not item[3] == 0:
		printresult(item[3])
	print(item[1])
	print(item[2])
	print(item[4])
def checkgoal(item):
	for j in range(1,3):
		counter=0
		flag = item[j][19]
		for i in range(20):
			if not item[j][i] == flag:
				counter+=1
				flag = item[j][i]
		if not counter == 3:
			return False
	return True
	#check if it is goal state
def solve():												
	BFS = Queue.PriorityQueue()
	item = [0,left,right,0,0,0]
	item[5] = heuristic(item)
	item[0] = 2*item[4]+item[5]
	BFS.put(item)
	while(not BFS.empty()):
		root = BFS.get()[:]
		if checkgoal(root):
			printresult(root)
			return
		for i in range(1,5):
			temp = root[:]
			temp[3] = root
			temp[4] +=1
			solverotate(i,temp)
			if (not temp[1] == root[1]) or (not temp[2] == root[2]): 
				temp[5] = heuristic(temp)
				temp[0] = 2*temp[4]+temp[5]
				BFS.put(temp)
def solve1():													
	BFS = Queue.PriorityQueue()
	frontier = Queue.PriorityQueue()							
	item = [0,left,right,0,0,0]
	item[5] = heuristic(item)
	item[0] = 2*item[4]+item[5]
	f_limit = item[0]
	f_next = 1000
	counter = 0
	flag =1
	BFS.put(item)
	while(1):
		if flag ==1:
			while(not BFS.empty()):
				counter+=1
				root = BFS.get()[:]
				for i in range(1,5):
					temp = root[:]
					temp[4] += 1
					if temp[3]+i==3 or temp[3]+i==7:
						continue
					solverotate(i,temp)
					temp[3]=i
					temp[5]=heuristic(item)
					temp[0]= temp[4]+temp[5]
					if checkgoal(root):
						print(counter)
						return
					if temp[0] <= f_limit:
						BFS.put(temp)
					else:
						f_next = min(f_next,temp[0])
						frontier.put(temp)
			f_limit = f_next
			f_next = 1000
			flag = 0
		else:
			while(not frontier.empty()):
				counter+=1
				root = frontier.get()[:]
				for i in range(1,5):
					temp = root[:]
					temp[4] += 1
					if temp[3]+i==3 or temp[3]+i==7:
						continue
					solverotate(i,temp)
					temp[3]=i
					temp[5]=heuristic(item)
					temp[0]= temp[4]+temp[5]
					if checkgoal(root):
						print(counter)
						return
					if temp[0] <= f_limit:
						frontier.put(temp)
					else:
						f_next = min(f_next,temp[0])
						BFS.put(temp)
			f_limit = f_next
			f_next = 1000
			flag =1
		#IDA* use two array to save the frontier when search on the other array
def randomizer(n):
	counter=0
	flag=0
	for i in range(0,n):
		move = random.randint(1,4)	
		if move == flag:
			counter=counter+1
		elif move+flag==3 or move+flag==7:
			move= 5-move
			counter=0
		else:
			counter=0
		if counter == 20:
			rotate(5-move)
			counter=0
			flag=5-move
		else:
			rotate(move)
			flag=move
def resetpuzzle():
	for i in range(5,26):
		print("round")
		for j in range(0,5):
			initialize()
			randomizer(i)
			solve1()
class Puzzle(QtGui.QWidget):
    def __init__(self):
        super(Puzzle, self).__init__()
        self.initUI()
    def initUI(self):
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('Puzzle')
		gridlayout = QtGui.QGridLayout()
		self.textedit = QtGui.QLineEdit()
		gridlayout.addWidget(self.textedit,60,120,10,10)
		button1 = QtGui.QPushButton( "1",self)
		gridlayout.addWidget(button1,60,0,10,10)
		button2 = QtGui.QPushButton("2",self)
		gridlayout.addWidget(button2,60,20,10,10)
		button3 = QtGui.QPushButton( "3",self)
		gridlayout.addWidget(button3,60,40,10,10)
		button4 = QtGui.QPushButton("4",self)
		gridlayout.addWidget(button4,60,60,10,10)
		button5 = QtGui.QPushButton("Reset",self)
		gridlayout.addWidget(button5,60,80,10,10)
		button6 = QtGui.QPushButton("solve",self)
		gridlayout.addWidget(button6,60,100,10,10)
		self.setLayout(gridlayout)
		button1.clicked.connect(LC)
		button1.clicked.connect(self.update)
		button2.clicked.connect(LCC)
		button2.clicked.connect(self.update)
		button3.clicked.connect(RC)
		button3.clicked.connect(self.update)
		button4.clicked.connect(RCC)
		button4.clicked.connect(self.update)
		button5.clicked.connect(initialize)
		button5.clicked.connect(self.update)
		button5.clicked.connect(resetpuzzle)
		button6.clicked.connect(solve1)
		button6.clicked.connect(self.update)
		self.show()	
    def paintEvent(self,event=None):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
    def drawBrushes(self, qp):
		color = QtGui.QColor(0,0,0)
		color.setNamedColor('#d4d4d4')
		qp.setPen(color)
		for i in range(0,20):
			if left[i] == 1:
				qp.setBrush(QtGui.QColor(255,0,0))
			elif left[i] == 2:
				qp.setBrush(QtGui.QColor(0,255,0))
			elif left[i] == 3:
				qp.setBrush(QtGui.QColor(0,0,255))
			elif left[i] == 4:
				qp.setBrush(QtGui.QColor(0,0,0))
			qp.drawEllipse(100-60*math.cos(math.radians(i*18)),130+60*math.sin(math.radians(i*18)),10,10)	
		for i in range(0,20):
			if right[i] == 1:
				qp.setBrush(QtGui.QColor(255,0,0))
			elif right[i] == 2:
				qp.setBrush(QtGui.QColor(0,255,0))
			elif right[i] == 3:
				qp.setBrush(QtGui.QColor(0,0,255))
			elif right[i] == 4:
				qp.setBrush(QtGui.QColor(0,0,0))
			qp.drawEllipse(170-60*math.cos(math.radians(i*18)),130+60*math.sin(math.radians(i*18)),10,10)
def main():
    app = QtGui.QApplication(sys.argv)
    puzzle = Puzzle()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()