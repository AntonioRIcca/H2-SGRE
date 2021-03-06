import sys
from .main_window import Ui_main_window

from PyQt5 import QtWidgets, QtGui

import yaml


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.ui.pID_LBL.setPixmap(QtGui.QPixmap("UI/_resources/P&ID_1500x900.png"))

        for element in ['FC301A', 'FC301B', 'EL101', 'S201', 'S202', 'S203', 'S204', 'S205']:
            self.led_light(element + '_statusLed_LBL', 'off')

        for element in ['EL101_out', 'EV103', 'EV302', 'FC301_in', 'S201', 'S202', 'S203', 'S204', 'S205',
                        'mainline1', 'mainline2', 'mainline3', 'vent']:
            self.ui.__getattribute__(element + '_LN').setVisible(False)
        self.valve_stop_img()

    def led_light(self, led, status):
        leds = {
            'off': 'Led-OFF_20x20.png',
            'on': 'Led-Green_20x20.png',
            'alert': 'Led-Yellow_20x20.png',
            'warning': 'Led-Red_20x20.png',
            'standby': 'Led-Blue_20x20.png',
        }

        try:
            self.ui.__getattribute__(led).setPixmap(QtGui.QPixmap("UI/_resources/" + leds[status]))
        except:
            print(led + ': Status led non riconosciuto')

    def valve_stop_img(self):
        for element in ['V104', 'V303']:
            self.ui.__getattribute__(element + '_img_LBL').setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_50x20"))
        self.ui.V103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSu_20x50.png"))
        self.ui.V302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowGiu_20x50.png"))
