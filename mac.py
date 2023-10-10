import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QMainWindow, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')
        self.check1 = QCheckBox("ЧИЗБУРГЕР", self)
        self.check2 = QCheckBox("Гамбургер", self)
        self.check3 = QCheckBox("Кока-Кола", self)
        self.check4 = QCheckBox("Нагетсы", self)
        self.check1.move(140, 110)
        self.check2.move(140, 130)
        self.check3.move(140, 150)
        self.check4.move(140, 170)
        self.btn = QPushButton('Заказать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(140, 200)
        self.btn.clicked.connect(self.click)

    def click(self):
        self.second_form = SecondForm(self, self.check1.isChecked(), self.check2.isChecked(), self.check3.isChecked(), self.check4.isChecked())
        self.second_form.show()


class SecondForm(QPlainTextEdit):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.plainText = QPlainTextEdit(self)
        if args[1]:
            self.plainText.appendPlainText('ЧИЗБУРГЕР')
        if args[2]:
            self.plainText.appendPlainText('Гамбургер')
        if args[3]:
            self.plainText.appendPlainText("Кока-Кола")
        if args[4]:
            self.plainText.appendPlainText("Нагетсы")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())