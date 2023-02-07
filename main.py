from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import sqlite3



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sql')
        self.cur = self.connection.cursor()
        self.resize(1800, 800)
        self.tableWidget.resize(1600, 700)
        self.update()
        
        
        self.show()
    def update(self):
        table = self.tableWidget
        #table.setRowCount(len(colors))
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["ID", "название сорта", "степень обжарки", "обработка", "описание вкуса", "цена", "объем упаковки"])
        self.cur.execute('SELECT * from coffee')
        #table.setItem(i, 0, item_name)
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
        print(data)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui()
    ex.show()
    sys.exit(app.exec_())

