import time
from tab1 import Tab1Action
from typing import NoReturn
from PyQt5 import QtCore, QtGui, QtWidgets

from design import Ui_MainWindow
from tab1 import Tab1Action
from tab2 import Tab2Action
from checkCondition import checkCondition
from splashScreen import SplashScreen
from animation import Animation
from changesInDesign import Changer

from collections import Counter

class mainUI(Ui_MainWindow, Tab1Action, Tab2Action, Changer):
    def preInit(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        x_center = int(resolution.width() / 2 - lb.frameSize().width()/2)
        y_center = int(resolution.height() / 2 - lb.frameSize().height()/2)

        an = Animation().animation(lb, x_center, y_center, MainWindow)
        an.start()
        lb.show()

    def init(self):
        # make the checkBoxes of heterozigosity disabled
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        # handing methods on actions
        self.pushButton.clicked.connect(self.takeData)
        self.pushButton_2.clicked.connect(self.clearLabelsTab2)
        self.pushButton_2.clicked.connect(self.actionTab2)
        self.pushButton_3.clicked.connect(self.goBackPage)
        self.pushButton_4.clicked.connect(self.goNextPage)

        self.comboBox.currentIndexChanged.connect(lambda : checkCondition(self.comboBox, self.checkBox_3))
        self.comboBox_2.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_2, self.checkBox_4))
        self.comboBox_3.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_3, self.checkBox_6))
        self.comboBox_4.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_4, self.checkBox_8))
        # time.sleep(3)
        lb.close()
        
        # self.onFinish()

    def onFinish(self):
        print("show window")
        MainWindow.show()

class OwnThread(QtCore.QThread):
    def __init__(self, parent = None):
        super(OwnThread, self).__init__(parent)

    def run(self):
        pass
        # ui.init()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainUI()
    
    lb = SplashScreen().create()
    ui.preInit()
    ui.setupUi(MainWindow)
    ui.change()
    
    ui.init()
    MainWindow.show()

    myThread = OwnThread()
    # MainWindow.moveToThread(myThread)
    myThread.finished.connect(ui.onFinish)
    myThread.start()
    

    # ui.setupUi(MainWindow)
    # ui.init()
    # MainWindow.show()
    sys.exit(app.exec_())