from PySide6.QtWidgets import  (QMainWindow, QPushButton, QApplication, QLabel, QToolBar, QStatusBar)
from PySide6.QtWidgets import QMenuBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Title")
        button = QPushButton("Press Me")

        self.setCentralWidget(button)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        toolbar = QToolBar("My Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

    def quit_app(self):
        self.app.quit()