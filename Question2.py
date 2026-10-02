import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()  # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "Special Midterm Exam in OOP"
        self.x = 450  # or left
        self.y = 260  # or top
        self.width = 350
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('Feather.ico'))

        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click to Change Color', self)
        self.button.move(115, 115)  # button.move(x, y)
        # connect the button's clicked signal to on_click()
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print("You clicked me!")
        self.button.setStyleSheet("background-color: yellow;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())