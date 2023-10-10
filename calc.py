import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')
        self.btn = QPushButton('gecr', self)
        self.btn.move(160, 110)
        self.btn.clicked.connect(self.click)
        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(0, 70)
        self.label = QLabel(self)
        self.label.setText("Второе число(целое):")
        self.label.move(0, 130)
        self.name_input = QLineEdit(self)
        self.name_input.move(0, 90)
        self.name_input1 = QLineEdit(self)
        self.name_input1.move(0, 150)
        self.count = QLCDNumber(self)
        self.count.move(300, 90)
        self.count1 = QLCDNumber(self)
        self.count1.move(300, 120)
        self.count2 = QLCDNumber(self)
        self.count2.move(300, 150)
        self.count4 = QLCDNumber(self)
        self.count4.move(300, 180)

    def click(self):
        self.first_data = self.name_input.text()
        self.second_data = self.name_input1.text()
        self.first_number = int(self.first_data)
        self.second_number = int(self.second_data)

        self.result1 = self.first_number + self.second_number
        self.result2 = self.first_number - self.second_number
        self.result3 = self.first_number * self.second_number

        if self.second_number != 0:
            self.result4 = round(self.first_number // self.second_number, 3)
        else:
            self.result4 = 'Error'

        self.count.display(int(self.result1))
        self.count1.display(int(self.result2))
        self.count2.display(int(self.result3))
        self.count4.display(int(self.result4))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())