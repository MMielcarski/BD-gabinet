# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\logowanie_python.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Logowanie_Window(object):
    def setupUi(self, Logowanie_Window):
        Logowanie_Window.setObjectName("Logowanie_Window")
        Logowanie_Window.resize(407, 241)
        self.email_label = QtWidgets.QLabel(Logowanie_Window)
        self.email_label.setGeometry(QtCore.QRect(40, 50, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setMidLineWidth(1)
        self.email_label.setTextFormat(QtCore.Qt.RichText)
        self.email_label.setObjectName("email_label")
        self.haslo_label = QtWidgets.QLabel(Logowanie_Window)
        self.haslo_label.setGeometry(QtCore.QRect(40, 100, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.haslo_label.setFont(font)
        self.haslo_label.setMidLineWidth(1)
        self.haslo_label.setTextFormat(QtCore.Qt.RichText)
        self.haslo_label.setObjectName("haslo_label")
        self.email_lineEdit = QtWidgets.QLineEdit(Logowanie_Window)
        self.email_lineEdit.setGeometry(QtCore.QRect(160, 60, 211, 22))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.haslo_lineEdit = QtWidgets.QLineEdit(Logowanie_Window)
        self.haslo_lineEdit.setGeometry(QtCore.QRect(160, 120, 211, 22))
        self.haslo_lineEdit.setObjectName("haslo_lineEdit")
        self.info_label = QtWidgets.QLabel(Logowanie_Window)
        self.info_label.setGeometry(QtCore.QRect(60, 0, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info_label.setFont(font)
        self.info_label.setMidLineWidth(1)
        self.info_label.setTextFormat(QtCore.Qt.RichText)
        self.info_label.setObjectName("info_label")
        self.zaloguj_pushButton = QtWidgets.QPushButton(Logowanie_Window)
        self.zaloguj_pushButton.setGeometry(QtCore.QRect(80, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zaloguj_pushButton.setFont(font)
        self.zaloguj_pushButton.setDefault(True)
        self.zaloguj_pushButton.setObjectName("zaloguj_pushButton")
        self.powrot_pushButton = QtWidgets.QPushButton(Logowanie_Window)
        self.powrot_pushButton.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.powrot_pushButton.setObjectName("powrot_pushButton")

        self.retranslateUi(Logowanie_Window)
        QtCore.QMetaObject.connectSlotsByName(Logowanie_Window)

    def retranslateUi(self, Logowanie_Window):
        _translate = QtCore.QCoreApplication.translate
        Logowanie_Window.setWindowTitle(_translate("Logowanie_Window", "Dialog"))
        self.email_label.setText(_translate("Logowanie_Window", "e-mail"))
        self.haslo_label.setText(_translate("Logowanie_Window", "hasło"))
        self.info_label.setText(_translate("Logowanie_Window", "Zaloguj się podając adres e-mail i hasło"))
        self.zaloguj_pushButton.setText(_translate("Logowanie_Window", "Zaloguj"))
        self.powrot_pushButton.setText(_translate("Logowanie_Window", "Powrót"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Logowanie_Window = QtWidgets.QDialog()
    ui = Ui_Logowanie_Window()
    ui.setupUi(Logowanie_Window)
    Logowanie_Window.show()
    sys.exit(app.exec_())
