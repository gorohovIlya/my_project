# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtWidgets.QLabel(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(80, 50, 211, 31))
        self.search.setObjectName("search")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.find_creature = QtWidgets.QLabel(self.centralwidget)
        self.find_creature.setGeometry(QtCore.QRect(200, 150, 381, 31))
        self.find_creature.setObjectName("find_creature")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 141, 141))
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/map_icons/island.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 260, 141, 141))
        self.label_5.setStyleSheet("border-image: url(:/newPrefix/map_icons/aberration.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.theislandbtn = QtWidgets.QPushButton(self.centralwidget)
        self.theislandbtn.setGeometry(QtCore.QRect(30, 410, 121, 31))
        self.theislandbtn.setObjectName("theislandbtn")
        self.scorchedbtn = QtWidgets.QPushButton(self.centralwidget)
        self.scorchedbtn.setGeometry(QtCore.QRect(350, 410, 121, 31))
        self.scorchedbtn.setObjectName("scorchedbtn")
        self.aberbtn = QtWidgets.QPushButton(self.centralwidget)
        self.aberbtn.setGeometry(QtCore.QRect(190, 410, 121, 31))
        self.aberbtn.setObjectName("aberbtn")
        self.extinctionbtn = QtWidgets.QPushButton(self.centralwidget)
        self.extinctionbtn.setGeometry(QtCore.QRect(670, 410, 121, 31))
        self.extinctionbtn.setObjectName("extinctionbtn")
        self.ragnarokbtn = QtWidgets.QPushButton(self.centralwidget)
        self.ragnarokbtn.setGeometry(QtCore.QRect(510, 410, 121, 31))
        self.ragnarokbtn.setObjectName("ragnarokbtn")
        self.settings = QtWidgets.QToolButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(30, 480, 131, 31))
        self.settings.setObjectName("settings")
        self.aboutprogram = QtWidgets.QPushButton(self.centralwidget)
        self.aboutprogram.setGeometry(QtCore.QRect(660, 480, 131, 31))
        self.aboutprogram.setObjectName("aboutprogram")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 280, 141, 91))
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/map_icons/ragnarok.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 260, 141, 141))
        self.label_7.setStyleSheet("border-image: url(:/newPrefix/map_icons/extinction.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 260, 141, 141))
        self.label_8.setStyleSheet("border-image: url(:/newPrefix/map_icons/scorched.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Поиск существа / параметра:</span></p></body></html>"))
        self.find_creature.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Найти существо самостоятельно на одной из карт:</span></p></body></html>"))
        self.theislandbtn.setText(_translate("MainWindow", "The Island"))
        self.scorchedbtn.setText(_translate("MainWindow", "Scorched Earth"))
        self.aberbtn.setText(_translate("MainWindow", "Aberration"))
        self.extinctionbtn.setText(_translate("MainWindow", "Extinction"))
        self.ragnarokbtn.setText(_translate("MainWindow", "Ragnarok"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.aboutprogram.setText(_translate("MainWindow", "О программе"))

