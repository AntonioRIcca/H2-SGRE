from .util_UI import Ui_util

from PyQt5 import QtWidgets, QtGui, QtCore
from _shared import variables as v


class Util(QtWidgets.QMainWindow):
    def __init__(self):
        super(Util, self).__init__()
        self.ui = Ui_util()
        self.ui.setupUi(self)

        cycle = QtCore.QTimer()
        cycle.timeout.connect(self.data)
        cycle.start(500)

    def data(self):
        v.par['EL101']['H2'] = self.ui.doubleSpinBox.value()
        v.par['EL101']['Pread'] = self.ui.doubleSpinBox_2.value()

