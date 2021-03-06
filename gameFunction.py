from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon, QPixmap
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint, QEvent
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
import ui_untitled
from balls import RunBalls
from qball import QBall

class gameSettings(QtWidgets.QMainWindow, ui_untitled.Ui_MainWindow):
    pole = 1
    zabaLook = 1
    fireBall = False
    x = 492
    y = 315
    minusTime = 50
    timer = 0

    #Тут обработка событий
    def __init__(self):
        super().__init__()
        self.setupUi(self)# Её не убирать !!!
        self._runBalls = RunBalls(self)
    # Тут создание лэйбла пример
        self.GameTimer = QtCore.QTimer(self)
        self.GameTimer.timeout.connect(self.time)

        self.fireBallTimer = QtCore.QTimer(self)
        self.fireBallTimer.timeout.connect(self.spawnBall)
        self.fireBallTimer.start(2000)

        self.startMenu()
        self.startGame.clicked.connect(lambda: self.hideAll())
        self.settingsButton.clicked.connect(lambda: self.settings())
        self.gameZon1.clicked.connect(lambda: self.firstGameZone())
        self.gameZon2.clicked.connect(lambda: self.secondGameZone())
        self.gameZon3.clicked.connect(lambda: self.thirdGameZone())
        self.mainMenu.clicked.connect(lambda: self.menu())
        self.exitGame.clicked.connect(lambda: self.exit())
        #self.exitGame.clicked.connect(MainWindow.) Тут надо написать выход из программы


    def time (self):
        gameSettings.minusTime -=1
        if (gameSettings.minusTime == 0):
            self.menu()
            self.welcome.setText('ВЫ ПРОИГРАЛИ!')
        self.timeGame.setText(f'Осталось времени: {gameSettings.minusTime}')

    #Стартовое меню
    def startMenu(self):
        self.mainMenu.hide()
        self.itsGame.hide()
        self.zaba.hide()
        self.changeMenu.hide()
        self.gameZon1.hide()
        self.gameZon2.hide()
        self.gameZon3.hide()
        self.timeGame.hide()
        gameSettings.timer = 0
        gameSettings.minusTime = 50
        self.timeGame.hide()


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
        self.fireBallFunction()
        self.GameTimer.start(1000)
        self.timeGame.show()
        self.ball.show()
        self.fireBallTimer.start(2000)

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
        self.GameTimer.stop()
        self.timeGame.hide()
        self.fireBallTimer.stop()
        gameSettings.minusTime = 50
        self.ball.hide()
        self.welcome.setText("<html><head/><body><p><span style=\" font-size:18pt;\">Добро пожаловать в мою игру</span></p></body></html>")



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W:
            self.zaba.setPixmap(QPixmap("zabaMid.png"))
            self.zabaLook = 1
            self.fireBallFunction()
            self.ballZabaMove()

        elif e.key() == Qt.Key_A:
            self.zaba.setPixmap(QPixmap("zabaLeft.png"))
            self.zabaLook = 4
            self.fireBallFunction()
            self.ballZabaMove()

        elif e.key() == Qt.Key_S:
            self.zaba.setPixmap(QPixmap("zabaBackside.png"))
            self.zabaLook = 2
            self.fireBallFunction()
            self.ballZabaMove()

        elif e.key() == Qt.Key_D:
            self.zaba.setPixmap(QPixmap("zabaRight.png"))
            self.zabaLook = 3
            self.fireBallFunction()
            self.ballZabaMove()

        elif e.key() == Qt.Key_E:
            self._runBalls.fire(self.zabaLook, self.ball)# Тут создаю шарик
            self.fireBall = False
            self.fireBallFunction()

    def spawnBall(self):
        self.random()
        self.random()
        self.random()
        self.random()

    def random(self):
        random_number = randint(1, 4)

        if random_number == 1:
            self._runBalls.createball()

        elif random_number == 2:
            self._runBalls.createball2()

        elif random_number == 3:
            self._runBalls.createball3()

        elif random_number == 4:
            self._runBalls.createball4()

    def fireBallFunction(self):
        if self.zabaLook == 1:
            self.x = 492
            self.y = 315

        elif self.zabaLook == 2:
            self.x = 492
            self.y = 405

        elif self.zabaLook == 3:
            self.x = 540
            self.y = 355

        elif self.zabaLook == 4:
            self.x = 445
            self.y = 355

        if self.fireBall == False:
            random_color = randint(1, 4)

            self.ball = QBall(self)
            self.ball.setGeometry(QtCore.QRect(self.x, self.y, 80, 60))
            if random_color == 3:
                self.ball.setPixmap(QtGui.QPixmap("blueBall.png"))
                self.ball.setScaledContents(True)
                self.ball.setBallColor('blue')
                self.ball.setToolTip("3")

            if random_color == 2:
                self.ball.setPixmap(QtGui.QPixmap("yellowBall.png"))
                self.ball.setScaledContents(True)
                self.ball.setBallColor('yellow')
                self.ball.setToolTip("2")

            if random_color == 1:
                self.ball.setPixmap(QtGui.QPixmap("redBall.png"))
                self.ball.setScaledContents(True)
                self.ball.setBallColor('red')
                self.ball.setToolTip("1")

            if random_color == 4:
                self.ball.setPixmap(QtGui.QPixmap("whiteBall.png"))
                self.ball.setScaledContents(True)
                self.ball.setBallColor('white')
                self.ball.setToolTip("4")

            self.ball.show()
            self.fireBall = True


    def ballZabaMove(self):
        if self.fireBall == True:
            self.ball.setGeometry(QtCore.QRect(self.x, self.y, 80, 60))
            #self._runBalls.fire(self.zabaLook, ball)