# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(380, 360, 311, 31))
        self.settingsButton.setObjectName("settingsButton")
        self.startGame = QtWidgets.QPushButton(self.centralwidget)
        self.startGame.setGeometry(QtCore.QRect(380, 320, 311, 31))
        self.startGame.setObjectName("startGame")
        self.exitGame = QtWidgets.QPushButton(self.centralwidget)
        self.exitGame.setGeometry(QtCore.QRect(430, 450, 191, 61))
        self.exitGame.setObjectName("exitGame")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(370, 180, 341, 51))
        self.welcome.setObjectName("welcome")
        self.mainMenu = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenu.setGeometry(QtCore.QRect(30, 10, 181, 41))
        self.mainMenu.setObjectName("mainMenu")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 10, 361, 141))
        self.label.setObjectName("label")
        self.itsGame = QtWidgets.QLabel(self.centralwidget)
        self.itsGame.setGeometry(QtCore.QRect(10, 0, 1041, 771))
        self.itsGame.setMaximumSize(QtCore.QSize(1041, 771))
        self.itsGame.setText("")
        self.itsGame.setTextFormat(QtCore.Qt.AutoText)
        self.itsGame.setPixmap(QtGui.QPixmap("игровое поле1.jpg"))
        self.itsGame.setScaledContents(True)
        self.itsGame.setOpenExternalLinks(False)
        self.itsGame.setObjectName("itsGame")
        self.zaba = QtWidgets.QLabel(self.centralwidget)
        self.zaba.setGeometry(QtCore.QRect(290, 210, 471, 351))
        self.zaba.setText("")
        self.zaba.setPixmap(QtGui.QPixmap("zabaMid.png"))
        self.zaba.setScaledContents(True)
        self.zaba.setWordWrap(False)
        self.zaba.setOpenExternalLinks(False)
        self.zaba.setObjectName("zaba")
        self.gameZon1 = QtWidgets.QPushButton(self.centralwidget)
        self.gameZon1.setGeometry(QtCore.QRect(430, 352, 201, 31))
        self.gameZon1.setObjectName("gameZon1")
        self.gameZon2 = QtWidgets.QPushButton(self.centralwidget)
        self.gameZon2.setGeometry(QtCore.QRect(430, 390, 201, 31))
        self.gameZon2.setObjectName("gameZon2")
        self.gameZon3 = QtWidgets.QPushButton(self.centralwidget)
        self.gameZon3.setGeometry(QtCore.QRect(430, 430, 201, 31))
        self.gameZon3.setObjectName("gameZon3")
        self.changeMenu = QtWidgets.QLabel(self.centralwidget)
        self.changeMenu.setGeometry(QtCore.QRect(310, 240, 461, 71))
        self.changeMenu.setObjectName("changeMenu")
        self.timeGame = QtWidgets.QLabel(self.centralwidget)
        self.timeGame.setGeometry(QtCore.QRect(30, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeGame.setFont(font)
        self.timeGame.setObjectName("timeGame")
        self.itsGame.raise_()
        self.welcome.raise_()
        self.mainMenu.raise_()
        self.label.raise_()
        self.startGame.raise_()
        self.settingsButton.raise_()
        self.exitGame.raise_()
        self.zaba.raise_()
        self.gameZon1.raise_()
        self.gameZon2.raise_()
        self.gameZon3.raise_()
        self.changeMenu.raise_()
        self.timeGame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settingsButton.setText(_translate("MainWindow", "Настройки"))
        self.startGame.setText(_translate("MainWindow", "Начать игру"))
        self.exitGame.setText(_translate("MainWindow", "Выйти из игры"))
        self.welcome.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Добро пожаловать в мою игру</span></p></body></html>"))
        self.mainMenu.setText(_translate("MainWindow", "Вернуться в главное меню"))
        self.gameZon1.setText(_translate("MainWindow", "1 игровое поле"))
        self.gameZon2.setText(_translate("MainWindow", "2 игровое поле"))
        self.gameZon3.setText(_translate("MainWindow", "3 игровое поле"))
        self.changeMenu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Выберите Игровое поле среди предложенных:</span></p></body></html>"))
        self.timeGame.setText(_translate("MainWindow", "Осталось времени: "))
