import sys
from window import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
