import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTextEdit


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("delsql.ui", self)
        self.con = sqlite3.connect("films_db.sqlite")
        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.delete_elem)
        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        if len(self.textEdit.toPlainText()) != 0:
            result = cur.execute("SELECT * FROM films WHERE " + self.textEdit.toPlainText()).fetchall()
        else:
            result = cur.execute("SELECT * FROM films").fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def delete_elem(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
        cur.execute("DELETE FROM films WHERE id IN (" + ", ".join(
            '?' * len(ids)) + ")", ids)
        self.con.commit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
