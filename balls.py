import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPixmap, QImage
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from qball import QBall
import gameFunction


class RunBalls(QtCore.QObject):
    def __init__(self, parent):
        QtCore.QObject.__init__(self)
        self.zabaLook2 = 1
        self._parent = parent
        self._isUpBall = False
        self._isDownBall = False
        self._isLeftBall = False
        self._isRightBall = False
        self.ballList = []
        self.tm = QtCore.QTimer(self)
        self.tm.timeout.connect(self.moveBalls)
        self.tm.start(100)

    def moveBalls(self):
        removeList = []
        for ball in self.ballList:

            if ball.toolTip() == "1":
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()-40, 80, 60))
                if ball.y() < 11:
                    if (self._isUpBall == True):
                        if (ball.ballColor() == self._upBall.ballColor()):
                            self.removeUpBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "2":
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()+40, 80, 60))
                if ball.y() > 699:
                    if (self._isDownBall == True):
                        if (ball.pixmap() == self._downBall.pixmap()):
                            self.removeDownBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "3":
                ball.setGeometry(QtCore.QRect(ball.x()+40, ball.y(), 80, 60))
                if ball.x() > 974:
                    if (self._isRightBall == True):
                        if (ball.pixmap() == self._rightBall.pixmap()):
                            self.removeRightBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "4":
                ball.setGeometry(QtCore.QRect(ball.x()-40, ball.y(), 80, 60))
                if ball.x() < 10:
                    if (self._isLeftBall == True):
                        if (ball.pixmap() == self._leftBall.pixmap()):
                            self.removeLeftBall()
                    ball.deleteLater()
                    removeList.append(ball)

        for ball in removeList:
            self.ballList.remove(ball)


    def createball(self):
        if self._isUpBall:
            return
        ball = QBall(self._parent)
        x = 491
        y = 10
        ball.setGeometry(QtCore.QRect(x, y, 80, 60))
        random_number = randint(1, 4)
        if random_number == 1:
            ball.setPixmap(QtGui.QPixmap("redBall.png"))
            ball.setBallColor('red')
        if random_number == 2:
            ball.setPixmap(QtGui.QPixmap("blueBall.png"))
            ball.setBallColor('blue')
        if random_number == 3:
            ball.setPixmap(QtGui.QPixmap("yellowBall.png"))
            ball.setBallColor('yellow')
        if random_number == 4:
            ball.setPixmap(QtGui.QPixmap("whiteBall.png"))
            ball.setBallColor('white')
        ball.setScaledContents(True)
        ball.setToolTip("1")
        ball.show()
        self._upBall = ball
        self._isUpBall = True
        self._upTimer = QtCore.QTimer(self)
        self._upTimer.timeout.connect(self.removeUpBall)
        self._upTimer.start(2000)

    def removeUpBall(self):
        self._upBall.deleteLater()
        self._isUpBall = False
        self._upTimer.deleteLater()

    def createball2(self):
        if self._isDownBall:
            return
        ball2 = QtWidgets.QLabel(self._parent)
        x = 491
        y = 699
        ball2.setGeometry(QtCore.QRect(x, y, 80, 60))
        random_number = randint(1, 4)
        if random_number == 1:
            ball2.setPixmap(QtGui.QPixmap("redBall.png"))
        if random_number == 2:
            ball2.setPixmap(QtGui.QPixmap("blueBall.png"))
        if random_number == 3:
            ball2.setPixmap(QtGui.QPixmap("yellowBall.png"))
        if random_number == 4:
            ball2.setPixmap(QtGui.QPixmap("whiteBall.png"))
        ball2.setScaledContents(True)
        ball2.setToolTip("2")
        ball2.show()
        self._downBall = ball2
        self._isDownBall = True
        self._upTimer2 = QtCore.QTimer(self)
        self._upTimer2.timeout.connect(self.removeDownBall)
        self._upTimer2.start(2000)


    def removeDownBall(self):
        self._downBall.deleteLater()
        self._isDownBall = False
        self._upTimer2.deleteLater()

    def createball3(self):
        if self._isRightBall:
            return
        ball3 = QtWidgets.QLabel(self._parent)
        x = 974
        y = 356
        ball3.setGeometry(QtCore.QRect(x, y, 80, 60))
        random_number = randint(1, 4)
        if random_number == 1:
            ball3.setPixmap(QtGui.QPixmap("redBall.png"))
        if random_number == 2:
            ball3.setPixmap(QtGui.QPixmap("blueBall.png"))
        if random_number == 3:
            ball3.setPixmap(QtGui.QPixmap("yellowBall.png"))
        if random_number == 4:
            ball3.setPixmap(QtGui.QPixmap("whiteBall.png"))
        ball3.setScaledContents(True)
        ball3.setToolTip("3")
        ball3.show()
        self._rightBall = ball3
        self._isRightBall = True
        self._rightTimer = QtCore.QTimer(self)
        self._rightTimer.timeout.connect(self.removeRightBall)
        self._rightTimer.start(2000)

    def removeRightBall(self):
        self._rightBall.deleteLater()
        self._isRightBall = False
        self._rightTimer.deleteLater()

    def createball4(self):
        if self._isLeftBall:
            return
        ball4 = QtWidgets.QLabel(self._parent)
        x = 10
        y = 356
        ball4.setGeometry(QtCore.QRect(x, y, 80, 60))
        random_number = randint(1, 4)
        if random_number == 1:
            ball4.setPixmap(QtGui.QPixmap("redBall.png"))
        if random_number == 2:
            ball4.setPixmap(QtGui.QPixmap("blueBall.png"))
        if random_number == 3:
            ball4.setPixmap(QtGui.QPixmap("yellowBall.png"))
        if random_number == 4:
            ball4.setPixmap(QtGui.QPixmap("whiteBall.png"))
        ball4.setScaledContents(True)
        ball4.setToolTip("4")
        ball4.show()
        self._leftBall = ball4
        self._isLeftBall = True
        self._leftTimer = QtCore.QTimer(self)
        self._leftTimer.timeout.connect(self.removeLeftBall)
        self._leftTimer.start(2000)

    def removeLeftBall(self):
        self._leftBall.deleteLater()
        self._isLeftBall = False
        self._leftTimer.deleteLater()

    def fire (self, zabaLook,ball):
        if zabaLook == 1:
            self.zabaLook2 = 1
            self.ballList.append(ball)
            #self.ball.deleteLater()

        elif zabaLook == 2:
            self.zabaLook2 = 2
            self.ballList.append(ball)
            #self.ball.deleteLater()

        elif zabaLook == 3:
            self.zabaLook2 = 3
            self.ballList.append(ball)


        elif zabaLook == 4:
            self.zabaLook2 = 4
            self.ballList.append(ball)

        self.ballList[len(self.ballList)-1].setToolTip(str(self.zabaLook2))
