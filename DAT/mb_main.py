import sys

try:
    from .datexel import Datexel
    # from .dat import DAT
    # from .modbus import Modbus
except:
    from datexel import Datexel
    # from dat import DAT
    # from modbus import Modbus

from _shared import variables as v
from PyQt5 import QtWidgets, QtCore, QtGui
from threading import Thread
from functools import partial

import modbus

# --  Rescaling della schermata ---------------
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ---------------------------------------------


class ModbusMain:
    def __init__(self):
        # self.mb = Modbus()
        self.v = 1
        self.mb = modbus.Modbus()

        self.app = QtWidgets.QApplication(sys.argv)
        ui1 = Thread(target=self.datexel())
        ui1.start()
        print('4')

    def datexel(self):
        self.main = Datexel()
        timer = QtCore.QTimer()
        timer.timeout.connect(self.refresh)
        timer.start(500)

        print(1)
        self.main.show()
        print(2)
        self.app.exec()
        print(3)

    def refresh(self):
        # self.v +=1
        # self.main.ui.i3017_21_0_DSB.setValue(self.v)
        print('refresh')
        self.mb_read()

        for ch in [21, 22, 31]:
            for reg in range(14,22):
                # self.main.ui.i3017_21_1_DSB.setValue(v.dat[ch]['reg'][reg])
                dsb = v.dat[ch]['signal'] +\
                      v.dat[ch]['mod'] + '_' + str(ch) + '_' + str(reg-14) + '_DSB'
                # print(dsb)
                self.main.ui.__getattribute__(dsb).setValue(v.dat[ch]['reg'][reg])

    def mb_read(self):
        for ch in [21, 22, 31]:
            regs = self.mb.read(ch=ch)
            print(regs)
            for i in range(0, 8):
                v.dat[ch]['reg'][14+i] = regs[i] / 1000
        pass

    # def dat(self):
    #     self.main = DAT()
    #
    #     timer = QtCore.QTimer()
    #     timer.timeout.connect(self.read_mb_ai)
    #     timer.start(100)
    #
    #     for i in range(1, 5):
    #         button = 'do' + str(i) + '_PB'
    #         self.main.ui.__getattribute__(button).clicked.connect(partial(self.write_mb_coil,
    #                                                                       address=15+i,
    #                                                                       unit=1,
    #                                                                       button=button))
    #
    #     self.main.show()
    #     self.app.exec()

    # def read_mb_ai(self):
    #     try:
    #         ai = self.mb.read()
    #         for i in range(1, 9):
    #             self.main.ui.__getattribute__('i' + str(i) + '_DSB').setValue(ai[i-1]/1000)
    #     except:
    #         pass

    # def write_mb_coil(self, address, unit, button):
    #     value = self.main.ui.__getattribute__(button).isChecked()
    #     self.mb.write_coil(address=address, value=value, unit=unit)


ModbusMain()
