import copy
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from UI.mainUI import Ui
from _shared import variables as v
from threading import Thread
from functools import partial
import time

from DAT.modbus import Modbus

# --  Rescaling della schermata ---------------
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


# ---------------------------------------------


class Main:
    def __init__(self):
        # a = v.par
        # self.sel_util = False
        self.fake_on = False
        self.settings_on = False
        self.util = None
        self.sim = None
        self.set = None
        self.mb_set = None
        self.main = None

        self.mb = Modbus()

        self.disp = ['TI221', 'TI222', 'TI223', 'TI224', 'TI225', 'TI306',
                     'PI226', 'PI227', 'PI228', 'PI229', 'PI230', 'PI307',
                     'TT216', 'TT217', 'TT218', 'TT219', 'TT220']

        self.t = 0
        self.t_last = 0
        self.dt = 0
        self.start_t = time.perf_counter()

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

    def open_settings(self):
        from UI.settings.settings import Settings

        # self.app_util = QtWidgets.QApplication([])
        self.set = Settings()
        self.set.show()
        # self.app_util.exec()
        # self.app_util.quit()
        # v.sel_settings = True

    def open_mb_set(self):
        from UI.settings.mb_set import MbSetting
        self.mb_set = MbSetting()
        self.mb_set.show()

    def open_interface(self):
        self.main = Ui()

        self.FC301_activation()

        self.main.ui.EL101_start_PB.clicked.connect(self.EL101_switch)
        self.main.ui.FC301_start_PB.clicked.connect(self.FC301_switch)
        self.main.ui.fake_BTN.clicked.connect(self.fake)
        self.main.ui.settings_BTN.clicked.connect(self.settings)
        self.main.ui.mb_set_BTN.clicked.connect(self.mb_config)

        for valve in ['103', '104', '302', '303']:
            # self.main.ui.EV103_img_LBL.mousePressEvent = partial(self.test, msg=valve)
            self.main.ui.__getattribute__('EV' + valve + '_img_LBL').mouseDoubleClickEvent = \
                partial(self.valve_clicked, valve=valve)
        # self.main.ui.EV103_img_LBL.mouseDoubleClickEvent()

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

    def test(self, event, msg):
        print(msg)

        print('cliccato')

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

    def settings(self):
        # if not self.settings_on:
        if not v.sel_settings:
            f2 = Thread(target=self.open_settings())
            f2.start()
            f2.join()
            # self.settings_on = True
            v.sel_settings = True
        else:
            v.sel_settings = False
            # self.settings_on = False
            self.set.close()

    def mb_config(self):
        if not v.sel_mb:
            f_mbs = Thread(target=self.open_mb_set())
            f_mbs.start()
            f_mbs.join()
            v.sel_mb = True
        else:
            v.sel_mb = False
            self.mb_set.close()

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

    def valve_clicked(self, e, valve):
        v.par['EV'][valve]['val'] = not v.par['EV'][valve]['val']
        self.single_par_to_mb(item=valve)

    def valve_switch(self):
        v.par['EV']['104']['val'] = v.par['EL101']['start']
        v.par['EV']['303']['val'] = v.par['FC301']['start']

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
        if v.par['EV']['104']['val']:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDX_20x20.png"))
        else:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV']['303']['val']:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png"))
        else:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV']['103']['val']:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowUp_20x20.png"))
        else:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

        if v.par['EV']['302']['val']:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDown_20x20.png"))
        else:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

    def refresh(self):
        self.mb_to_par()

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
        # self.main.ui.PI307_DSB.setValue(v.par['PI307']['pressure'])
        # self.main.ui.TI306_DSB.setValue(v.par['TI306']['T'])

        self.main.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301A']['Pread'] + v.par['FC301B']['Pread'])
        self.main.ui.FC301_H2_DSB.setValue(v.par['FC301']['H2'])

        for d in self.disp:
            self.main.ui.__getattribute__(d + '_DSB').setValue(v.par[d]['val'])

        self.valve_draw()
        self.visual_flux()

        self.main.ui.fake_BTN.setChecked(v.sel_util)
        self.main.ui.settings_BTN.setChecked(v.sel_settings)
        self.t = time.perf_counter() - self.start_t
        self.dt = time.perf_counter() - self.t_last
        self.t_last = time.perf_counter()

        self.alarm_check()

        # self.set_params()
        print('refresh \t %.3f\t%.3f' % (self.t, self.dt))

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
        el = v.par['EL101']['start'] and v.par['EL101']['H2'] > 0 and v.par['EL101']['status'] == 'on' \
             and v.par['EV']['104']['val']
        fc = v.par['FC301']['start'] and v.par['FC301A']['H2'] + v.par['FC301B']['H2'] > 0 and \
             (v.par['FC301A']['status'] == 'on' or v.par['FC301B']['status'] == 'on') and v.par['EV']['303']['val']
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

    def alarm_check(self):
        if v.par['EL101']['start'] and v.par['EL101']['Pset'] != 0:
            if v.alarm['EL101']['power']['on'] and \
                    (v.par['EL101']['Pread'] / v.par['EL101']['Pset'] > 1 + v.alarm['EL101']['power']['tr+'] / 100 or
                     v.par['EL101']['Pread'] / v.par['EL101']['Pset'] < 1 - v.alarm['EL101']['power']['tr-'] / 100):
                v.alarm['EL101']['power']['time'] += self.dt
                print('warning EL101 power')
            else:
                v.alarm['EL101']['power']['time'] = 0

            for p in ['pressure', 'H2']:
                if v.alarm['EL101'][p]['on'] and \
                        (v.par['EL101'][p] > v.alarm['EL101'][p]['tr+'] or
                         v.par['EL101'][p] < v.alarm['EL101'][p]['tr-']):
                    v.alarm['EL101'][p]['time'] += self.dt
                    print('warning EL101 ' + p)
                else:
                    v.alarm['EL101'][p]['time'] = 0
        else:
            for p in ['power', 'pressure', 'H2']:
                v.alarm['EL101'][p]['time'] = 0

        self.main.ui.EL101_log_TE.clear()
        for p in ['power', 'pressure', 'H2']:
            if v.alarm['EL101'][p]['time'] > 5:
                self.main.ui.EL101_log_TE.setText(self.main.ui.EL101_log_TE.toPlainText() + 'ERRORE EL101 ' + p + '\n')
            # else:
            #     self.main.ui.EL101_log_TE.clear()

        if v.par['EL101']['start']:
            if v.par['EL101']['Pset'] > 0:
                v.par['EL101']['status'] = 'on'
            else:
                v.par['EL101']['status'] = 'standby'

            for p in ['power', 'pressure', 'H2']:
                if v.alarm['EL101'][p]['time'] > 0:
                    v.par['EL101']['status'] = 'alert'
                    break
            for p in ['power', 'pressure', 'H2']:
                if v.alarm['EL101'][p]['time'] > 5:
                    v.par['EL101']['status'] = 'warning'
                    break
        else:
            v.par['EL101']['status'] = 'off'

    def mb_to_par(self):
        v.mb_conn = True    # se una lettura dal registro fallisce, diventa False

        # Lettura dei segnali analogici
        for ch in [21, 22, 31]:
            regs = self.mb.read(ch=ch)
            for i in range(0, 8):
                v.dat[ch]['reg'][i + 14] = regs[i]

        for d in self.disp:
            ch = v.par[d]['mb']['ch']
            reg = v.par[d]['mb']['reg']
            m = v.par[d]['mb']['scale']
            q = v.par[d]['mb']['offset']
            v.par[d]['val'] = v.dat[ch]['reg'][reg] * m - q

        # TODO: da testare
        # Lettura dei segnali digitali
        for ch in [11, 12, 13, 14]:
            k = list(v.dat[ch]['reg'].keys())
            regs = self.mb.read(ch=ch, reg=0, count=4) + self.mb.read(ch=ch, reg=16, count=4)
            for i in range(0, 8):
                v.dat[ch]['reg'][k[i]] = regs[i]

        # ModBus Led setting
        if v.mb_conn:
            self.main.led_light('mb_statusLed_LBL', 'on')
        else:
            self.main.led_light('mb_statusLed_LBL', 'warning')

    def par_to_mb(self):
        for ch in [11, 12, 13, 14]:
            for reg in [16, 17, 18, 19]:
                self.mb.write_coil(address=reg, value=bool(v.dat[ch]['reg'][reg]), unit=ch)
        pass

    # TODO: Da testare
    def single_par_to_mb(self, item):
        print(v.par['EV'])
        ch = v.par['EV'][item]['mb']['ch']
        reg = v.par['EV'][item]['mb']['reg']
        print('prova scrittura registro ' + str(reg) + ' della unità ' + str(ch))
        self.mb.write_coil(address=reg, value=bool(v.dat[ch]['reg'][reg]), unit=ch)


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
