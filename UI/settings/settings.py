from .settings_UI import Ui_settings

from PyQt5 import QtWidgets, QtGui, QtCore
from _shared import variables as v


class Settings(QtWidgets.QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.set_data()

        self.ui.ok_PB.clicked.connect(self.data)
        self.ui.cancel_PB.clicked.connect(self.close_window)

        # cycle = QtCore.QTimer()
        # cycle.timeout.connect(self.data)
        # cycle.start(500)

    def data(self):
        for elem in ['EL101']:
            for p in ['power', 'pressure', 'H2']:
                v.alarm[elem][p]['tr+'] = self.ui.__getattribute__(elem + '_' + p + '_max_DSB').value()
                v.alarm[elem][p]['tr-'] = self.ui.__getattribute__(elem + '_' + p + '_min_DSB').value()
                v.alarm[elem][p]['on'] = self.ui.__getattribute__(elem + '_' + p + '_act_CkB').isChecked()

        self.close_window()

    def set_data(self):
        for elem in ['EL101']:
            for p in ['power', 'pressure', 'H2']:
                # self.ui.EL101_P_max_DSB.setValue(v.alarm[elem][p]['tr+'])
                self.ui.__getattribute__(elem + '_' + p + '_max_DSB').setValue(v.alarm[elem][p]['tr+'])
                self.ui.__getattribute__(elem + '_' + p + '_min_DSB').setValue(v.alarm[elem][p]['tr-'])
                self.ui.__getattribute__(elem + '_' + p + '_act_CkB').setChecked(v.alarm[elem][p]['on'])
                # self.ui.EL101_P_act_DSB.setChecked()

        # self.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        # self.ui.EL101_H2_DSB.setValue(v.par['EL101']['H2'])
        # self.ui.TI306_T_DSB.setValue(v.par['TI306']['T'])
        # self.ui.PI307_pressure_DSB.setValue(v.par['PI307']['pressure'])
        # self.ui.FC301_H2_DSB.setValue(v.par['FC301']['H2'])
        # for i in range(1, 6):
        #     for param in ['pressure', 'Tflux', 'Tvessel']:
        #         self.ui.__getattribute__('S20' + str(i) + '_' + param + '_DSB').setValue(v.par['S20' + str(i)][param])
        # for valve in ['104', '103', '302', '303']:
        #     self.ui.__getattribute__('EV' + valve + '_CkB').setChecked(v.par['EV'][valve])

    def closeEvent(self, event):
        print('Chiuso')
        v.sel_settings = False

    def close_window(self):
        self.close()
