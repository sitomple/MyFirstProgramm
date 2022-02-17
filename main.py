import sys

from PyQt5 import QtGui, QtWidgets
from ui_Main_form import Ui_MainWindow
from Employee import Employee

def runApplication():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    mainWorker = Employee('Sitomple')
    runApplication()