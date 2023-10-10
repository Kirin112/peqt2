import sys
from PyQt5 import uic # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QApplication
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('sex.png'))

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def run(self):
        self.label.setText("OK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())