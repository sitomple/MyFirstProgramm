from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPixmap
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_untitled

class gameSettings(QtWidgets.QMainWindow, ui_untitled.Ui_MainWindow):

    #Тут обработка событий
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainMenu.hide()
        self.itsGame.hide()
        self.zaba.hide()
        self.startGame.clicked.connect(lambda:self.hideAll())
        self.mainMenu.clicked.connect(lambda:self.menu())
        #self.exitGame.clicked.connect(MainWindow.) Тут надо написать выход из программы

    #Тут игровое поле
    def gameZuma(self):
        self.itsGame.show()
        self.mainMenu.show()
        self.itsGame.setStyleSheet("background-image : url(игровое поле1.jpg) center center cover no-repeat fixed;")
        self.zaba.setPixmap(QPixmap("background-image : url(Без имени-5.jpg)"))
        #self.zaba.setPixmap(QPixmap("Без имени-5.jpg"))

    # Тут я прячу все кнопки
    #Тут запуск игры(прячу кнопки и запускаю поле)
    def hideAll(self):
        self.exitGame.hide()
        self.startGame.hide()
        self.settingsButton.hide()
        self.welcome.hide()
        self.mainMenu.show()
        self.itsGame.show()
        self.zaba.show()
        self.gameZuma()

        # self.setMouseTracking(True)

        # self.ball()

    # Тут делаю все кнопки видимыми
    def menu(self):
        self.exitGame.show()
        self.startGame.show()
        self.settingsButton.show()
        self.welcome.show()
        self.itsGame.hide()
        self.mainMenu.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W:
            self.zaba.setPixmap(QPixmap("background-image : url(zabaMid.jpg)"))
        elif e.key() == Qt.Key_S:
            self.zaba.setPixmap(QPixmap("background-image : url(zabaBackside.jpg)"))
        elif e.key() == Qt.Key_D:
            self.zaba.setPixmap(QPixmap("background-image : url(zabaRight.jpg)"))
        elif e.key() == Qt.Key_A:
            self.zaba.setPixmap(QPixmap("background-image : url(zabaLeft.jpg)"))