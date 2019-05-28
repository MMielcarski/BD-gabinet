# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\logowanie_python.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector
from mysql.connector import errorcode
import haslo
import random
import string
from Desktop_app import send_email

ZALOGOWANY_JAKO = ""


class Ui_Logowanie_Window(object):


    def zaloguj(self):
        global ID_ZALOGOWANEGO_LEKARZA
        ID_ZALOGOWANEGO_LEKARZA = ""

        login = str(self.email_lineEdit.text())
        haslo = str(self.haslo_lineEdit.text())
        print("{} {}".format(login, haslo))

        sql = "SELECT ID_LEKARZA, imie, nazwisko FROM lekarze WHERE adres_email = '"+login+"' AND haslo = '"+haslo+"'"
        print(sql)

        # mycursor.execute(
        #     "SELECT ID_LEKARZA, imie, nazwisko FROM lekarze WHERE adres_email = 'sklodowski_pediatra@gmail.com' AND haslo = 'admin2'")

        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if(len(myresult) == 0):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Błędny e-mail lub hasło.\nSpróbuj ponownie")
            msg.setWindowTitle("Będne dane")
            retval = msg.exec_()
        else:
            ID_ZALOGOWANEGO_LEKARZA = str(myresult[0][0])
            print("ID lekarza: ", ID_ZALOGOWANEGO_LEKARZA)
            ZALOGOWANY_JAKO = str(myresult[0][1])+ " " + str(myresult[0][2])
            print("Zalogowany jako", ZALOGOWANY_JAKO)
            Logowanie_Window.hide()
            self.main_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.main_window)
            self.main_window.show()


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
        self.haslo_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
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

        self.zaloguj_pushButton.clicked.connect(self.zaloguj)
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


##########################################################################################

class Ui_MainWindow(object):

    def dodaj_pacjenta(self):
        self.dodajpacjenta = QtWidgets.QMainWindow()
        self.ui = Ui_Dodaj_pacjenta()
        self.ui.setupUi(self.dodajpacjenta)
        self.dodajpacjenta.show()

    def wybierz_pacjenta(self):
        self.wybor_pacjenta = QtWidgets.QMainWindow()
        self.ui = Ui_Wybor_pacjenta()
        self.ui.setupUi(self.wybor_pacjenta)
        self.wybor_pacjenta.show()


    def usun_pacjenta(self):
        self.usunpacjenta = QtWidgets.QMainWindow()
        self.ui = Ui_Usunpacjenta()
        self.ui.setupUi(self.usunpacjenta)
        self.usunpacjenta.show()


    def pokaz_wszystkich_pacjentow(self):
        self.pokazwszystkich_window = QtWidgets.QMainWindow()
        self.ui = Ui_Wszyscypacjenci()
        self.ui.setupUi(self.pokazwszystkich_window)
        self.pokazwszystkich_window.show()

    def pokaz_wszystkich_lekarzy(self):
        self.pokazwszystkichlekarzy_window = QtWidgets.QMainWindow()
        self.ui = Ui_Wszyscy_lekarze()
        self.ui.setupUi(self.pokazwszystkichlekarzy_window)
        self.pokazwszystkichlekarzy_window.show()

    def pokaz_wszystkie_leki(self):
        self.pokazwszystkieleki_window = QtWidgets.QMainWindow()
        self.ui = Ui_baza_lekow()
        self.ui.setupUi(self.pokazwszystkieleki_window)
        self.pokazwszystkieleki_window.show()

    def dodaj_lek(self):
        self.dodajlek_window = QtWidgets.QMainWindow()
        self.ui = Ui_Dodaj_lek()
        self.ui.setupUi(self.dodajlek_window)
        self.dodajlek_window.show()

    def pokaz_oddzialy_nfz(self):
        self.oddzialynfz_window = QtWidgets.QMainWindow()
        self.ui = Ui_Oddzialy_NFZ()
        self.ui.setupUi(self.oddzialynfz_window)
        self.oddzialynfz_window.show()

    def pokaz_wizyty_do_zatw(self):
        self.wizytydozatw_window = QtWidgets.QMainWindow()
        self.ui = Ui_Wizyty_do_zatwierdzenia()
        self.ui.setupUi(self.wizytydozatw_window)
        self.wizytydozatw_window.show()

    def odswiez_okno(self):
        mycursor.execute("SELECT COUNT(*) FROM wizyty WHERE czy_zatwierdzona = 0 AND ID_LEKARZA = " + \
                         str(ID_ZALOGOWANEGO_LEKARZA))
        result = mycursor.fetchall()
        self.label_2.setText(str(result[0][0]))


    def pokaz_statystyki(self):
        self.pokazstaty = QtWidgets.QMainWindow()
        self.ui = Ui_Statystyki()
        self.ui.setupUi(self.pokazstaty)
        self.pokazstaty.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 172)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 30, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.odswierz_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.odswierz_pushButton.setGeometry(QtCore.QRect(610, 40, 151, 61))
        self.odswierz_pushButton.setObjectName("odswierz_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 26))
        self.menubar.setObjectName("menubar")
        self.menuPAcjenci = QtWidgets.QMenu(self.menubar)
        self.menuPAcjenci.setObjectName("menuPAcjenci")
        self.menuZatwierdz_wizyt = QtWidgets.QMenu(self.menubar)
        self.menuZatwierdz_wizyt.setObjectName("menuZatwierdz_wizyt")
        self.menuStatystyki = QtWidgets.QMenu(self.menubar)
        self.menuStatystyki.setObjectName("menuStatystyki")
        self.menuOddzia_y_NFZ = QtWidgets.QMenu(self.menubar)
        self.menuOddzia_y_NFZ.setObjectName("menuOddzia_y_NFZ")
        self.menuLekarze = QtWidgets.QMenu(self.menubar)
        self.menuLekarze.setObjectName("menuLekarze")
        self.menuLeki = QtWidgets.QMenu(self.menubar)
        self.menuLeki.setObjectName("menuLeki")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWybierz_pacjenta = QtWidgets.QAction(MainWindow)
        self.actionWybierz_pacjenta.setObjectName("actionWybierz_pacjenta")
        self.actionUsun_pacjenta = QtWidgets.QAction(MainWindow)
        self.actionUsun_pacjenta.setObjectName("actionUsun_pacjenta")
        self.actionPoka = QtWidgets.QAction(MainWindow)
        self.actionPoka.setObjectName("actionPoka")
        self.actionPokaz_statystyki = QtWidgets.QAction(MainWindow)
        self.actionPokaz_statystyki.setObjectName("actionPokaz_statystyki")
        self.actionPokaz_dostepne_oddzialy = QtWidgets.QAction(MainWindow)
        self.actionPokaz_dostepne_oddzialy.setObjectName("actionPokaz_dostepne_oddzialy")
        self.actionPokaz_lekarzy = QtWidgets.QAction(MainWindow)
        self.actionPokaz_lekarzy.setObjectName("actionPokaz_lekarzy")
        self.actionPokaz_wszystkich = QtWidgets.QAction(MainWindow)
        self.actionPokaz_wszystkich.setObjectName("actionPokaz_wszystkich")
        self.actionfsd = QtWidgets.QAction(MainWindow)
        self.actionfsd.setObjectName("actionfsd")
        self.actionPokaz_baze_lekow = QtWidgets.QAction(MainWindow)
        self.actionPokaz_baze_lekow.setObjectName("actionPokaz_baze_lekow")
        self.actionDodaj_lek = QtWidgets.QAction(MainWindow)
        self.actionDodaj_lek.setObjectName("actionDodaj_lek")
        self.actionDodaj_pacjenta = QtWidgets.QAction(MainWindow)
        self.actionDodaj_pacjenta.setObjectName("actionDodaj_pacjenta")
        self.menuPAcjenci.addAction(self.actionWybierz_pacjenta)
        self.menuPAcjenci.addAction(self.actionDodaj_pacjenta)
        self.menuPAcjenci.addAction(self.actionUsun_pacjenta)
        self.menuPAcjenci.addAction(self.actionPokaz_wszystkich)
        self.menuPAcjenci.addSeparator()
        self.menuZatwierdz_wizyt.addAction(self.actionPoka)
        self.menuStatystyki.addAction(self.actionPokaz_statystyki)
        self.menuOddzia_y_NFZ.addAction(self.actionPokaz_dostepne_oddzialy)
        self.menuLekarze.addAction(self.actionPokaz_lekarzy)
        self.menuLeki.addAction(self.actionPokaz_baze_lekow)
        self.menuLeki.addAction(self.actionDodaj_lek)
        self.menubar.addAction(self.menuPAcjenci.menuAction())
        self.menubar.addAction(self.menuLekarze.menuAction())
        self.menubar.addAction(self.menuZatwierdz_wizyt.menuAction())
        self.menubar.addAction(self.menuLeki.menuAction())
        self.menubar.addAction(self.menuOddzia_y_NFZ.menuAction())
        self.menubar.addAction(self.menuStatystyki.menuAction())

        self.actionDodaj_pacjenta.triggered.connect(self.dodaj_pacjenta)
        self.actionPokaz_wszystkich.triggered.connect(self.pokaz_wszystkich_pacjentow)
        self.actionWybierz_pacjenta.triggered.connect(self.wybierz_pacjenta)
        self.actionUsun_pacjenta.triggered.connect(self.usun_pacjenta)
        self.actionPokaz_lekarzy.triggered.connect(self.pokaz_wszystkich_lekarzy)
        self.actionPokaz_baze_lekow.triggered.connect(self.pokaz_wszystkie_leki)
        self.actionDodaj_lek.triggered.connect(self.dodaj_lek)
        self.actionPokaz_dostepne_oddzialy.triggered.connect(self.pokaz_oddzialy_nfz)
        self.actionPoka.triggered.connect(self.pokaz_wizyty_do_zatw)
        self.odswierz_pushButton.clicked.connect(self.odswiez_okno)
        self.actionPokaz_statystyki.triggered.connect(self.pokaz_statystyki)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        mycursor.execute("SELECT COUNT(*) FROM wizyty WHERE czy_zatwierdzona = 0 AND ID_LEKARZA = " + \
                         str(ID_ZALOGOWANEGO_LEKARZA))
        result = mycursor.fetchall()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BDGabinet"))
        self.label.setText(_translate("MainWindow", "Pacjenci do zatwierdzenia: "))
        self.label_2.setText(_translate("MainWindow", str(result[0][0])))
        self.odswierz_pushButton.setText(_translate("MainWindow", "Odśwież"))
        self.menuPAcjenci.setTitle(_translate("MainWindow", "Pacjenci"))
        self.menuZatwierdz_wizyt.setTitle(_translate("MainWindow", "Zatwierdź wizytę"))
        self.menuStatystyki.setTitle(_translate("MainWindow", "Statystyki"))
        self.menuOddzia_y_NFZ.setTitle(_translate("MainWindow", "Oddziały NFZ"))
        self.menuLekarze.setTitle(_translate("MainWindow", "Lekarze"))
        self.menuLeki.setTitle(_translate("MainWindow", "Leki"))
        self.actionWybierz_pacjenta.setText(_translate("MainWindow", "Wybierz pacjenta"))
        self.actionUsun_pacjenta.setText(_translate("MainWindow", "Usuń pacjenta"))
        self.actionPoka.setText(_translate("MainWindow", "Pokaż"))
        self.actionPokaz_statystyki.setText(_translate("MainWindow", "Pokaż statystyki"))
        self.actionPokaz_dostepne_oddzialy.setText(_translate("MainWindow", "Pokaż dostępne oddziały"))
        self.actionPokaz_lekarzy.setText(_translate("MainWindow", "Pokaż lekarzy"))
        self.actionPokaz_wszystkich.setText(_translate("MainWindow", "Pokaż wszystkich"))
        self.actionfsd.setText(_translate("MainWindow", "fsd"))
        self.actionPokaz_baze_lekow.setText(_translate("MainWindow", "Pokaż bazę leków"))
        self.actionDodaj_lek.setText(_translate("MainWindow", "Dodaj lek "))
        self.actionDodaj_pacjenta.setText(_translate("MainWindow", "Dodaj pacjenta"))


###########################################################################

class Ui_Wybor_pacjenta(object):

    def pobierz_pesel(self):
        global PESEL_pacjenta
        PESEL_pacjenta = str(self.PESEL_lineEdit.text())
        global IMIE_I_NAZWISKO_WYB_PACJENTA
        IMIE_I_NAZWISKO_WYB_PACJENTA = " "
        global ID_WYB_PACJENTA
        ID_WYB_PACJENTA = " "

        if PESEL_pacjenta != None and len(PESEL_pacjenta) == 11:
            try:
                mycursor.execute("SELECT imie, nazwisko, ID_PACJENTA FROM pacjenci WHERE PESEL = " + str(PESEL_pacjenta))
                result = mycursor.fetchall()
                print(len(result))
                if(len(result)) != 0:
                    IMIE_I_NAZWISKO_WYB_PACJENTA = str(result[0][0]) + " " + str(result[0][1])
                    ID_WYB_PACJENTA = str(result[0][2])
                    print("Wybrano: ", IMIE_I_NAZWISKO_WYB_PACJENTA)
                    print("ID: ", ID_WYB_PACJENTA)
                    self.oknopacjenta = QtWidgets.QMainWindow()
                    self.ui = Ui_Pacjent_window()
                    self.ui.setupUi(self.oknopacjenta)
                    self.oknopacjenta.show()
                else:
                    print("nok")
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("Nie znaleziono pacjenta o takim numerze PESEL.\nSpróbuj ponownie")
                    msg.setWindowTitle("Będne dane")
                    retval = msg.exec_()
            except:
                print("Error")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Błędny numer PESEL.\nSpróbuj ponownie")
            msg.setWindowTitle("Będne dane")
            retval = msg.exec_()





    def setupUi(self, Wybor_pacjenta):
        Wybor_pacjenta.setObjectName("Wybor_pacjenta")
        Wybor_pacjenta.resize(415, 119)
        self.wybierz_pushButton = QtWidgets.QPushButton(Wybor_pacjenta)
        self.wybierz_pushButton.setGeometry(QtCore.QRect(100, 60, 93, 28))
        self.wybierz_pushButton.setObjectName("wybierz_pushButton")
        self.wybierz_pushButton.clicked.connect(self.pobierz_pesel)
        self.label = QtWidgets.QLabel(Wybor_pacjenta)
        self.label.setGeometry(QtCore.QRect(220, 40, 55, 16))
        self.label.setObjectName("label")
        self.PESEL_lineEdit = QtWidgets.QLineEdit(Wybor_pacjenta)
        self.PESEL_lineEdit.setGeometry(QtCore.QRect(220, 60, 113, 22))
        self.PESEL_lineEdit.setObjectName("PESEL_lineEdit")
        self.label_2 = QtWidgets.QLabel(Wybor_pacjenta)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Wybor_pacjenta)
        QtCore.QMetaObject.connectSlotsByName(Wybor_pacjenta)

    def retranslateUi(self, Wybor_pacjenta):
        _translate = QtCore.QCoreApplication.translate
        Wybor_pacjenta.setWindowTitle(_translate("Wybor_pacjenta", "Dialog"))
        self.wybierz_pushButton.setText(_translate("Wybor_pacjenta", "Wybierz"))
        self.label.setText(_translate("Wybor_pacjenta", "PESEL"))
        self.label_2.setText(_translate("Wybor_pacjenta", "Wybierz pacjenta podając jego numr PESEL"))

#######################################################################################

class Ui_Wszyscypacjenci(object):

    def wybierz_pacjenta(self):

        global PESEL_pacjenta
        global IMIE_I_NAZWISKO_WYB_PACJENTA
        IMIE_I_NAZWISKO_WYB_PACJENTA = " "
        global ID_WYB_PACJENTA
        ID_WYB_PACJENTA = " "

        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row()
        imie      =  self.tableWidget.item(row_number, 0).text()
        nazwisko  =  self.tableWidget.item(row_number, 1).text()
        PESEL_pacjenta     =  self.tableWidget.item(row_number, 2).text()

        mycursor.execute("SELECT ID_PACJENTA FROM pacjenci WHERE PESEL = "+str(PESEL_pacjenta))
        result = mycursor.fetchone()

        IMIE_I_NAZWISKO_WYB_PACJENTA = imie + " " + nazwisko
        ID_WYB_PACJENTA = str(result[0])
        print("Wybrano: ", IMIE_I_NAZWISKO_WYB_PACJENTA)
        print("ID: ", ID_WYB_PACJENTA)


        self.oknopacjenta = QtWidgets.QMainWindow()
        self.ui = Ui_Pacjent_window()
        self.ui.setupUi(self.oknopacjenta)
        self.oknopacjenta.show()


    def setupUi(self, Wszyscypacjenci):
        Wszyscypacjenci.setObjectName("Wszyscypacjenci")
        Wszyscypacjenci.resize(595, 507)
        self.tableWidget = QtWidgets.QTableWidget(Wszyscypacjenci)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 881, 491))
        self.tableWidget.setObjectName("Wszyscy pacjenci")
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        mycursor.execute("SELECT imie, nazwisko, PESEL, adres_email, nr_tel FROM pacjenci")
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(len(myresult))
        self.tableWidget.setColumnCount(5)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        row = 0

        mycursor.execute("SELECT imie, nazwisko, PESEL, adres_email, nr_tel FROM pacjenci")
        while True:
            sqlRow = mycursor.fetchone()
            if sqlRow == None:
                break
            print(sqlRow)
            for col in range(0,5):
                self.tableWidget.setItem(row,col,QtWidgets.QTableWidgetItem(str(sqlRow[col])))
            row = row+1

        self.tableWidget.resizeColumnsToContents()

        self.tableWidget.doubleClicked.connect(self.wybierz_pacjenta)

        self.retranslateUi(Wszyscypacjenci)
        QtCore.QMetaObject.connectSlotsByName(Wszyscypacjenci)

    def retranslateUi(self, Wszyscypacjenci):
        _translate = QtCore.QCoreApplication.translate
        Wszyscypacjenci.setWindowTitle(_translate("Wszyscypacjenci", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Wszyscypacjenci", "Imię"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Wszyscypacjenci", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Wszyscypacjenci", "PESEL"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Wszyscypacjenci", "e-mail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Wszyscypacjenci", "Nr.tel"))

###############################################################################

class Ui_Dodaj_pacjenta(object):
    def gen_haslo(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(8))

    def dodaj(self):
        imie = self.tableWidget.item(0, 0).text()
        nazwisko = self.tableWidget.item(0, 1).text()
        nrtel = self.tableWidget.item(0, 2).text()
        email = self.tableWidget.item(0, 3).text()
        ID_oddzialu = 1
        pesel = 0
        haslo = self.gen_haslo()

        if imie != None and nazwisko != None and pesel != None and nrtel != None and email != None:
            try:
                sql = "INSERT INTO pacjenci(imie, nazwisko, PESEL, adres_email, nr_tel, ID_ODDZIALU_NFZ, haslo)" \
                      + "VALUES (" + "\"" + str(imie) + "\"" + "," + "\"" + str(nazwisko) + "\"" + "," + str(pesel) \
                      + "," + "\"" + str(email) + "\"" + "," + "\"" + str(nrtel) + "\"" \
                      + "," + str(1) + "," + "\"" + str(haslo) + "\"" + ")"
                print(sql)

                mycursor.execute(sql)
                mydb.commit()
                send_email.send_first_time_email(str(email), str(haslo))

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Dodano pacjenta.\nEmail został wysłany")
                msg.setWindowTitle("Dodano pacjenta")
                retval = msg.exec_()
            except:
                print("Error")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Błedne dane.\nSpróbuj ponownie")
            msg.setWindowTitle("Będne dane")
            retval = msg.exec_()


    def setupUi(self, Dodaj_pacjenta):
        Dodaj_pacjenta.setObjectName("Dodaj_pacjenta")
        Dodaj_pacjenta.resize(576, 143)
        self.tableWidget = QtWidgets.QTableWidget(Dodaj_pacjenta)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 561, 61))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(Dodaj_pacjenta)
        self.pushButton.setGeometry(QtCore.QRect(10, 77, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.dodaj)


        self.retranslateUi(Dodaj_pacjenta)
        QtCore.QMetaObject.connectSlotsByName(Dodaj_pacjenta)

    def retranslateUi(self, Dodaj_pacjenta):
        _translate = QtCore.QCoreApplication.translate
        Dodaj_pacjenta.setWindowTitle(_translate("Dodaj_pacjenta", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dodaj_pacjenta", "Nowy"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dodaj_pacjenta", "Imię"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dodaj_pacjenta", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dodaj_pacjenta", "Nr.Tel"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dodaj_pacjenta", "e-mail"))
        self.pushButton.setText(_translate("Dodaj_pacjenta", "Dodaj"))

###############################################################################################

class Ui_Usunpacjenta(object):

    def usunpacjenta(self):

        pesel = str(self.PESEL_lineEdit.text())

        if len(pesel) ==11 and (pesel.isdigit() == True):
            try:
                sql = "DELETE FROM 'pacjenci' WHERE 'pacjenci'.'PESEL' = " + str(pesel)
                print(sql)
                mycursor.execute(sql)
                mydb.commit()

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Usunięto pacjęta")
                msg.setWindowTitle("Usunęto")
                retval = msg.exec_()
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Błędny PESEL")
                msg.setWindowTitle("Będne dane")
                retval = msg.exec_()
                print("Error")



    def setupUi(self, Usunpacjenta):
        Usunpacjenta.setObjectName("Usunpacjenta")
        Usunpacjenta.resize(415, 106)
        self.label_2 = QtWidgets.QLabel(Usunpacjenta)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.wybierz_pushButton = QtWidgets.QPushButton(Usunpacjenta)
        self.wybierz_pushButton.setGeometry(QtCore.QRect(270, 47, 93, 41))
        self.wybierz_pushButton.setObjectName("wybierz_pushButton")
        self.label = QtWidgets.QLabel(Usunpacjenta)
        self.label.setGeometry(QtCore.QRect(50, 40, 55, 16))
        self.label.setObjectName("label")
        self.PESEL_lineEdit = QtWidgets.QLineEdit(Usunpacjenta)
        self.PESEL_lineEdit.setGeometry(QtCore.QRect(50, 60, 161, 22))
        self.PESEL_lineEdit.setObjectName("PESEL_lineEdit")

        self.wybierz_pushButton.clicked.connect(self.usunpacjenta)

        self.retranslateUi(Usunpacjenta)
        QtCore.QMetaObject.connectSlotsByName(Usunpacjenta)

    def retranslateUi(self, Usunpacjenta):
        _translate = QtCore.QCoreApplication.translate
        Usunpacjenta.setWindowTitle(_translate("Usunpacjenta", "Dialog"))
        self.label_2.setText(_translate("Usunpacjenta", "Usuń pacjenta podając jego numer PESEL"))
        self.wybierz_pushButton.setText(_translate("Usunpacjenta", "Usuń"))
        self.label.setText(_translate("Usunpacjenta", "PESEL"))

############################################################################################

class Ui_Wszyscy_lekarze(object):
    def setupUi(self, Wszyscy_lekarze):
        Wszyscy_lekarze.setObjectName("Wszyscy_lekarze")
        Wszyscy_lekarze.resize(895, 270)
        self.tableWidget = QtWidgets.QTableWidget(Wszyscy_lekarze)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 881, 261))
        self.tableWidget.setObjectName("tableWidget")


        mycursor.execute("SELECT tytul, imie, nazwisko, specjalizacja, adres_email, nr_tel, nr_pwz FROM lekarze")
        myresult = mycursor.fetchall()
        print(myresult)
        self.tableWidget.setRowCount(len(myresult))
        print(len(myresult))
        self.tableWidget.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        row = 0
        try:
            mycursor.execute("SELECT tytul, imie, nazwisko, specjalizacja, adres_email, nr_tel, nr_pwz FROM lekarze")
            while True:
                sqlRow = mycursor.fetchone()
                if sqlRow == None:
                    break
                print(str(sqlRow))
                for col in range(0, 7):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                row = row + 1
        except:
            print("Error")

        self.retranslateUi(Wszyscy_lekarze)
        QtCore.QMetaObject.connectSlotsByName(Wszyscy_lekarze)

    def retranslateUi(self, Wszyscy_lekarze):
        _translate = QtCore.QCoreApplication.translate
        Wszyscy_lekarze.setWindowTitle(_translate("Wszyscy_lekarze", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Wszyscy_lekarze", "Tytuł"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Wszyscy_lekarze", "Imię"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Wszyscy_lekarze", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Wszyscy_lekarze", "Specjalizacja"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Wszyscy_lekarze", "e-mail"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Wszyscy_lekarze", "Nr.Tel"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Wszyscy_lekarze", "Numer PWZ"))

###################################################################################

class Ui_baza_lekow(object):
    def setupUi(self, baza_lekow):
        baza_lekow.setObjectName("baza_lekow")
        baza_lekow.resize(886, 468)
        self.tableWidget = QtWidgets.QTableWidget(baza_lekow)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 881, 451))
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(7)
        # self.tableWidget.setRowCount(1)

        mycursor.execute("SELECT nazwa, postac, dawka, sklad, czy_refundowany, procent_refundacji, czy_na_recepte from leki")
        myresult = mycursor.fetchall()
        print(myresult)
        self.tableWidget.setRowCount(len(myresult))
        print(len(myresult))
        self.tableWidget.setColumnCount(7)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)


        row = 0
        try:
            mycursor.execute("SELECT nazwa, postac, dawka, sklad, czy_refundowany, procent_refundacji, czy_na_recepte from leki")
            while True:
                sqlRow = mycursor.fetchone()
                if sqlRow == None:
                    break
                print(str(sqlRow))
                for col in range(0, 7):
                    if sqlRow[col] == None:
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str("Brak")))
                    elif sqlRow[col] == "n":
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str("Tak")))
                    elif sqlRow[col] == "t":
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str("Tak")))
                    else:
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                row = row + 1
        except:
            print("Error")

        self.retranslateUi(baza_lekow)
        QtCore.QMetaObject.connectSlotsByName(baza_lekow)

    def retranslateUi(self, baza_lekow):
        _translate = QtCore.QCoreApplication.translate
        baza_lekow.setWindowTitle(_translate("baza_lekow", "Baza leków"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("baza_lekow", "Nazwa"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("baza_lekow", "Postać"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("baza_lekow", "Dawka"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("baza_lekow", "Skład"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("baza_lekow", "Refundacja"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("baza_lekow", "Procent ref."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("baza_lekow", "Recepta"))

#####################################################################################

class Ui_Dodaj_lek(object):

    def dodaj(self):
        nazwa       = self.tableWidget.item(0, 0).text()
        postac      = self.tableWidget.item(0, 1).text()
        dawka       = self.tableWidget.item(0, 2).text()
        sklad       = self.tableWidget.item(0, 3).text()
        czy_ref     = self.tableWidget.item(0, 4).text()
        procent_ref = self.tableWidget.item(0, 5).text()
        czy_recepta = self.tableWidget.item(0, 6).text()


        if nazwa != None and postac != None and dawka != None and sklad != None\
                and czy_ref != None and procent_ref != None and czy_recepta != None\
                and (str(procent_ref).isdigit() == True) and int(procent_ref)>=0 and int(procent_ref) <=100\
                and (czy_ref == "t" or czy_ref == "n") and (czy_recepta == "t" or czy_recepta == "n"):

            if procent_ref == "0":
                procent_ref = "NULL"

            try:

                sql = "INSERT INTO leki(nazwa, postac, dawka, sklad, czy_refundowany, procent_refundacji, czy_na_recepte)"\
                      +"VALUES (" + "\"" + str(nazwa) + "\"" + "," + "\"" + str(postac) + "\"" + "," + "\"" + str(dawka) + "\"" \
                      + "," + "\"" + str(sklad) + "\"" + "," + "\"" + str(czy_ref) + "\"" \
                      + "," + str(procent_ref) + "," + "\"" + str(czy_recepta) + "\"" + ")"

                print(sql)

                mycursor.execute(sql)
                mydb.commit()

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Dodano lek")
                msg.setWindowTitle("Dodano lek")
                retval = msg.exec_()
            except:
                print("Error")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Błedne dane.\nSpróbuj ponownie")
            msg.setWindowTitle("Będne dane")
            retval = msg.exec_()


    def setupUi(self, Dodaj_lek):
        Dodaj_lek.setObjectName("Dodaj_lek")
        Dodaj_lek.resize(971, 157)
        self.tableWidget = QtWidgets.QTableWidget(Dodaj_lek)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 961, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.dodaj_pushButton = QtWidgets.QPushButton(Dodaj_lek)
        self.dodaj_pushButton.setGeometry(QtCore.QRect(10, 90, 941, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dodaj_pushButton.setFont(font)
        self.dodaj_pushButton.setObjectName("dodaj_pushButton")

        self.dodaj_pushButton.clicked.connect(self.dodaj)

        self.retranslateUi(Dodaj_lek)
        QtCore.QMetaObject.connectSlotsByName(Dodaj_lek)

    def retranslateUi(self, Dodaj_lek):
        _translate = QtCore.QCoreApplication.translate
        Dodaj_lek.setWindowTitle(_translate("Dodaj_lek", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dodaj_lek", "Nowy lek"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dodaj_lek", "Nazwa"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dodaj_lek", "Postać"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dodaj_lek", "Dawka"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dodaj_lek", "Skład"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dodaj_lek", "Czy ref. (t/n)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dodaj_lek", "Procent ref. [%]"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dodaj_lek", "Recepta [t/n]"))
        self.dodaj_pushButton.setText(_translate("Dodaj_lek", "Dodaj"))

#####################################################################################

class Ui_Oddzialy_NFZ(object):
    def setupUi(self, Oddzialy_NFZ):
        Oddzialy_NFZ.setObjectName("Oddzialy_NFZ")
        Oddzialy_NFZ.resize(322, 669)
        self.tableWidget = QtWidgets.QTableWidget(Oddzialy_NFZ)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 301, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(16)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        row = 0
        try:
            mycursor.execute(
                "SELECT ID_ODDZIALU_NFZ, nazwa from oddzialy_nfz")
            while True:
                sqlRow = mycursor.fetchone()
                if sqlRow == None:
                    break
                print(str(sqlRow))
                for col in range(0, 2):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                row = row + 1
        except:
            print("Error")

        self.retranslateUi(Oddzialy_NFZ)
        QtCore.QMetaObject.connectSlotsByName(Oddzialy_NFZ)

    def retranslateUi(self, Oddzialy_NFZ):
        _translate = QtCore.QCoreApplication.translate
        Oddzialy_NFZ.setWindowTitle(_translate("Oddzialy_NFZ", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Oddzialy_NFZ", "ID Oddziału"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Oddzialy_NFZ", "Nazwa"))

#####################################################################################

class Ui_Wizyty_do_zatwierdzenia(object):


    def zatwierdz_wizyte(self):
        rows = []
        for idx in self.tableWidget.selectionModel().selectedRows():
            rows.append(idx.row())

        print(len(rows))
        for idx in rows:
            try:
                email  = self.tableWidget.item(idx, 3).text()
                cel_wizyty  = self.tableWidget.item(idx, 4).text()
                data = self.tableWidget.item(idx, 5).text()

                sql = "UPDATE wizyty SET czy_zatwierdzona = 1 WHERE cel_wizyty = "+ "\""+str(cel_wizyty)+ "\" AND data = " \
                      + "\"" + str(data) + "\""
                print(sql)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "wpis(y) zatwierdzono")
                send_email.send_confirm_email(str(email), ZALOGOWANY_JAKO, str(data))
                self.tableWidget.removeRow(idx)

            except:
                print("Error")

    def odrzuc_wizyte(self):
        rows = []
        for idx in self.tableWidget.selectionModel().selectedRows():
            rows.append(idx.row())

        for idx in rows:
            try:
                email = self.tableWidget.item(idx, 3).text()
                cel_wizyty = self.tableWidget.item(idx, 4).text()
                data = self.tableWidget.item(idx, 5).text()

                sql = "DELETE FROM wizyty WHERE cel_wizyty = " + "\"" + str(
                    cel_wizyty) + "\" AND data = " \
                      + "\"" + str(data) + "\""
                print(sql)
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "wpis(y) usunięto")
                send_email.send_reject_email(str(email), ZALOGOWANY_JAKO, str(data))
                self.tableWidget.removeRow(idx)

            except:
                print("Error")


    def setupUi(self, Wizyty_do_zatwierdzenia):
        Wizyty_do_zatwierdzenia.setObjectName("Wizyty_do_zatwierdzenia")
        Wizyty_do_zatwierdzenia.resize(808, 453)
        self.tableWidget = QtWidgets.QTableWidget(Wizyty_do_zatwierdzenia)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 791, 341))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        mycursor.execute("SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.nr_tel, pacjenci.adres_email, wizyty.cel_wizyty, wizyty.data FROM\
                            wizyty INNER JOIN pacjenci ON pacjenci.ID_PACJENTA = wizyty.ID_PACJENTA WHERE wizyty.czy_zatwierdzona = 0 AND wizyty.ID_LEKARZA = "\
                            + str(ID_ZALOGOWANEGO_LEKARZA) )

        myresult = mycursor.fetchall()
        print(myresult)
        self.tableWidget.setRowCount(len(myresult))

        row = 0
        try:
            mycursor.execute("SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.nr_tel, pacjenci.adres_email, wizyty.cel_wizyty, wizyty.data FROM\
                                        wizyty INNER JOIN pacjenci ON pacjenci.ID_PACJENTA = wizyty.ID_PACJENTA WHERE wizyty.czy_zatwierdzona = 0 AND wizyty.ID_LEKARZA = " \
                             + str(ID_ZALOGOWANEGO_LEKARZA))
            while True:
                sqlRow = mycursor.fetchone()
                if sqlRow == None:
                    break
                print(str(sqlRow))
                for col in range(0, 6):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                row = row + 1
        except:
            print("Error")

        self.akc_pushButton = QtWidgets.QPushButton(Wizyty_do_zatwierdzenia)
        self.akc_pushButton.setGeometry(QtCore.QRect(70, 370, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.akc_pushButton.setFont(font)
        self.akc_pushButton.setDefault(True)
        self.akc_pushButton.setObjectName("akc_pushButton")
        self.odrzuc_pushButton_2 = QtWidgets.QPushButton(Wizyty_do_zatwierdzenia)
        self.odrzuc_pushButton_2.setGeometry(QtCore.QRect(410, 370, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.odrzuc_pushButton_2.setFont(font)
        self.odrzuc_pushButton_2.setObjectName("odrzuc_pushButton_2")

        self.akc_pushButton.clicked.connect(self.zatwierdz_wizyte)
        self.odrzuc_pushButton_2.clicked.connect(self.odrzuc_wizyte)

        self.retranslateUi(Wizyty_do_zatwierdzenia)
        QtCore.QMetaObject.connectSlotsByName(Wizyty_do_zatwierdzenia)

    def retranslateUi(self, Wizyty_do_zatwierdzenia):
        _translate = QtCore.QCoreApplication.translate
        Wizyty_do_zatwierdzenia.setWindowTitle(_translate("Wizyty_do_zatwierdzenia", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "Imię"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "Nazwisko"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "Nr tel."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "e-mail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "Cel"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Wizyty_do_zatwierdzenia", "Data"))
        self.akc_pushButton.setText(_translate("Wizyty_do_zatwierdzenia", "Akceptuj"))
        self.odrzuc_pushButton_2.setText(_translate("Wizyty_do_zatwierdzenia", "Odrzuć"))

#####################################################################################

class Ui_Pacjent_window(object):

    def aktualizuj_historie(self):
        przebyte    = self.tableWidget.item(0, 0).text()
        przewlekle  = self.tableWidget.item(1, 0).text()
        pobyty      = self.tableWidget.item(2, 0).text()
        zabiegi     = self.tableWidget.item(3, 0).text()
        szczepienia = self.tableWidget.item(4, 0).text()
        uczulenia   = self.tableWidget.item(5, 0).text()
        obiazenia   = self.tableWidget.item(6, 0).text()

        # UPDATE `historie` SET `uczulenia` = 'Sosna' WHERE `historie`.`ID_HISTORII` = 2;
        try:
            sql = "UPDATE historie SET przebyte_choroby = " + "\"" + str(przebyte) + "\"," + \
                                      "przewlekle_choroby = " + "\"" + str(przewlekle) + "\"," + \
                                      "pobyty_w_szpitalu = " + "\"" + str(pobyty) + "\"," + \
                                      "zabeigi = " + "\"" + str(zabiegi) + "\"," + \
                                      "szczepienia = " + "\"" + str(szczepienia) + "\"," + \
                                      "uczulenia = " + "\"" + str(uczulenia) + "\"," + \
                                      "obciazenia = " + "\"" + str(obiazenia) + "\" " +\
                                      "WHERE historie.ID_HISTORII = " + str(ID_HISTORII)
            mycursor.execute(sql)
            mydb.commit()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Zaktualizowano historię choroby")
            msg.setWindowTitle("Operacja się powiodła")
            retval = msg.exec_()
            self.tableWidget.resizeColumnsToContents()


        except:
            print("Error")

    def edytuj_dane_personalne(self):
        self.edytujdanepers = QtWidgets.QMainWindow()
        self.ui = Ui_Dane_pacjenta()
        self.ui.setupUi(self.edytujdanepers)
        self.edytujdanepers.show()

    def usun_pacjenta(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Czy napewno usunąc pacjenta?")
        msg.setWindowTitle("Uwaga!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == 1024:
            try:
                sql = "DELETE FROM pacjenci WHERE ID_PACJENTA = "+str(ID_WYB_PACJENTA)
                mycursor.execute(sql)
                mydb.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Usunięto pacjenta")
                msg.setWindowTitle("Operacja się powiodła")
                retval = msg.exec_()
            except:
                print("Error")

    def pokaz_wizyty(self):
        self.pokazwizyty = QtWidgets.QMainWindow()
        self.ui = Ui_Wizyty()
        self.ui.setupUi(self.pokazwizyty)
        self.pokazwizyty.show()


    def setupUi(self, Pacjent_window):
        Pacjent_window.setObjectName("Pacjent_window")
        Pacjent_window.resize(1029, 505)
        self.centralwidget = QtWidgets.QWidget(Pacjent_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 1001, 331))
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        self.tableWidget.resizeColumnsToContents()
        row = 0
        print(str(ID_WYB_PACJENTA))
        mycursor.execute("SELECT przebyte_choroby, przewlekle_choroby, pobyty_w_szpitalu, zabeigi, szczepienia,\
                            uczulenia, obciazenia, ID_HISTORII FROM historie WHERE historie.ID_PACJENTA = "+ str(ID_WYB_PACJENTA))
        #print(mycursor.fetchall())

        while True:
            sqlRow = mycursor.fetchone()
            if sqlRow == None:
                break
            print(sqlRow)
            for row in range(0, 7):
                if sqlRow[row] == None:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str("Brak")))
                else:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(sqlRow[row])))

            row = row + 1
            global ID_HISTORII
            ID_HISTORII = sqlRow[7]
            print("ID_HIS", ID_HISTORII)

        self.tableWidget.resizeColumnsToContents()
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 60, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Pacjent_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pacjent_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        self.menuDane = QtWidgets.QMenu(self.menubar)
        self.menuDane.setObjectName("menuDane")
        self.menuWizyty = QtWidgets.QMenu(self.menubar)
        self.menuWizyty.setObjectName("menuWizyty")
        Pacjent_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pacjent_window)
        self.statusbar.setObjectName("statusbar")
        Pacjent_window.setStatusBar(self.statusbar)
        self.actionUsu_pacjenta = QtWidgets.QAction(Pacjent_window)
        self.actionUsu_pacjenta.setObjectName("actionUsu_pacjenta")
        self.actionPoka_wizyty = QtWidgets.QAction(Pacjent_window)
        self.actionPoka_wizyty.setObjectName("actionPoka_wizyty")
        self.actionEdytuj = QtWidgets.QAction(Pacjent_window)
        self.actionEdytuj.setObjectName("actionEdytuj")
        self.actionPoka_wszystkie_dane = QtWidgets.QAction(Pacjent_window)
        self.actionPoka_wszystkie_dane.setObjectName("actionPoka_wszystkie_dane")
        self.menuDane.addAction(self.actionPoka_wszystkie_dane)
        self.menuDane.addAction(self.actionUsu_pacjenta)
        self.menuWizyty.addAction(self.actionPoka_wizyty)
        self.menubar.addAction(self.menuDane.menuAction())
        self.menubar.addAction(self.menuWizyty.menuAction())

        self.pushButton.clicked.connect(self.aktualizuj_historie)
        self.actionPoka_wszystkie_dane.triggered.connect(self.edytuj_dane_personalne)
        self.actionUsu_pacjenta.triggered.connect(self.usun_pacjenta)
        self.actionPoka_wizyty.triggered.connect(self.pokaz_wizyty)

        self.retranslateUi(Pacjent_window)
        QtCore.QMetaObject.connectSlotsByName(Pacjent_window)

    def retranslateUi(self, Pacjent_window):

        print(IMIE_I_NAZWISKO_WYB_PACJENTA)
        print(PESEL_pacjenta)

        _translate = QtCore.QCoreApplication.translate
        Pacjent_window.setWindowTitle(_translate("Pacjent_window", "MainWindow"))
        self.label.setText(_translate("Pacjent_window", "Pacjent: "))
        self.label_2.setText(_translate("Pacjent_window", IMIE_I_NAZWISKO_WYB_PACJENTA))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Pacjent_window", "Przebyte horoby"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Pacjent_window", "Przewlekłe horoby"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Pacjent_window", "Pobyty w szpitalu"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Pacjent_window", "Zabiegi"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Pacjent_window", "Szczepienia"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Pacjent_window", "Uczulenia"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Pacjent_window", "Obciążenia"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Pacjent_window", "Opis"))
        self.pushButton.setText(_translate("Pacjent_window", "Aktualizuj histoię"))
        self.label_3.setText(_translate("Pacjent_window", "Historia pacjenta"))
        self.menuDane.setTitle(_translate("Pacjent_window", "Dane"))
        self.menuWizyty.setTitle(_translate("Pacjent_window", "Wizyty"))
        self.actionUsu_pacjenta.setText(_translate("Pacjent_window", "Usuń pacjenta"))
        self.actionPoka_wizyty.setText(_translate("Pacjent_window", "Pokaż wizyty"))
        self.actionEdytuj.setText(_translate("Pacjent_window", "Edytuj"))
        self.actionPoka_wszystkie_dane.setText(_translate("Pacjent_window", "Pokaż wszystkie dane"))

#####################################################################################

class Ui_Dane_pacjenta(object):

    def aktualizuj_dane(self):
        imie          = self.tableWidget.item(0, 0).text()
        nazwisko      = self.tableWidget.item(1, 0).text()
        PESEL         = self.tableWidget.item(2, 0).text()
        plec          = self.tableWidget.item(3, 0).text()
        dataur        = self.tableWidget.item(4, 0).text()
        ulica         = self.tableWidget.item(5, 0).text()
        nr_domu       = self.tableWidget.item(6, 0).text()
        nr_mieszkania = self.tableWidget.item(7, 0).text()
        miasto        = self.tableWidget.item(8, 0).text()
        kod_pocztowy  = self.tableWidget.item(9, 0).text()
        nr_tel        = self.tableWidget.item(10, 0).text()
        email         = self.tableWidget.item(11, 0).text()

        if(imie != None and nazwisko !=None and PESEL != None and len(str(PESEL))==11 and plec!= None\
                and (plec == "k" or plec == "m") and dataur!=None and ulica != None and nr_domu !=None\
                and nr_mieszkania !=None and miasto !=None and kod_pocztowy!=None and nr_tel != None\
                and email != None):
            try:
                sql = "UPDATE pacjenci SET imie = " + "\"" + str(imie) + "\"," + \
                      "nazwisko = " + "\"" + str(nazwisko) + "\"," + \
                      "plec = " + "\"" + str(plec) + "\"," + \
                      "kod_pocztowy = "  + kod_pocztowy + "," + \
                      "ulica = " + "\"" + str(ulica) + "\"," + \
                      "nr_domu = " + "\"" + str(nr_domu) + "\"," + \
                      "nr_mieszkania = " + "\"" + str(nr_mieszkania) + "\"," + \
                      "nr_tel = " + "\"" + str(nr_tel) + "\"," + \
                      "adres_email = " + "\"" + str(email) + "\"," + \
                      "data_urodzenia = " + "\"" + str(dataur) + "\"," + \
                      "PESEL = " + PESEL + "," + \
                      "miejscowosc= " + "\"" + str(miasto) + "\"" + \
                      "WHERE pacjenci.ID_PACJENTA= " + str(ID_WYB_PACJENTA)

                mycursor.execute(sql)
                mydb.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Zaktualizowano dane")
                msg.setWindowTitle("Operacja się powiodła")
                retval = msg.exec_()
                self.tableWidget.resizeColumnsToContents()

            except:
                print("Error aktualizacja danych pacjena")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Błędne dane \nWprowadz poprawne dane")
            msg.setWindowTitle("Błędne dane")
            retval = msg.exec_()
            print("Błędne dane")


    def setupUi(self, Dane_pacjenta):
        Dane_pacjenta.setObjectName("Dane_pacjenta")
        Dane_pacjenta.resize(400, 556)
        self.tableWidget = QtWidgets.QTableWidget(Dane_pacjenta)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()

        row = 0
        mycursor.execute("SELECT imie, nazwisko, PESEL, plec, data_urodzenia, ulica, nr_domu,\
                        nr_mieszkania, miejscowosc, kod_pocztowy, nr_tel, adres_email\
                         FROM pacjenci WHERE ID_PACJENTA = " + str(ID_WYB_PACJENTA) )

        #print(mycursor.fetchall())

        while True:
            sqlRow = mycursor.fetchone()
            if sqlRow == None:
                break
            print(sqlRow)
            for row in range(0, 12):
                if sqlRow[row] == None:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str("Brak")))
                else:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(sqlRow[row])))
            row = row + 1


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton = QtWidgets.QPushButton(Dane_pacjenta)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.aktualizuj_dane)
        self.retranslateUi(Dane_pacjenta)
        QtCore.QMetaObject.connectSlotsByName(Dane_pacjenta)

    def retranslateUi(self, Dane_pacjenta):
        _translate = QtCore.QCoreApplication.translate
        Dane_pacjenta.setWindowTitle(_translate("Dane_pacjenta", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dane_pacjenta", "Imię"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dane_pacjenta", "Nazwisko"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dane_pacjenta", "PESEL"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dane_pacjenta", "Płeć"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dane_pacjenta", "Data urodzenia"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dane_pacjenta", "Ulica"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dane_pacjenta", "Numer domu"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dane_pacjenta", "Numer mieszkania"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dane_pacjenta", "Miasto"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dane_pacjenta", "Kod pocztowy"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dane_pacjenta", "Nr tel."))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dane_pacjenta", "e-mail"))
        self.pushButton.setText(_translate("Dane_pacjenta", "Aktualizuj dane"))

#####################################################################################

class Ui_Wizyty(object):

    def wybierz_wizyte(self):
        global ID_WYBRANEJ_WIZYTY

        for idx in self.tableWidget.selectionModel().selectedIndexes():
            row_number = idx.row()
            print(row_number)

        cel = self.tableWidget.item(row_number, 0).text()
        data = self.tableWidget.item(row_number, 1).text()


        mycursor.execute("SELECT ID_WIZYTY FROM wizyty WHERE data = " + "\"" +str(data)+ "\"" +\
                         " AND cel_wizyty =" + "\"" + str(cel) + "\"")
        print()
        result = mycursor.fetchone()
        ID_WYBRANEJ_WIZYTY = result[0]

        self.opiswizyty = QtWidgets.QMainWindow()
        self.ui = Ui_opisy_wizyty()
        self.ui.setupUi(self.opiswizyty)
        self.opiswizyty.show()


    def setupUi(self, Wizyty):
        Wizyty.setObjectName("Wizyty")
        Wizyty.resize(460, 300)
        self.tableWidget = QtWidgets.QTableWidget(Wizyty)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 451, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        sql = "SELECT cel_wizyty, data FROM wizyty WHERE ID_PACJENTA = " + str(ID_WYB_PACJENTA) + \
                         " AND ID_LEKARZA = " + str(ID_ZALOGOWANEGO_LEKARZA)
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        self.tableWidget.setRowCount(len(myresult))


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        row = 0
        try:
            mycursor.execute("SELECT cel_wizyty, data FROM wizyty WHERE ID_PACJENTA = " + str(ID_WYB_PACJENTA) + \
                                 " AND ID_LEKARZA = " + str(ID_ZALOGOWANEGO_LEKARZA) )
            while True:
                sqlRow = mycursor.fetchone()
                if sqlRow == None:
                    break
                print(str(sqlRow))
                for col in range(0, 2):
                    self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                row = row + 1
        except:
            print("Error")

        self.tableWidget.doubleClicked.connect(self.wybierz_wizyte)
        self.tableWidget.resizeColumnsToContents()
        self.retranslateUi(Wizyty)
        QtCore.QMetaObject.connectSlotsByName(Wizyty)

    def retranslateUi(self, Wizyty):
        _translate = QtCore.QCoreApplication.translate
        Wizyty.setWindowTitle(_translate("Wizyty", "Wykaz wizyt"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Wizyty", "Cel wizyty"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Wizyty", "Data"))

#####################################################################################

class Ui_Statystyki(object):
    def setupUi(self, Statystyki):
        Statystyki.setObjectName("Statystyki")
        Statystyki.resize(400, 114)
        self.label = QtWidgets.QLabel(Statystyki)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ilosc_pajentowlabel_2 = QtWidgets.QLabel(Statystyki)
        self.ilosc_pajentowlabel_2.setGeometry(QtCore.QRect(250, 20, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ilosc_pajentowlabel_2.setFont(font)
        self.ilosc_pajentowlabel_2.setObjectName("ilosc_pajentowlabel_2")

        self.retranslateUi(Statystyki)
        QtCore.QMetaObject.connectSlotsByName(Statystyki)

    def retranslateUi(self, Statystyki):

        mycursor.execute("SELECT COUNT(*) FROM pacjenci")
        result = mycursor.fetchone()

        _translate = QtCore.QCoreApplication.translate
        Statystyki.setWindowTitle(_translate("Statystyki", "Dialog"))
        self.label.setText(_translate("Statystyki", "Ilość pacjentów = "))
        self.ilosc_pajentowlabel_2.setText(_translate("Statystyki", str(result[0])))

#####################################################################################


class Ui_opisy_wizyty(object):
    def setupUi(self, opisy_wizyty):
        opisy_wizyty.setObjectName("opisy_wizyty")
        opisy_wizyty.resize(863, 349)
        self.tableWidget = QtWidgets.QTableWidget(opisy_wizyty)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 841, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        row = 0
        mycursor.execute("SELECT wywiad, rozpoznanie, zalecenia, zalecone_badania, zwolnienia\
                          FROM wizyty WHERE ID_WIZYTY = " + str(ID_WYBRANEJ_WIZYTY))

        # print(mycursor.fetchall())

        while True:
            sqlRow = mycursor.fetchone()
            if sqlRow == None:
                break
            print(sqlRow)
            for row in range(0, 5):
                if sqlRow[row] == None:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str("Brak")))
                else:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(sqlRow[row])))
            row = row + 1



        self.tableWidget.resizeColumnsToContents()
        self.pushButton = QtWidgets.QPushButton(opisy_wizyty)
        self.pushButton.setGeometry(QtCore.QRect(170, 280, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(opisy_wizyty)
        QtCore.QMetaObject.connectSlotsByName(opisy_wizyty)

    def retranslateUi(self, opisy_wizyty):
        _translate = QtCore.QCoreApplication.translate
        opisy_wizyty.setWindowTitle(_translate("opisy_wizyty", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("opisy_wizyty", "Wywiad"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("opisy_wizyty", "Rozpoznanie"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("opisy_wizyty", "Zalecenia"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("opisy_wizyty", "Zlecone badania"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("opisy_wizyty", "Zwolnienia"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("opisy_wizyty", "Opis"))
        self.pushButton.setText(_translate("opisy_wizyty", "Aktualizuj Dane"))


#####################################################################################


#####################################################################################




if __name__ == "__main__":
    import sys


    mydb = mysql.connector.connect(  # struktura potrzebna do laczenia z baza
        host="db4free.net",
        user="root00",
        passwd=haslo.haslo(),  # utworz plik (nie dodawaj na gita) i tam funckje haslo() ktora zaraca haslo
        database="dbgabinet"
    )


    mycursor = mydb.cursor()  # utworzenie kursora potrzebnego do poruszania się po bazie (selecty, inserty itp)
    mycursor.execute("SHOW DATABASES")  # pokazywanie dostepnych baz danych
    for x in mycursor:
        print(x)

    app = QtWidgets.QApplication(sys.argv)
    Logowanie_Window = QtWidgets.QDialog()
    ui = Ui_Logowanie_Window()
    ui.setupUi(Logowanie_Window)
    Logowanie_Window.show()


    sys.exit(app.exec_())
