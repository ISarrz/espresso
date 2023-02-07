from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import sqlite3

class Add(QtWidgets.QMainWindow):
    def __init__(self, window):
        super(Add, self).__init__() 
        self.windoww = window
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connection = sqlite3.connect('coffee.sql')
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

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sql')
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

