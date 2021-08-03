from PyQt5 import QtCore, QtGui, QtWidgets

class SplashScreen():
    def create(self):
        lb = QtWidgets.QLabel()
        lb.setScaledContents(1)

        pixmap = QtGui.QPixmap("icon-blood.svg")
        lb.setPixmap(pixmap)
        lb.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        lb.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        lb.setGeometry(QtCore.QRect(0, 0, 171, 171))
        return lb