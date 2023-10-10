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
        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(160, 110)
        self.btn.clicked.connect(self.change)
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
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(300, 90)
        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(300, 120)
        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(300, 150)
        self.LCD_count4 = QLCDNumber(self)
        self.LCD_count4.move(300, 180)

    def change(self):
        self.first_data = self.name_input.text()
        self.second_data = self.self.name_input1.text()
        self.first_number = int(self.first_data)
        self.second_number = int(self.second_data)

        self.result1 = self.first_number + self.second_number
        self.result2 = self.first_number - self.second_number
        self.result3 = self.first_number * self.second_number

        if self.second_number != 0:
            self.result4 = round(self.first_number / self.second_number, 3)
        else:
            self.result4 = 'Error'

        self.LCD_count.display(self.result1)
        self.LCD_count1.display(self.result2)
        self.LCD_count2.display(self.result3)
        self.LCD_count4.display(self.result4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())