from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor

class QBall(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self._ballColor = QColor('black')

    def ballColor(self):
        return self._ballColor

    def setBallColor(self, color):
        self._ballColor = color
