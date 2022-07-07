import sys
from PyQt5 import QtWidgets, QtCore

from UI.mainUI import Ui
from _shared import variables as v


class Main:
    def __init__(self):
        # self.main = Ui()
        self.app = QtWidgets.QApplication([])

        self.open_interface()
        pass

    def open_interface(self):
        self.main = Ui()

        self.main.ui.EL101_start_PB.clicked.connect(self.EL101_switch)
        self.main.ui.FC301_start_PB.clicked.connect(self.FC301_switch)

        # self.main.ui.FC301_Pset_DSB.valueChanged.connect(self.set_params)
        for elem in ['FC301A', 'FC301B', 'FC301', 'EL101']:
            self.main.ui.__getattribute__(elem + '_Pset_DSB').valueChanged.connect(self.set_params)

        timer = QtCore.QTimer()
        timer.timeout.connect(self.refresh)
        # timer.start(500)

        self.main.show()
        self.app.exec()
        self.app.quit()

    def EL101_switch(self):
        v.par['EL101']['start'] = self.main.ui.EL101_start_PB.isChecked()
        # self.set_params()
        # self.refresh()
        # v.par['EL101']['status'] = 'on'     # Todo: Da spostare

        # if self.main.ui.EL101_start_PB.isChecked():
        #     self.main.ui.EL101_start_PB.setText('STOP')
        #     self.main.led_light('EL101_statusLed_LBL', 'on')
        #     print('Start EL101')
        # else:
        #     self.main.ui.EL101_start_PB.setText('START')
        #     self.main.led_light('EL101_statusLed_LBL', 'off')
        #     print('Stop EL101')
        # for line in ['EL101_out', 'S201', 'S202', 'S203', 'S204', 'S205', 'mainline1']:
        #     self.main.ui.__getattribute__(line + '_LN').setVisible(self.main.ui.EL101_start_PB.isChecked())

    def FC301_switch(self):
        v.par['FC301']['start'] = self.main.ui.FC301_start_PB.isChecked()
        self.set_params()
        # self.refresh()

        # if self.main.ui.FC301_start_PB.isChecked():
        #     self.main.ui.EL101_start_PB.setText('STOP')
        #     self.main.u3i.FC301A_GB.setEnabled(self.main.ui.FC301A_activation_CkB.isChecked())
        #     self.main.ui.FC301B_GB.setEnabled(self.main.ui.FC301B_activation_CkB.isChecked())
        #     self.main.led_light('FC301A_statusLed_LBL', 'on')
        # else:
        #     self.main.ui.EL101_start_PB.setText('START')

    def refresh(self):
        for elem in ['FC301A', 'FC301B', 'EL101']:
            for param in ['Pset', 'Pread', 'H2']:
                self.main.ui.__getattribute__(elem + '_' + param + '_DSB').setValue(v.par[elem][param])
                self.main.led_light(elem + '_statusLed_LBL', v.par[elem]['status'])
                self.main.ui.__getattribute__(elem + '_log_TE').setText(v.par[elem]['log'])
        self.main.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301A']['Pread'] + v.par['FC301B']['Pread'])
        # self.set_params()
        print('refresh')

    def set_params(self):
        print('set params')
        for elem in ['FC301A', 'FC301B', 'EL101']:
            v.par[elem]['Pset'] = self.main.ui.__getattribute__(elem + '_Pset_DSB').value()
        v.par['FC301A']['activated'] = self.main.ui.FC301A_activation_CkB.isChecked()
        v.par['FC301B']['activated'] = self.main.ui.FC301B_activation_CkB.isChecked()
        v.par['FC301']['split'] = self.main.ui.FC301_split_CkB.isChecked()
        if self.main.ui.FC301_split_CkB.isChecked():
            for elem in ['FC301A', 'FC301B']:
                v.par[elem]['Pset'] = self.main.ui.FC301_Pset_DSB.value() / 2
                self.main.ui.__getattribute__(elem + '_Pset_DSB').setValue(v.par[elem]['Pset'])
            # v.par['FC301A']['Pset'] = self.main.ui.FC301_Pset_DSB.value() / 2
            # v.par['FC301B']['Pset'] = self.main.ui.FC301_Pset_DSB.value() / 2
        else:
            v.par['FC301A']['Pset'] = self.main.ui.FC301A_Pset_DSB.value()
            v.par['FC301B']['Pset'] = self.main.ui.FC301B_Pset_DSB.value()
            self.main.ui.FC301_Pset_DSB.setValue(v.par['FC301A']['Pset'] + v.par['FC301B']['Pset'])



Main()
