import sys

try:
    from .dat import DAT
    from .modbus import Modbus
except:
    from dat import DAT
    from modbus import Modbus

from PyQt5 import QtWidgets, QtCore, QtGui
from threading import Thread
from functools import partial

# --  Rescaling della schermata ---------------
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ---------------------------------------------


class Mb_Main:
    def __init__(self):
        self.mb = Modbus()

        self.app = QtWidgets.QApplication(sys.argv)
        ui1 = Thread(target=self.dat())
        ui1.start()

    def dat(self):
        self.main = DAT()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.read_mb_ai)
        timer.start(100)

        for i in range(1, 5):
            button = 'do' + str(i) + '_PB'
            self.main.ui.__getattribute__(button).clicked.connect(partial(self.write_mb_coil,
                                                                          address=15+i,
                                                                          unit=1,
                                                                          button=button))

        self.main.show()
        self.app.exec()

    def read_mb_ai(self):
        try:
            ai = self.mb.read()
            for i in range(1, 9):
                self.main.ui.__getattribute__('i' + str(i) + '_DSB').setValue(ai[i-1]/1000)
        except:
            pass

    def write_mb_coil(self, address, unit, button):
        value = self.main.ui.__getattribute__(button).isChecked()
        self.mb.write_coil(address=address, value=value, unit=unit)


Mb_Main()
