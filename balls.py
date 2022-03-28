import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPixmap, QImage
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
import gameFunction


class RunBalls(QtCore.QObject):
    def __init__(self, parent):
        QtCore.QObject.__init__(self)
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
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()-10, 80, 60))
                if ball.y() < 11:
                    if (self._isUpBall==True):
                        self.removeUpBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "2":
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()+10, 80, 60))
                if ball.y() > 699:
                    if (self._isDownBall==True):
                        self.removeDownBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "3":
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()-10, 80, 60))
                if ball.y() < 11:
                    if (self._isUpBall==True):
                        self.removeUpBall()
                    ball.deleteLater()
                    removeList.append(ball)

            if ball.toolTip() == "4":
                ball.setGeometry(QtCore.QRect(ball.x(), ball.y()-10, 80, 60))
                if ball.y() < 11:
                    if (self._isUpBall==True):
                        self.removeUpBall()
                    ball.deleteLater()
                    removeList.append(ball)

        for ball in removeList:
            self.ballList.remove(ball)


    def createball(self):
        x = 491
        y = 10
        if self._isUpBall:
            return
        ball = QtWidgets.QLabel(self._parent)
        ball.setGeometry(QtCore.QRect(x, y, 80, 60))
        ball.setPixmap(QtGui.QPixmap("redBall.png"))
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
        self._upTimer.stop()

    def createball2(self):
        x = 491
        y = 699
        if self._isDownBall:
            return
        ball2 = QtWidgets.QLabel(self._parent)
        ball2.setGeometry(QtCore.QRect(x, y, 80, 60))
        ball2.setPixmap(QtGui.QPixmap("blueBall.png"))
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
        self._upTimer2.stop()

    def createball3(self):
        x = 565
        y = 360
        if self._isDownBall:
            return
        ball = QtWidgets.QLabel(self._parent)
        ball.setGeometry(QtCore.QRect(x, y, 80, 60))
        ball.setPixmap(QtGui.QPixmap("whiteBall.png"))
        ball.setScaledContents(True)
        ball.setToolTip("3")
        ball.show()
        self._LeftBall3 = ball
        self._isLeftBall3 = True
        self._upTimer3 = QtCore.QTimer(self)
        self._upTimer3.timeout.connect(self.removeUpBall)
        self._upTimer3.start(2000)

    def removeLeftDownBall(self):
        self._downBall.deleteLater()
        self._isDownBall = False
        self._upTimer3.stop()

    def createball4(self):
        x = 420
        y = 360
        self.ball4 = QtWidgets.QLabel(self)
        self.ball4.setGeometry(QtCore.QRect(x, y, 80, 60))
        self.ball4.setPixmap(QtGui.QPixmap("yellowBall.png"))
        self.ball4.setScaledContents(True)
        self.ball4.show()

    def removeRightBall(self):
        self._downBall.deleteLater()
        self._isDownBall = False
        self._upTimer2.stop()

    def fire (self, zabaLook):
        if zabaLook == 1:
            #x = 492
            #y = 11
            x = 492
            y = 315
            ball = QtWidgets.QLabel(self._parent)
            ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            ball.setPixmap(QtGui.QPixmap("redBall.png"))
            ball.setScaledContents(True)
            ball.setToolTip("1")
            ball.show()
            self.ballList.append(ball)
            #self.ball.deleteLater()

        elif zabaLook == 2:
            #x = 493
            #y = 699
            x = 492
            y = 380
            ball = QtWidgets.QLabel(self._parent)
            ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            ball.setPixmap(QtGui.QPixmap("yellowBall.png"))
            ball.setScaledContents(True)
            ball.setToolTip("2")
            ball.show()
            self.ballList.append(ball)
            #self.ball.deleteLater()

        elif zabaLook == 3:
            x = 974
            y = 355
            self.ball = QtWidgets.QLabel(self)
            self.ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            self.ball.setPixmap(QtGui.QPixmap("blueBall.png"))
            self.ball.setScaledContents(True)
            self.ball.show()
            self.ball.deleteLater()

        elif zabaLook == 4:
            x = 10
            y = 355
            self.ball = QtWidgets.QLabel(self)
            self.ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            self.ball.setPixmap(QtGui.QPixmap("whiteBall.png"))
            self.ball.setScaledContents(True)
            self.ball.show()

            self.ball.deleteLater()