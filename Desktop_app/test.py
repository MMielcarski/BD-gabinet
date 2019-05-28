# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import sys
#
# class Model(QAbstractTableModel):
#     def __init__(self, parent=None, *args):
#         QAbstractTableModel.__init__(self, parent, *args)
#         self.items = ['Row0_Column0','Row0_Column1','Row0_Column2']
#
#     def flags(self, index):
#         return Qt.ItemIsEnabled | Qt.ItemIsSelectable
#
#     def rowCount(self, parent):
#         return 1
#     def columnCount(self, parent):
#         return len(self.items)
#
#     def data(self, index, role):
#         if not index.isValid(): return QVariant()
#         elif role != Qt.DisplayRole:
#             return QVariant()
#
#         column=index.column()
#         if column<len(self.items):
#             return QVariant(self.items[column])
#         else:
#             return QVariant()
#
# class MyWindow(QWidget):
#     def __init__(self, *args):
#         QWidget.__init__(self, *args)
#
#         tablemodel=Model(self)
#
#         self.tableview=QTableView()
#         self.tableview.setModel(tablemodel)
#         self.tableview.clicked.connect(self.viewClicked)
#
#         self.tableview.setSelectionBehavior(QTableView.SelectRows)
#
#         layout = QHBoxLayout(self)
#         layout.addWidget(self.tableview)
#
#         self.setLayout(layout)
#
#     def viewClicked(self, clickedIndex):
#         row=clickedIndex.row()
#         model=clickedIndex.model()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = MyWindow()
#     w.show()
#     sys.exit(app.exec_())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore


class LoginWindow(QtWidgets.QWidget):

    got_password = QtCore.pyqtSignal(str)

    def __init__(self):
        super(LoginWindow, self).__init__()

        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        send_button = QtWidgets.QPushButton("Send")
        close_button = QtWidgets.QPushButton("Close")

        send_button.clicked.connect(self.send_clicked)
        close_button.clicked.connect(self.close)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.password)
        layout.addWidget(send_button)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setWindowTitle("Login")
        self.setMinimumWidth(350)

    def send_clicked(self):
        self.got_password.emit(self.password.text())


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.login = LoginWindow()
        self.login.got_password.connect(self.show_it)

        self.edit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton("Get input from window")
        button.clicked.connect(self.get_login)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)

    def get_login(self):
        self.login.show()

    def show_it(self, the_password):
        self.edit.setText(the_password)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())