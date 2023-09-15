from .sim_UI import Ui_sim

from PyQt5 import QtWidgets, QtGui, QtCore
from _shared import variables as v


class Sim(QtWidgets.QMainWindow):
    def __init__(self):
        super(Sim, self).__init__()
        self.ui = Ui_sim()
        self.ui.setupUi(self)
        self.set_data()

        print('sim.py')

        cycle = QtCore.QTimer()
        cycle.timeout.connect(self.data)
        cycle.start(500)

    def data(self):
        for elem in ['EL101', 'FC301A', 'FC301B']:
            try:
                y = int(v.par[elem]['activated'])
            except:
                y = 1
            v.par[elem]['Pread'] = self.ui.__getattribute__(elem + '_P_DSB').value() * y
            # v.par[elem]['status'] = self.ui.__getattribute__(elem + '_status_CB').currentText()
        v.par['EL101']['pressure'] = self.ui.EL101_pressure_DSB.value()
        v.par['EL101']['H2'] = self.ui.EL101_H2_DSB.value()
        v.par['TI306']['T'] = self.ui.TI306_T_DSB.value()
        v.par['PI307']['pressure'] = self.ui.PI307_pressure_DSB.value()
        v.par['FC301']['H2'] = self.ui.FC301_H2_DSB.value()
        # for i in range(1, 6):
        #     for param in ['pressure', 'Tflux', 'Tvessel']:
        #         v.par['S20' + str(i)][param] = self.ui.__getattribute__('S20' + str(i) + '_' + param + '_DSB').value()
        # for valve in ['104', '103', '302', '303']:
        #     v.par['EV'][valve] = self.ui.__getattribute__('EV' + valve + '_CkB').isChecked()
        #
        p = v.par['FC301A']['Pread'] + v.par['FC301B']['Pread']
        if p != 0:
            for elem in ['FC301A', 'FC301B']:
                v.par[elem]['H2'] = v.par['FC301']['H2'] * v.par[elem]['Pread'] / p
        v.sim['EL101']['power'] = self.ui.EL101_P_DSB.value()
        v.sim['EL101']['pressure'] = self.ui.EL101_pressure_DSB.value()
        v.sim['EL101']['flux'] = self.ui.EL101_H2_DSB.value()

        for i in ['S201', 'S202', 'S203', 'S204', 'S205']:
            for t in ['pressure', 'Tflux', 'Tvessel']:
                # v.sim[i] = self.ui.S201_Tflux_DSB
                v.sim[i][t] = self.ui.__getattribute__(i + '_' + t + '_DSB').value()
        pass

    def set_data(self):
        for elem in ['EL101', 'FC301A', 'FC301B']:
            # self.ui.__getattribute__(elem + '_P_DSB').setValue(v.par[elem]['Pread'])
            self.ui.__getattribute__(elem + '_status_CB').setCurrentText(v.par[elem]['status'])
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

        # self.ui.EL101_H2_DSB.setValue(v.par['EL101']['mb']['r']['Flow']['val'] * 3600/1e-6)

        self.ui.EL101_P_DSB.setValue(v.sim['EL101']['power'])
        self.ui.EL101_pressure_DSB.setValue(v.sim['EL101']['pressure'])
        self.ui.EL101_H2_DSB.setValue(v.sim['EL101']['flux'])

        for i in ['S201', 'S202', 'S203', 'S204', 'S205']:
            for t in ['pressure', 'Tflux', 'Tvessel']:
                self.ui.__getattribute__(i + '_' + t + '_DSB').setValue(v.sim[i][t])

    def closeEvent(self, event):
        print('Chiuso')
        v.sel_util = False