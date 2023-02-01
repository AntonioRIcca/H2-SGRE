import copy
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from UI.mainUI import Ui
from _shared import variables as v
from threading import Thread
import time

# --  Rescaling della schermata ---------------
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# ---------------------------------------------


class Main:
    def __init__(self):
        a = v.par
        # self.sel_util = False
        self.fake_on = False
        # self.main = Ui()
        self.app = QtWidgets.QApplication(sys.argv)
        # self.app_util = QtWidgets.QApplication([])

        # f1 = Thread(target=test2)
        # f2 = Thread(target=test)

        # f1 = Thread(target=self.open_util())
        f2 = Thread(target=self.open_interface())

        # f1.start()
        f2.start()

        # self.open_util()
        # self.open_interface()

        pass

    def open_util(self):
        from UI._util.util import Util

        # self.app_util = QtWidgets.QApplication([])
        self.util = Util()
        self.util.show()
        # self.app_util.exec()
        # self.app_util.quit()
        v.sel_util = True

    def open_sim(self):
        from UI._simulation.sim import Sim

        # self.app_util = QtWidgets.QApplication([])
        self.sim = Sim()
        self.sim.show()
        # self.app_util.exec()
        # self.app_util.quit()
        v.sel_util = True

    def open_interface(self):
        self.main = Ui()

        self.FC301_activation()

        self.main.ui.EL101_start_PB.clicked.connect(self.EL101_switch)
        self.main.ui.FC301_start_PB.clicked.connect(self.FC301_switch)
        self.main.ui.fake_BTN.clicked.connect(self.fake)

        # self.main.ui.FC301_Pset_DSB.valueChanged.connect(self.set_params)
        for elem in ['FC301A', 'FC301B', 'FC301', 'EL101']:
            self.main.ui.__getattribute__(elem + '_Pset_DSB').valueChanged.connect(self.set_params)
        for elem in ['FC301_split', 'FC301A_activation', 'FC301B_activation']:
            self.main.ui.__getattribute__(elem + '_CkB').clicked.connect(self.FC301_activation)

        timer = QtCore.QTimer()
        timer.timeout.connect(self.refresh)
        timer.start(1000)

        self.main.show()
        self.app.exec()
        # self.app.quit()

    def EL101_switch(self):
        v.par['EL101']['start'] = self.main.ui.EL101_start_PB.isChecked()
        self.valve_switch()
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

    def fake(self):
        if not self.fake_on:
            f1 = Thread(target=self.open_sim())
            f1.start()
            f1.join()
            self.fake_on = True
        else:
            self.fake_on = False
            self.sim.close()

    def FC301_switch(self):
        v.par['FC301']['start'] = self.main.ui.FC301_start_PB.isChecked()
        self.valve_switch()
        # self.set_params()
        # self.refresh()

        # if self.main.ui.FC301_start_PB.isChecked():
        #     self.main.ui.EL101_start_PB.setText('STOP')
        #     self.main.u3i.FC301A_GB.setEnabled(self.main.ui.FC301A_activation_CkB.isChecked())
        #     self.main.ui.FC301B_GB.setEnabled(self.main.ui.FC301B_activation_CkB.isChecked())
        #     self.main.led_light('FC301A_statusLed_LBL', 'on')
        # else:
        #     self.main.ui.EL101_start_PB.setText('START')

    def FC301_activation(self):
        for elem in ['FC301A', 'FC301B']:
            v.par[elem]['activated'] = self.main.ui.__getattribute__(elem + '_activation_CkB').isChecked()
            self.main.ui.__getattribute__(elem + '_GB').setEnabled(v.par[elem]['activated'])
        # v.par['FC301A']['activated'] = self.main.ui.FC301A_activation_CkB.isChecked()
        # v.par['FC301B']['activated'] = self.main.ui.FC301B_activation_CkB.isChecked()

        self.main.ui.FC301_start_PB.setEnabled(v.par['FC301A']['activated'] or v.par['FC301B']['activated'])
        if self.main.ui.FC301_start_PB.isChecked():
            self.main.ui.FC301_start_PB.setChecked(v.par['FC301A']['activated'] or v.par['FC301B']['activated'])
            v.par['FC301']['start'] = self.main.ui.FC301_start_PB.isChecked()
        self.main.ui.FC301_split_CkB.setEnabled(v.par['FC301A']['activated'] and v.par['FC301B']['activated'])

        if not (v.par['FC301A']['activated'] and v.par['FC301B']['activated']):
            self.main.ui.FC301_split_CkB.setChecked(False)

        self.valve_switch()
        self.set_params()

    def valve_switch(self):
        v.par['EV']['104'] = v.par['EL101']['start']
        v.par['EV']['303'] = v.par['FC301']['start']


        # if v.par['FC301']['start']:
        #     self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png"))
        # else:
        #     self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))
        #
        # if v.par['EL101']['start']:
        #     self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDX_20x20.png"))
        # else:
        #     self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

    def valve_draw(self):
        if v.par['EV']['104']:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDX_20x20.png"))
        else:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV']['303']:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png"))
        else:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV']['103']:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowUp_20x20.png"))
        else:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

        if v.par['EV']['302']:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDown_20x20.png"))
        else:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

    def refresh(self):
        if v.sel_util:
            self.sim.data()

        self.simulation()

        for elem in ['FC301A', 'FC301B']:
            v.par[elem]['H2'] = v.par['FC301']['H2'] * int(v.par[elem]['activated']) * v.par[elem]['Pread'] / \
                                    max((v.par['FC301A']['Pread'] + v.par['FC301B']['Pread']), 0.000001)

        for elem in ['FC301A', 'FC301B', 'EL101']:
            for param in ['Pset', 'Pread', 'H2']:
                self.main.ui.__getattribute__(elem + '_' + param + '_DSB').setValue(v.par[elem][param])
            self.main.led_light(elem + '_statusLed_LBL', v.par[elem]['status'])
            self.main.ui.__getattribute__(elem + '_log_TE').setText(v.par[elem]['log'])

        self.main.ui.FT102_DSB.setValue(v.par['EL101']['H2'])
        self.main.ui.FT308_DSB.setValue(v.par['FC301A']['H2'] + v.par['FC301B']['H2'])
        self.main.ui.PI307_DSB.setValue(v.par['PI307']['pressure'])
        self.main.ui.TI306_DSB.setValue(v.par['TI306']['T'])

        self.main.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301A']['Pread'] + v.par['FC301B']['Pread'])
        self.main.ui.FC301_H2_DSB.setValue(v.par['FC301']['H2'])

        for i in range(1, 6):
            self.main.ui.__getattribute__('PI' + str(i+225) + '_DSB').setValue(v.par['S20' + str(i)]['pressure'])
            self.main.ui.__getattribute__('TI' + str(i+220) + '_DSB').setValue(v.par['S20' + str(i)]['Tflux'])
            self.main.ui.__getattribute__('TT' + str(i+215) + '_DSB').setValue(v.par['S20' + str(i)]['Tvessel'])

        self.valve_draw()
        self.visual_flux()

        self.main.ui.fake_BTN.setChecked(v.sel_util)

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
            self.main.ui.FC301_Pset_DSB.setValue(v.par['FC301A']['Pset'] * int(v.par['FC301A']['activated']) +
                                                 v.par['FC301B']['Pset'] * int(v.par['FC301B']['activated']))

    def visual_flux(self):
        el = v.par['EL101']['start'] and v.par['EL101']['H2'] > 0 and v.par['EL101']['status'] == 'on'
        fc = v.par['FC301']['start'] and (v.par['FC301A']['H2'] + v.par['FC301B']['H2'] > 0) and \
              (v.par['FC301A']['status'] == 'on' or v.par['FC301B']['status'] == 'on')
        self.main.ui.EL101_out_LN.setVisible(el)
        for elem in ['FC301_in', 'mainline3', 'mainline2']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(fc)
        for elem in ['mainline1', 'S201', 'S202', 'S203', 'S204', 'S205']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(el or fc)

    def simulation(self):
        v.par['EL101']['Pread'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['power'] / 100)
        v.par['EL101']['H2'] = v.par['EL101']['Pread'] * 3.3 / 1.2 * 0.06 * v.sim['EL101']['flux'] / 100
        # v.par['EL101']['pressure'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['pressure'] / 100)
        a = []
        for i in ['S201', 'S202', 'S203', 'S204', 'S205']:
            # a.append(self.main.ui.PI226_DSB.value())
            a.append(v.sim[i]['pressure'])
            v.par[i] = copy.deepcopy(v.sim[i])
        v.par['EL101']['pressure'] = max(a) * v.sim['EL101']['pressure'] / 100


def test():
    i = 0
    # i += 1
    # print(i)

    while True:
        i += 1
        print(i)

        # time.sleep(2)


def test2():
    while True:
        print('Test2')
    # print('Test2')
    #     time.sleep(0.7)
#


# def search_MB(index):
    # print(list(v.par['EL101']['mb']['rw'].keys()))



Main()
