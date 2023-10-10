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
        self.btn = QPushButton('+', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(140, 110)
        self.btn.clicked.connect(self.click)
        self.btn1 = QPushButton('-', self)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.move(200, 110)
        self.btn1.clicked.connect(self.click1)
        self.btn2 = QPushButton('*', self)
        self.btn2.resize(self.btn.sizeHint())
        self.btn2.move(270, 110)
        self.btn2.clicked.connect(self.click2)
        self.label = QLabel(self)
        self.name_input = QLineEdit(self)
        self.name_input.move(0, 90)
        self.name_input.setText("0")
        self.name_input1 = QLineEdit(self)
        self.name_input1.move(0, 150)
        self.name_input1.setText("0")
        self.name_input2 = QLineEdit(self)
        self.name_input2.move(0, 200)
        self.name_input2.setReadOnly(True)


    def click(self):
        self.name_input2.setText(str(int(self.name_input1.text()) + int(self.name_input.text())))

    def click1(self):
        self.name_input2.setText(str(int(self.name_input1.text()) - int(self.name_input.text())))

    def click2(self):
        self.name_input2.setText(str(int(self.name_input1.text()) * int(self.name_input.text())))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())