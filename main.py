from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Second(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 701, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "id"))
        self.label_2.setText(_translate("Form", "сорт"))
        self.label_3.setText(_translate("Form", "обжарка"))
        self.label_4.setText(_translate("Form", "вид"))
        self.label_5.setText(_translate("Form", "описание вкуса"))
        self.label_6.setText(_translate("Form", "цена"))
        self.label_7.setText(_translate("Form", "объем"))
        self.pushButton.setText(_translate("Form", "Сохранить"))

class Main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 333)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 471, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 141, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить кофе"))

class Add(QtWidgets.QMainWindow, Second):
    def __init__(self, window):
        super(Add, self).__init__() 
        self.windoww = window
        self.setupUi(self)
        self.connection = sqlite3.connect('data\coffee.sql')
        self.cur = self.connection.cursor()
        self.label_8.setText("")
        self.pushButton.clicked.connect(self.click)
    def click(self):
        id = self.lineEdit.text()
        degree = self.lineEdit_3.text().lower()
        state = self.lineEdit_4.text().lower()
        taste = self.lineEdit_5.text().lower()
        price = self.lineEdit_6.text().lower()
        volume = self.lineEdit_7.text().lower()
        srt = self.lineEdit_2.text()
        if degree == 'светлая':
            degree ='0'
        elif degree == 'средняя':
            degree = '1'
        elif degree == 'тёмная' or degree == 'темная':
            degree == '2'
        else:
            degree = ''
        if state == 'молотый':
            state = '1'
        elif state == 'в зёрнах' or state == 'в зернах':
            state = '0'
        else:
            state = ''
        if id:
            if degree:
                self.cur.execute(f"""Update coffee set degree="{degree}" where id = {id}""")
            if state:
                self.cur.execute(f"""Update coffee set state="{state}" where id = {id}""")
            if taste:
                self.cur.execute(f"""Update coffee set taste="{taste}" where id = {id}""")
            if price:
                self.cur.execute(f"""Update coffee set price="{price}" where id = {id}""")
            if srt:
                self.cur.execute(f"""Update coffee set name="{srt}" where id = {id}""")
            if volume:
                self.cur.execute(f"""Update coffee set volume="{volume}" where id = {id}""")
            self.label_8.setText("Сохранено")
            self.connection.commit()
        else:
            if degree and state and taste and price and volume and srt:
                self.label_8.setText("Сохранено")
                command = f"""insert into coffee (name, degree, state, taste, price, volume)
                 values ( "{srt}", "{degree}", "{state}", "{taste}", "{price}", "{volume}")"""
                self.cur.execute(command)
                self.connection.commit()
            else:
                pass
                self.label_8.setText("Ошибка ввода")
        self.windoww.update()

class Ui(QtWidgets.QMainWindow, Main):
    def __init__(self):
        super(Ui, self).__init__() 
        self.setupUi(self)
        self.connection = sqlite3.connect('data\coffee.sql')
        self.cur = self.connection.cursor()
        self.resize(1800, 800)
        self.tableWidget.resize(1600, 700)
        self.pushButton.clicked.connect(self.click)
        self.update()
        self.show()
    def click(self):
        self.ex = Add(self)
        self.ex.show()
    def update(self):
        table = self.tableWidget
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["ID", "название сорта", "степень обжарки", "обработка", "описание вкуса", "цена", "объем упаковки"])
        self.cur.execute('SELECT * from coffee')
        data = self.cur.fetchall()
        table.setRowCount(len(data))
        for i, g in enumerate(data):
            for j, k in enumerate(g):
                if j == 2: #степень
                    if k == 0:
                        degree = 'светлая'
                    elif k == 1:
                        degree = 'средняя'
                    elif k == 2:
                        degree = 'тёмная'
                    table.setItem(i, j, QTableWidgetItem(degree))
                elif j == 3:
                    if k == 0:
                        state = 'в зернах'
                    else:
                        state = 'молотый'
                    table.setItem(i, j, QTableWidgetItem(state))
                else:
                    table.setItem(i, j, QTableWidgetItem(str(k)))

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui()
    ex.show()
    sys.exit(app.exec_())

