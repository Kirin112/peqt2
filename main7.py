import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Шестая программа')
        self.btn = QPushButton('->', self)
        self.btn.move(0, 150)
        self.btn.clicked.connect(self.change)
        self.name_input = QLineEdit(self)
        self.name_input.move(0, 90)
        self.name_input1 = QLineEdit(self)
        self.name_input1.move(150, 90)

    def change(self):
        if self.btn.text() == "->":
            self.btn.setText("<-")
            self.name_input1.setText(self.name_input.text())
            self.name_input.setText('')
        else:
            self.btn.setText("->")
            self.name_input.setText(self.name_input1.text())
            self.name_input1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())