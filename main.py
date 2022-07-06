import sys
from PyQt5 import QtWidgets

from UI.mainUI import Ui


class Main:
    def __init__(self):
        self.main = None
        self.app = QtWidgets.QApplication([])
        self.open_interface()
        pass

    def open_interface(self):
        self.main = Ui()
        self.main.show()
        self.app.exec()
        self.app.quit()



Main()
