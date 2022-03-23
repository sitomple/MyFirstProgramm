from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPixmap
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_untitled
import balls

class gameSettings(QtWidgets.QMainWindow, ui_untitled.Ui_MainWindow, balls.runBalls):
    pole = 1
    zabaLook = 1

    #Тут обработка событий
    def __init__(self):
        super().__init__()
        self.setupUi(self)# Её не убирать !!!

    # Тут создание лэйбла пример
        '''self.my_text = QtWidgets.QLabel('Привет codeby!')
        self.my_text.setAlignment(QtCore.Qt.AlignCenter)
        self.my_text.show()'''
        #self.label = QtWidgets.QLabel( self)
        #self.label.setPixmap(QtGui.QPixmap("игровое поле1.jpg"))

        self.startMenu()
        self.startGame.clicked.connect(lambda: self.hideAll())
        self.settingsButton.clicked.connect(lambda: self.settings())
        self.gameZon1.clicked.connect(lambda: self.firstGameZone())
        self.gameZon2.clicked.connect(lambda: self.secondGameZone())
        self.gameZon3.clicked.connect(lambda: self.thirdGameZone())
        self.mainMenu.clicked.connect(lambda: self.menu())
        self.exitGame.clicked.connect(lambda: self.exit())
        #self.exitGame.clicked.connect(MainWindow.) Тут надо написать выход из программы

    #Стартовое меню
    def startMenu(self):
        self.mainMenu.hide()
        self.itsGame.hide()
        self.zaba.hide()
        self.changeMenu.hide()
        self.gameZon1.hide()
        self.gameZon2.hide()
        self.gameZon3.hide()

    #Тут выход из игры
    def exit (self):
        QMainWindow.close(self)

    #Тут настройки для игры
    def settings(self):
        self.changeMenu.show()
        self.gameZon1.show()
        self.gameZon2.show()
        self.gameZon3.show()
        self.mainMenu.show()
        self.exitGame.hide()
        self.startGame.hide()
        self.settingsButton.hide()
        self.welcome.hide()

    #Тут игровые поля
    def firstGameZone(self):
        self.pole = 1
    def secondGameZone(self):
        self.pole = 2
    def thirdGameZone(self):
        self.pole = 3

    #Тут игровое поле
    def gameZuma(self):
        if self.pole == 1:
            self.itsGame.setPixmap(QtGui.QPixmap("игровое поле1.jpg"))
            self.itsGame.show()
        if self.pole == 2:
            self.itsGame.setPixmap(QtGui.QPixmap("игровое поле2.jpg"))
            self.itsGame.show()
        if self.pole == 3:
            self.itsGame.setPixmap(QtGui.QPixmap("игровое поле3.jpg"))
            self.itsGame.show()
        self.mainMenu.show()
        self.zaba.show()

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
        self.zaba.hide()
        self.gameZon1.hide()
        self.gameZon2.hide()
        self.gameZon3.hide()
        self.changeMenu.hide()

        #Тут убираю мячика когда сделаю их удаление их надо будет удалить
        #self.ball.hide() Эту скорее всего надо оставить

        #self.ball2.hide()
        #self.ball3.hide()
        #self.ball4.hide()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W:
            self.zaba.setPixmap(QPixmap("zabaMid.png"))
            self.zabaLook = 1
            #balls.runBalls.createball(self)#Тут создаю шарик

        elif e.key() == Qt.Key_S:
            self.zaba.setPixmap(QPixmap("zabaBackside.png"))
            self.zabaLook = 2
            #balls.runBalls.createball2(self)  # Тут создаю шарик

        elif e.key() == Qt.Key_D:
            self.zaba.setPixmap(QPixmap("zabaRight.png"))
            self.zabaLook = 3
            #balls.runBalls.createball3(self)  # Тут создаю шарик

        elif e.key() == Qt.Key_A:
            self.zaba.setPixmap(QPixmap("zabaLeft.png"))
            self.zabaLook = 4
            #balls.runBalls.createball4(self)  # Тут создаю шарик

        elif e.key() == Qt.Key_E:
            balls.runBalls.fire(self, self.zabaLook)  # Тут создаю шарик