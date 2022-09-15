try:
    from .dat_ui import Ui_dat
    from .modbus import Modbus
except:
    from dat_ui import Ui_dat
    from modbus import Modbus

import time


from PyQt5 import QtWidgets, QtGui, QtCore
from _shared import variables as v

# --  Rescaling della schermata ---------------
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ---------------------------------------------


class DAT(QtWidgets.QMainWindow):
    def __init__(self):
        super(DAT, self).__init__()
        self.ui = Ui_dat()
        self.ui.setupUi(self)
        self.mb = Modbus()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.read_ai_mb)
        timer.start(1000)
        # while True:
        #     # self.read_ai_mb()
        #     time.sleep(1)

    def read_ai_mb(self):
        ai = self.mb.read()
        for i in range(0, 8):
            self.ui.__getattribute__('i' + str(i) + '_DSB').setValue(ai[i])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dat = QtWidgets.QMainWindow()
    myui = DAT()
    myui.ui.setupUi(dat)
    dat.show()
    app.exec_()
    print('exec')
    sys.exit()
