from PyQt5.QtWidgets import QSlider
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import  Qt
import sys
from button_holder import ButtonHolder

app = QApplication(sys.argv)

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


window = ButtonHolder()
window.show()

app.exec()

''' Version 1: Everything in global scope
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My First App!)

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()
'''
''' Version 2: Setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Title")
        button = QPushButton("Press Me")
        
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()
'''

