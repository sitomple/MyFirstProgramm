import sys

from PyQt5 import QtGui, QtWidgets
#from ui_untitled import Ui_MainWindow
from Employee import Employee
from gameFunction import gameSettings

def runApplication():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = gameSettings()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    #mainWorker = Employee('Sitomple')
    runApplication()