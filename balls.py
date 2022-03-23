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


class runBalls():
    def createball(self):
        x = 491
        y = 295
        self.ball = QtWidgets.QLabel(self)
        self.ball.setGeometry(QtCore.QRect(x, y, 80, 60))
        self.ball.setPixmap(QtGui.QPixmap("redBall.png"))
        self.ball.setScaledContents(True)
        self.ball.show()


    def createball2(self):
        x = 491
        y = 425
        self.ball2 = QtWidgets.QLabel(self)
        self.ball2.setGeometry(QtCore.QRect(x, y, 80, 60))
        self.ball2.setPixmap(QtGui.QPixmap("blueBall.png"))
        self.ball2.setScaledContents(True)
        self.ball2.show()

    def createball3(self):
        x = 565
        y = 360
        self.ball3 = QtWidgets.QLabel(self)
        self.ball3.setGeometry(QtCore.QRect(x, y, 80, 60))
        self.ball3.setPixmap(QtGui.QPixmap("whiteBall.png"))
        self.ball3.setScaledContents(True)
        self.ball3.show()

    def createball4(self):
        x = 420
        y = 360
        self.ball4 = QtWidgets.QLabel(self)
        self.ball4.setGeometry(QtCore.QRect(x, y, 80, 60))
        self.ball4.setPixmap(QtGui.QPixmap("yellowBall.png"))
        self.ball4.setScaledContents(True)
        self.ball4.show()


    def fire (self, zabaLook):
        if zabaLook == 1:
            x = 492
            y = 11
            self.ball = QtWidgets.QLabel(self)
            self.ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            self.ball.setPixmap(QtGui.QPixmap("redBall.png"))
            self.ball.setScaledContents(True)
            self.ball.show()
            self.ball.deleteLater()

        elif zabaLook == 2:
            x = 493
            y = 699
            self.ball = QtWidgets.QLabel(self)
            self.ball.setGeometry(QtCore.QRect(x, y, 80, 60))
            self.ball.setPixmap(QtGui.QPixmap("yellowBall.png"))
            self.ball.setScaledContents(True)
            self.ball.show()
            self.ball.deleteLater()

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