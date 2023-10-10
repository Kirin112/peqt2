import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QTimeEdit
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dates = []
        uic.loadUi('check.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.delete)

    def run(self):
        self.listWidget.clear()
        d = self.calendarWidget.selectedDate()
        form_d = d.toString("yyyy-MM-dd")
        t = self.timeEdit.time()
        form_t = t.toString()
        self.dates.append(f"{form_d} {form_t} - {self.lineEdit.text()}")
        print(self.dates)
        self.dates = sorted(self.dates)
        for date in self.dates:
            self.listWidget.addItem(date)

    def delete(self):
        self.listWidget.clear()
        self.dates = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())