# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\menuPreBooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 588)
        MainWindow.setStyleSheet("background-color: \"#60ACE9\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 290, 321, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton.setStyleSheet("font: 11pt \"Candara\";\n"
"border: 2px solid white; \n"
"border-radius: 10px;\n"
"color: white; ")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 360, 321, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget_2)
        self.commandLinkButton_2.setStyleSheet("font: 11pt \"Candara\";\n"
"border: 2px solid white; \n"
"border-radius: 10px; \n"
"color: white; ")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout_2.addWidget(self.commandLinkButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 201, 201))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(110, 430, 321, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget_3)
        self.commandLinkButton_3.setStyleSheet("font: 11pt \"Candara\";\n"
"border: 2px solid white; \n"
"border-radius: 10px; \n"
"color: white; ")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout_3.addWidget(self.commandLinkButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
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
        self.commandLinkButton.setText(_translate("MainWindow", "Consultar información sobre una piscina"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Realizar reserva"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Logo/Logo.png\" width=\"200\" height=\"200\"/></p></body></html>"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Cancelar reserva"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
