# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designConv2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_16 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox_3)
        self.horizontalLayout_10.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        self.label_17 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox_4)
        self.horizontalLayout_10.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bloty calculator"))
        self.label_3.setText(_translate("MainWindow", "Уведіть вхідні дані:"))
        self.label.setText(_translate("MainWindow", "Група крові чоловіка"))
        self.comboBox.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox.setItemText(3, _translate("MainWindow", "IV"))
        self.label_4.setText(_translate("MainWindow", "Резус позитивність"))
        self.label_16.setText(_translate("MainWindow", "Гетерозиготність"))
        self.label_2.setText(_translate("MainWindow", "Група крові жінки"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "I"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "II"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "III"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "IV"))
        self.label_5.setText(_translate("MainWindow", "Резус позитивність"))
        self.label_17.setText(_translate("MainWindow", "Гетерозиготність"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "firstr"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "secondr"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "thirdr"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "fourthr"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "firstc"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "secondc"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "thirdc"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "fourthc"))
        self.pushButton.setText(_translate("MainWindow", "Розрахувати"))
        self.label_6.setText(_translate("MainWindow", "Відповідно до вхідних даних у дітей можуть бути такі групи крові:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1 задача"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2 задача"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3 задача"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
