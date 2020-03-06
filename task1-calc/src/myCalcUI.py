# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myCalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 261, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:40px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#e7e7e7;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 190, 260, 200))
        self.widget.setMinimumSize(QtCore.QSize(0, 45))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.widget)
        self.pushButton_div.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_div.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 3, 3, 1, 1)
        self.pushButton_equal = QtWidgets.QPushButton(self.widget)
        self.pushButton_equal.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_equal.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#555555;\n"
"color:white;")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.gridLayout.addWidget(self.pushButton_equal, 3, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_9.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_6.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.widget)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_sub.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 1, 3, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.widget)
        self.pushButton_plus.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_plus.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setAutoFillBackground(False)
        self.pushButton_plus.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#4CAF50;\n"
"color:white;")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_7.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_5.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_point = QtWidgets.QPushButton(self.widget)
        self.pushButton_point.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_point.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#4CAF50;\n"
"color:white;")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 3, 1, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.widget)
        self.pushButton_0.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_0.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_1.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#008CBA;\n"
"color:white;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.widget)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(60, 45))
        self.pushButton_mul.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"font-size:25px;\n"
"border-color: rgb(85, 85, 255);\n"
"border-radius:10px;\n"
"background-color:#4CAF50;\n"
"color:white;\n"
"")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 130, 261, 42))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_DEL = QtWidgets.QPushButton(self.widget1)
        self.pushButton_DEL.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_DEL.setFont(font)
        self.pushButton_DEL.setStyleSheet("background-color: rgb(255, 96, 23);\n"
"border-radius:10px;\n"
"color:white;")
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.horizontalLayout.addWidget(self.pushButton_DEL)
        self.pushButton_AC = QtWidgets.QPushButton(self.widget1)
        self.pushButton_AC.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_AC.setFont(font)
        self.pushButton_AC.setStyleSheet("background-color: rgb(255, 96, 23);\n"
"border-radius:10px;\n"
"color:white;")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.horizontalLayout.addWidget(self.pushButton_AC)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 23))
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
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_mul.setText(_translate("MainWindow", "*"))
        self.pushButton_DEL.setText(_translate("MainWindow", "DEL"))
        self.pushButton_AC.setText(_translate("MainWindow", "AC"))
