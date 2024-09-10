from PyQt6.QtWidgets import QApplication
from window.MainWindow import MainWindow

import sys # Only needed to access command-line arguments

app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()