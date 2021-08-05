from typing import NoReturn
from PyQt5 import QtCore, QtGui, QtWidgets

from design import Ui_MainWindow
from tab1 import Tab1Action
from tab2 import Tab2Action
from tab3 import Tab3Action
from checkCondition import checkCondition
from splashScreen import SplashScreen
from animation import Animation
from style import Changer

from collections import Counter

class mainUI(Ui_MainWindow, Tab1Action, Tab2Action, Tab3Action, Changer):
    def preInit(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        x_center = int(resolution.width() / 2 - lb.frameSize().width()/2)
        y_center = int(resolution.height() / 2 - lb.frameSize().height()/2)

        an = Animation().animation(lb, x_center, y_center, MainWindow)
        an.finished.connect(self.onFinishAnimation)
        an.start()
        lb.show()

    def init(self):
        # Tab3Action().__init__()
        # make the checkBoxes of heterozigosity disabled
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_8.setEnabled(False)
        self.checkBox_10.setEnabled(False)
        # handing methods on actions
        self.pushButton.clicked.connect(self.takeData)
        self.pushButton_2.clicked.connect(self.clearLabelsTab2)
        self.pushButton_2.clicked.connect(self.actionTab2)
        self.pushButton_3.clicked.connect(self.goBackPage)
        self.pushButton_4.clicked.connect(self.goNextPage)

        # button "Розрахувати" in 3 tab
        self.pushButton_5.clicked.connect(self.actionTab3)

        # buttons with arrows in 3 tab
        # self.pushButton_8.clicked.connect(self.resetToDefaultGroupsLabels)
        # self.pushButton_9.clicked.connect(self.resetToDefaultGroupsLabels)
        # self.pushButton_10.clicked.connect(self.resetToDefaultGroupsLabels)
        # self.pushButton_11.clicked.connect(self.resetToDefaultGroupsLabels)

        self.pushButton_8.clicked.connect(self.goUpFather)
        self.pushButton_9.clicked.connect(self.goDownFather)
        self.pushButton_10.clicked.connect(self.goUpMother)
        self.pushButton_11.clicked.connect(self.goDownMother)

        # check condition in 1 tab
        self.comboBox.currentIndexChanged.connect(lambda : checkCondition(self.comboBox, self.checkBox_3))
        self.comboBox_2.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_2, self.checkBox_4))
        # check condition in 2 tab
        self.comboBox_3.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_3, self.checkBox_6))
        self.comboBox_4.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_4, self.checkBox_8))
        # check condition in 3 tab
        self.comboBox_5.currentIndexChanged.connect(lambda : checkCondition(self.comboBox_5, self.checkBox_10))

        self.comboBox_5.currentIndexChanged.connect(self.clearGlobalVarTab3)
        self.checkBox_9.clicked.connect(self.clearGlobalVarTab3)
        self.checkBox_10.clicked.connect(self.clearGlobalVarTab3)

        self.setStyleToChosenGroup()
    def onFinishAnimation(self):
        MainWindow.show()
        lb.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainUI()
    
    splash = SplashScreen()
    lb = splash.create()
    ui.preInit()

    ui.setupUi(MainWindow)
    ui.change()
    ui.init()

    sys.exit(app.exec_())