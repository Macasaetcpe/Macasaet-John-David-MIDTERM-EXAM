import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 450
        self.y = 150
        self.width = 500
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.textboxlbl2 = QLabel("Enter your Fullname: ", self)
        self.textboxlbl2.setStyleSheet("color: red;")
        self.textboxlbl2.move(45, 75)

        # First Name input
        self.fname_input = QLineEdit(self)
        self.fname_input.move(250, 70)
        self.fname_input.resize(200, 25)

        self.button = QPushButton('Click to display your Fullname', self)
        self.button.setStyleSheet("color: red;")
        self.button.move(45, 120) # button.move(x,y)
        self.button.clicked.connect(self.display_fullname)

        # Last Name input
        self.lname_input = QLineEdit(self)
        self.lname_input.move(250, 120)
        self.lname_input.resize(200, 25)

        # Display the window
        self.show()

    @pyqtSlot()
    def display_fullname(self):
        text = self.fname_input.text()
        self.lname_input.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())