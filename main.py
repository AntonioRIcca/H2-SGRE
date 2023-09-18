import copy
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from UI.mainUI import Ui
from _shared import variables as v
from threading import Thread
from functools import partial
import time
import datetime

import sqlite3

from DAT.modbus import Modbus

# --  Rescaling della schermata ---------------
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------------------------


class Main:
    def __init__(self):
        # self.fake_on = False
        # self.settings_on = False
        # self.util = None

        # Inizializzazione delle variabili delle finestre
        self.sim = None
        self.set = None
        self.mb_set = None
        self.main = None

        self.mb = Modbus()

        # elenco delle caselle DSB collegate alle schede analogiche ModBus
        self.disp = ['TI221', 'TI222', 'TI223', 'TI224', 'TI225', 'TI306',
                     'PI226', 'PI227', 'PI228', 'PI229', 'PI230', 'PI307',
                     'TT216', 'TT217', 'TT218', 'TT219', 'TT220']

        # elenco delle elettrovalvole
        self.valves = ['EV103', 'EV104', 'EV302', 'EV303']

        # Inizializzazione delle variabili del timer
        self.t = 0          # tempo relativo dall'avvio del software
        self.t_last = 0     # tempo assoluto alla fine del ciclo precendente
        self.dt = 0         # durata del ciclo
        self.start_t = time.perf_counter()      #tempo assoluto dell'avvio del softare

        self.db_init()

        # self.main = Ui()
        self.app = QtWidgets.QApplication(sys.argv)

        f0 = Thread(target=self.interface_open())
        f0.start()
        pass

    # def open_util(self):
    #     from UI._util.util import Util
    #
    #     print('Open Util')
    #
    #     # self.app_util = QtWidgets.QApplication([])
    #     self.util = Util()
    #     self.util.show()
    #     # self.app_util.exec()
    #     # self.app_util.quit()
    #     v.sel_util = True

    def db_init(self):
        try:
            os.remove('_database/dati.db')
        except:
            pass

        now = datetime.datetime.now()
        dbname = now.strftime('%Y%m%d_%H%M%S') + '.db'
        print(dbname)

        self.conn = sqlite3.connect('_database/' + dbname)

        self.c = self.conn.cursor()
        #
        # self.c.execute('CREATE TABLE IF NOT EXISTS EL101('
        #                'time REAL, '
        #                'power REAL,'
        #                'pressure REAL,'
        #                'flux REAL,'
        #                'status TEXT)')

        for elem in ['EL101', 'FC301A', 'FC301B']:
            self.c.execute('CREATE TABLE IF NOT EXISTS ' + elem + '('
                           'time REAL, '
                           'power REAL,'
                           'pressure REAL, '
                           'flux REAL,'
                           'status TEXT)')

        self.c.execute('CREATE TABLE IF NOT EXISTS valves('
                       'time REAL, '
                       'EV103 TEXT,'
                       'EV104 TEXT,'
                       'EV302 TEXT,'
                       'EV303 TEXT)')

        self.c.execute('CREATE TABLE IF NOT EXISTS pressures('
                       'time REAL, '
                       'PI226 REAL,'
                       'PI227 REAL,'
                       'PI228 REAL,'
                       'PI229 REAL,'
                       'PI230 REAL,'
                       'PI307 REAL)')

        self.c.execute('CREATE TABLE IF NOT EXISTS temperatures('
                       'time REAL, '
                       'TI221 REAL,'
                       'TI222 REAL,'
                       'TI223 REAL,'
                       'TI224 REAL,'
                       'TI225 REAL,'
                       'TI306 REAL,'
                       'TT216 REAL,'
                       'TT217 REAL,'
                       'TT218 REAL,'
                       'TT219 REAL,'
                       'TT220 REAL)')

        self.conn.commit()
        self.db_append()

    def db_append(self, t=0):
        t_string = (t,)
        p_string = (t,)
        for d in self.disp:
            if d[:1] == 'T':
                t_string = t_string + (v.par[d]['val'],)
            else:
                p_string = p_string + (v.par[d]['val'],)

        db_string = 'INSERT INTO temperatures VALUES ('
        for i in t_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, t_string)

        db_string = 'INSERT INTO pressures VALUES ('
        for i in p_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, p_string)

        v_string = (t, )
        for valve in self.valves:
            v_string = v_string + (str(v.par[valve]['val']), )
        db_string = 'INSERT INTO valves VALUES ('
        for i in v_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, v_string)

        par = ['power', 'pressure', 'flux']
        for dev in ['EL101', 'FC301A', 'FC301B']:
            par_string = (t, )
            for p in par:
                par_string = par_string + (v.par[dev][p], )
            par_string = par_string + (str(v.par[dev]['status']),)
            db_string = 'INSERT INTO ' + dev + '  VALUES ('
            for i in par_string:
                db_string = db_string + '?, '
            db_string = db_string[:len(db_string) - 2] + ')'
            self.c.execute(db_string, par_string)

        self.conn.commit()

    #
    def simul(self):
        # print('Fake')
        if not v.sel_util:
            f1 = Thread(target=self.simul_open())
            f1.start()
            f1.join()
        else:
            self.sim.close()
        # print(v.sel_util)

    def simul_open(self):
        # Apertuta della finestra simulazione (Fake)
        from UI._simulation.sim import Sim
        self.sim = Sim()
        self.sim.show()
        v.sel_util = True

    def settings(self):
        # Apertura della finestra Settings
        if not v.sel_settings:
            f2 = Thread(target=self.settings_open())
            f2.start()
            f2.join()
            # self.settings_on = True
            v.sel_settings = True
        else:
            v.sel_settings = False
            # self.settings_on = False
            self.set.close()

    def settings_open(self):
        from UI.settings.settings import Settings
        self.set = Settings()
        self.set.show()
        v.sel_settings = True

    def mb_config(self):
        # Apertura della finestra Modbus Config
        if not v.sel_mb:
            f_mbs = Thread(target=self.mb_config_open())
            f_mbs.start()
            f_mbs.join()
            v.sel_mb = True
        else:
            v.sel_mb = False
            self.mb_set.close()

    def mb_config_open(self):
        from UI.settings.mb_set import MbSetting
        self.mb_set = MbSetting()
        self.mb_set.show()
        v.sel_mb = True

    def interface_open(self):
        self.main = Ui()

        self.FC301_activation()

        # -- Definizione delle azioni --------------------------------------------------------------------
        self.main.ui.EL101_start_PB.clicked.connect(self.EL101_switch)
        self.main.ui.FC301_start_PB.clicked.connect(self.FC301_switch)
        self.main.ui.fake_BTN.clicked.connect(self.simul)
        self.main.ui.settings_BTN.clicked.connect(self.settings)
        self.main.ui.mb_set_BTN.clicked.connect(self.mb_config)

        for valve in self.valves:   # Al doppio click sulle valvole, devono cambiare stato
            self.main.ui.__getattribute__(valve + '_img_LBL').mouseDoubleClickEvent = \
                partial(self.valve_clicked, valve=valve)

        for elem in ['FC301A', 'FC301B', 'FC301', 'EL101']:
            self.main.ui.__getattribute__(elem + '_Pset_DSB').valueChanged.connect(self.set_params)
        for elem in ['FC301_split', 'FC301A_activation', 'FC301B_activation']:
            self.main.ui.__getattribute__(elem + '_CkB').clicked.connect(self.FC301_activation)
        # ------------------------------------------------------------------------------------------------

        timer = QtCore.QTimer()
        timer.timeout.connect(self.refresh)
        timer.start(1000)

        self.main.show()
        self.app.exec()

    def EL101_switch(self):
        # cambia lo stato della variabile "start" per EL101
        v.par['EL101']['start'] = self.main.ui.EL101_start_PB.isChecked()
        self.valve_switch()     # richiamo delle funzioni relative alle valvole

    def FC301_switch(self):
        # cambia lo stato della variabile "start" per FC301
        for disp in ['FC301', 'FC301A', 'FC301B']:
            v.par[disp]['start'] = self.main.ui.FC301_start_PB.isChecked()
        self.valve_switch()     # richiamo delle funzioni relative alle valvole

    def FC301_activation(self):
        for elem in ['FC301A', 'FC301B']:
            # verifica delle FC abilitate, scrittura nel dizionario e disabilitazione delle FC disattive
            v.par[elem]['activated'] = self.main.ui.__getattribute__(elem + '_activation_CkB').isChecked()
            self.main.ui.__getattribute__(elem + '_GB').setEnabled(v.par[elem]['activated'])

        # La funzione FC può essere attiva solo se almeno una FC è abilitata
        self.main.ui.FC301_start_PB.setEnabled(v.par['FC301A']['activated'] or v.par['FC301B']['activated'])

        # Se la funzione FC è già attiva, si verifica se almeno una FC è attiva, altrimenti la funzione deve essere
        # disattivata
        if self.main.ui.FC301_start_PB.isChecked():
            self.main.ui.FC301_start_PB.setChecked(v.par['FC301A']['activated'] or v.par['FC301B']['activated'])
            v.par['FC301']['start'] = self.main.ui.FC301_start_PB.isChecked()

        # Lo Split power delle FC è possibile se entrambe sono attive
        self.main.ui.FC301_split_CkB.setEnabled(v.par['FC301A']['activated'] and v.par['FC301B']['activated'])
        if not (v.par['FC301A']['activated'] and v.par['FC301B']['activated']):
            self.main.ui.FC301_split_CkB.setChecked(False)

        self.valve_switch()     # richiamo delle funzioni relative alle valvole
        self.set_params()       # TODO: Da verificare se deve rimanere qui, o se deve ricadere in refresh

    def valve_clicked(self, e, valve):
        # la valvola cliccata deve cambiare stato: si inverte il valore in v.par
        v.par[valve]['val'] = not v.par[valve]['val']

        # lo stesso valore viene scritto in v.dat
        ch = v.par[valve]['mb']['ch']
        reg = v.par[valve]['mb']['reg']
        v.dat[ch]['reg'][reg] = v.par[valve]['val']

        # viene scritto il registro corrispondente su ModBus    TODO: Da capire se si vuole spostare in refresh
        self.valve_par_to_mb(item=valve)

    def valve_switch(self):
        # Se EL101 è avviato, la valvola EV104 deve essere aperta, altrimenti deve essere chiusa
        v.par['EV104']['val'] = v.par['EL101']['start']

        # -- TODO: Da capire se si vuole spostare in refresh -------------------------------------
        self.par_to_dat('EV104')        # lo stato della valvola viene scritto su v.dat
        self.valve_par_to_mb('EV104')   # viene scritto il registro corrispondente su ModBus
        # ----------------------------------------------------------------------------------------

        # Se FC301 è avviato, la valvola EV303 deve essere aperta, altrimenti deve essere chiusa
        v.par['EV303']['val'] = v.par['FC301']['start']

        # -- TODO: Da capire se si vuole spostare in refresh -------------------------------------
        self.par_to_dat('EV303')        # lo stato della valvola viene scritto su v.dat
        self.valve_par_to_mb('EV303')   # viene scritto il registro corrispondente su ModBus
        # ----------------------------------------------------------------------------------------

    def valve_draw(self):   # Rappresentazione grafica delle valvole
        if v.par['EV104']['val']:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDX_20x20.png"))
        else:
            self.main.ui.EV104_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV303']['val']:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowSX_20x20.png"))
        else:
            self.main.ui.EV303_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopHoriz_20x20.png"))

        if v.par['EV103']['val']:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowUp_20x20.png"))
        else:
            self.main.ui.EV103_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

        if v.par['EV302']['val']:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/arrowDown_20x20.png"))
        else:
            self.main.ui.EV302_img_LBL.setPixmap(QtGui.QPixmap("UI/_resources/StopVert_20x20.png"))

    def refresh(self):
        self.mb_to_par()        # lettura dati da ModBus

        if v.sel_util:          # se la finestra fake è attiva, vengono letti i valori dalla finestra
            self.sim.data()
            self.simulation()   # elaborazione dei dati dei dispositivi in funzione dei dati di simulazione

        # viene stimato il consumo di H2 per le due FC: l'H2 viene parzializzato sulle FC attive sulla base delle
        # potenze assorbite
        for elem in ['FC301A', 'FC301B']:   # TODO: forse va spostato nella sezione di elaborazione dati
            v.par[elem]['flux'] = v.par['FC301']['flux'] * int(v.par[elem]['activated']) * v.par[elem]['power'] / \
                                max((v.par['FC301A']['power'] + v.par['FC301B']['power']), 0.000001)

        # --- Scrittura dei dati nell'interfaccia #TODO: da spostare in una sezione dedicata -----------------------
        for elem in ['FC301A', 'FC301B', 'EL101']:
            self.main.ui.__getattribute__(elem + '_Pset_DSB').setValue(v.par[elem]['power_set'])
            self.main.ui.__getattribute__(elem + '_Pread_DSB').setValue(v.par[elem]['power'])
            self.main.ui.__getattribute__(elem + '_H2_DSB').setValue(v.par[elem]['flux'])

            self.main.led_light(elem + '_statusLed_LBL', v.par[elem]['status'])
            self.main.ui.__getattribute__(elem + '_log_TE').setText(v.par[elem]['log'])

        self.main.ui.FT102_DSB.setValue(v.par['EL101']['flux'])
        self.main.ui.FT308_DSB.setValue(v.par['FC301A']['flux'] + v.par['FC301B']['flux'])
        # self.main.ui.PI307_DSB.setValue(v.par['PI307']['pressure'])
        # self.main.ui.TI306_DSB.setValue(v.par['TI306']['T'])

        self.main.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301A']['power'] + v.par['FC301B']['power'])
        self.main.ui.FC301_H2_DSB.setValue(v.par['FC301']['flux'])

        for d in self.disp:
            self.main.ui.__getattribute__(d + '_DSB').setValue(v.par[d]['val'])
        # ----------------------------------------------------------------------------------------------------------

        self.valve_draw()       # Aggiornamento grafico delle valvole
        self.visual_flux()      # Aggiornamento grafico dei flussi
        self.alarm_check()    # TODO: Bisogna definire la logica degli allarmi
        self.led_set()          # Aggiornamento dei led

        self.main.ui.fake_BTN.setChecked(v.sel_util)            # Aggiornamento dello stato del pulsante FAKE
        self.main.ui.settings_BTN.setChecked(v.sel_settings)    # Aggiornamento dello stato del pulsante SETTINGS

        self.t = time.perf_counter() - self.start_t     # tempo dall'inizio dell'esecuzione
        self.dt = time.perf_counter() - self.t_last     # tempo del singolo ciclo di refresh
        self.t_last = time.perf_counter()

        self.db_append(self.t)
        #
        # # self.set_params()
        # print('refresh \t %.3f\t%.3f' % (self.t, self.dt))

    def set_params(self):   # Lettura dei parametri dall'interfaccia e scrittura in v.par
        # print('set params')
        for elem in ['FC301A', 'FC301B', 'EL101']:
            v.par[elem]['power_set'] = self.main.ui.__getattribute__(elem + '_Pset_DSB').value()
        v.par['FC301A']['activated'] = self.main.ui.FC301A_activation_CkB.isChecked()
        v.par['FC301B']['activated'] = self.main.ui.FC301B_activation_CkB.isChecked()
        v.par['FC301']['split'] = self.main.ui.FC301_split_CkB.isChecked()
        if self.main.ui.FC301_split_CkB.isChecked():
            for elem in ['FC301A', 'FC301B']:
                v.par[elem]['power_set'] = self.main.ui.FC301_Pset_DSB.value() / 2
                self.main.ui.__getattribute__(elem + '_Pset_DSB').setValue(v.par[elem]['power_set'])
            # v.par['FC301A']['Pset'] = self.main.ui.FC301_Pset_DSB.value() / 2
            # v.par['FC301B']['Pset'] = self.main.ui.FC301_Pset_DSB.value() / 2
        else:
            v.par['FC301A']['power_set'] = self.main.ui.FC301A_Pset_DSB.value()
            v.par['FC301B']['power_set'] = self.main.ui.FC301B_Pset_DSB.value()
            self.main.ui.FC301_Pset_DSB.setValue(v.par['FC301A']['power_set'] * int(v.par['FC301A']['activated']) +
                                                 v.par['FC301B']['power_set'] * int(v.par['FC301B']['activated']))

    def visual_flux(self):  # rappresentazione grafica dei flussi
        # el = elettrolizzatore in produzione
        el = v.par['EL101']['start'] and v.par['EL101']['flux'] > 0 and v.par['EL101']['status'] == 'on' \
             and v.par['EV104']['val']

        # fc = fuel cell alimentata
        fc = (v.par['FC301A']['status'] == 'on' or v.par['FC301B']['status'] == 'on') and v.par['EV303']['val'] and v.par['FC301']['start'] # and v.par['FC301A']['H2'] + v.par['FC301B']['H2'] > 0


        self.main.ui.EL101_out_LN.setVisible(el)
        for elem in ['FC301_in', 'mainline3', 'mainline2']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(fc)
        for elem in ['mainline1', 'S201', 'S202', 'S203', 'S204', 'S205']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(el or fc)

    def simulation(self):   # Calcolo dei parametri in base alla schermata Simulations
        v.par['EL101']['power'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['power'] / 100)
        v.par['EL101']['flux'] = v.par['EL101']['power'] * 3.3 / 1.2 * 0.06 * v.sim['EL101']['flux'] / 100
        v.par['EL101']['pressure'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['pressure'] / 100)

        # La pressione dell'elettrolizzatore è pari al massimo della pressione delle bombole
        a = []
        for i in ['S201', 'S202', 'S203', 'S204', 'S205']:
            # a.append(self.main.ui.PI226_DSB.value())
            a.append(v.sim[i]['pressure'])
            v.par[i] = copy.deepcopy(v.sim[i])
        v.par['EL101']['pressure'] = max(a) * v.sim['EL101']['pressure'] / 100

    def alarm_check(self):  # Verifica degli stati di allarme
        # print('Delay = ' + str(v.alarm['EL101']['power']['delay']))
        # print('Time = ' + str(v.alarm['EL101']['power']['time']))

        states = ['off', 'alert', 'warning']

        for disp in ['EL101', 'FC301A', 'FC301B']:
            log = ''
            # print(disp)

            # La verifica dell'allarme viene eseguita se il dispositivo è attivato e se viene richiesta una potenza
            # superiore a 0
            if v.par[disp]['start'] and v.par[disp]['power_set'] != 0:
                for p in ['power', 'pressure', 'flux']:
                    # status = 0

                    # "val" = valore del parametro in p.u.; "a" = soglie di allarme superiori e inferiori in p.u.)
                    if p == 'power':
                        # print('Pset : ' + str(v.par[disp]['Pread']) + '\tPread : ' + str(v.par[disp]['Pset']))
                        val = v.par[disp]['power'] / v.par[disp]['power_set']
                        a = [1 - v.alarm[disp][p]['tr-'] / 100, 1 + v.alarm[disp][p]['tr+'] / 100]
                    else:
                        print(disp)
                        print(p + ': ' + str(v.par[disp][p]))
                        val = v.par[disp][p]
                        a = [v.alarm[disp][p]['tr-'], v.alarm[disp][p]['tr+']]

                    # il dispositivo è in allarme se l'allarme è attivo, e se il parametro è al di fuori dei range di
                    # ammissibilità
                    if v.alarm[disp][p]['on'] and (val > a[1] or val < a[0]):
                        # se il dispositivo è in allarme, viene conteggiato il tempo di allarme, e il dispositivo si
                        # considera in ALERT (status = 1)
                        status = 1
                        v.alarm[disp][p]['time'] += self.dt
                        # print('warning EL101 power')

                        # se il tempo di alert supera il tempo di soglia, lo stato diventa WARNING (status = 2)
                        if v.alarm[disp][p]['time'] >= v.alarm[disp][p]['delay']:
                            status = 2
                            # print('ALARM EL101 power')
                            pass

                    else:   # se l'allarme per la grandezza indicata non è attivo...
                        status = 0                      # ...lo status di allarme è OFF...
                        v.alarm[disp][p]['time'] = 0    # ... e si azzera il tempo di alert.

                    if status > 0:  # Se il parametro è in WARNING o in ALERT si compone il messaggio di errore
                        if log != '':   # Se nel log c'era già qualcosa si aggiunge un rigo
                            log = log + '\n'
                        log = log + states[status] + ' ' + p + ' for device ' + disp

                    # la relativa voce in v.alarm diventa "off", "warning" o "alert"
                    v.alarm[disp][p]['status'] = states[status]

                    # for p in ['pressure', 'H2']:
                    #     if v.alarm['EL101'][p]['on'] and \
                    #             (v.par['EL101'][p] > v.alarm['EL101'][p]['tr+'] or
                    #              v.par['EL101'][p] < v.alarm['EL101'][p]['tr-']):
                    #         v.alarm['EL101'][p]['time'] += self.dt
                    #         print('warning EL101 ' + p)
                    #     else:
                    #         v.alarm['EL101'][p]['time'] = 0

            # Se il componente è disattivo o non eroga/riceve potenza, si azzerano i tempi di alert per tutte le
            # grandezze
            else:
                for p in ['power', 'pressure', 'flux']:
                    v.alarm[disp][p]['time'] = 0

            # self.main.ui.EL101_log_TE.setText(log)
            self.main.ui.__getattribute__(disp + '_log_TE').setText(log)    # Scrittura del log del dispositivo
            # print('log: ' + log)

            # print()

            # self.main.ui.EL101_log_TE.clear()
            # for p in ['power', 'pressure', 'H2']:
            #     if v.alarm['EL101'][p]['time'] > 5:
            #         self.main.ui.EL101_log_TE.setText(self.main.ui.EL101_log_TE.toPlainText() + 'ERRORE EL101 ' + p + '\n')
            #     # else:
            #     #     self.main.ui.EL101_log_TE.clear()

    def led_set(self):  # Aggiornamento dei led
        for disp in ['EL101', 'FC301A', 'FC301B']:

            states = ['off', 'alert', 'warning']
            if v.par[disp]['start']:    # Il controllo si fa solo se il dispositivo è stato avviato
                if v.par[disp]['power_set'] > 0:     # se la potenza è maggiore di zero, il dispositivo è in ON
                    v.par[disp]['status'] = 'on'
                else:                           # altrimento il dispositivo è in standby
                    v.par[disp]['status'] = 'standby'

                i = 0   # indica lo stato di allarme maggiore per il dispositivo
                for p in ['power', 'pressure', 'flux']:
                    i = max(i, states.index(v.alarm[disp][p]['status']))
                    # print(disp, p, i)

                if i > 0:   # dispositivo in Warning / Allarme
                    v.par[disp]['status'] = states[i]   # scrittura dello stato

                #     if v.alarm[disp][p]['time'] > 0:
                #         v.par[disp]['status'] = 'alert'
                #         break
                # for p in ['power', 'pressure', 'H2']:
                #     if v.alarm[disp][p]['time'] > 5:
                #         v.par[disp]['status'] = 'warning'
                #         break
            else:                       # Il dispositivo è in OFF
                v.par[disp]['status'] = 'off'

    def mb_to_par(self):    # trasferimento dei valori da modbus a v.dat e quindi a v.par
        v.mb_conn = True    # se una lettura dal registro fallisce, diventa False

        # Lettura dei segnali analogici
        for ch in [21, 22, 31]:
            regs = self.mb.read_holding(ch=ch)
            for i in range(0, 8):
                v.dat[ch]['reg'][i + 14] = regs[i]

        # Considero i valori relativi agli indicatori inseriti in "self.disp"
        for d in self.disp:
            ch = v.par[d]['mb']['ch']
            reg = v.par[d]['mb']['reg']
            m = v.par[d]['mb']['scale']
            q = v.par[d]['mb']['offset']
            v.par[d]['val'] = v.dat[ch]['reg'][reg] * m - q     # I valori sono corretti per fatt. di scala e offset

        # TODO: da testare
        # Lettura dei segnali digitali
        for ch in [11, 12, 13, 14]:
            k = list(v.dat[ch]['reg'].keys())   # lista dei registri da leggere
            # read_coils legge sempre 8 registri, li tronco a 4
            regs = self.mb.read_holding(ch=ch, reg=0, count=4) + list(self.mb.read_coils(ch=ch, reg=16, count=4))[:4]
            for i in range(0, 8):
                v.dat[ch]['reg'][k[i]] = regs[i]
            # TODO: non li scrivo in v.par??????


        # ModBus Led setting
        # durante la lettura da ModBus, v.mb_conn, se c'è un errore, v.mb_conn diventa False
        if v.mb_conn:
            self.main.led_light('mb_statusLed_LBL', 'on')
        else:
            self.main.led_light('mb_statusLed_LBL', 'warning')
        # TODO: Bisogna implementare la scrittura del log. Magari indicare quali canali modbus non sono funzionanti

    # -- Al momento questa funzione non viene usata ------------------------------------------------------------
    def par_to_mb(self):    # Trasferimento dei segnali digitali dall'interfaccia al registro modbus dei DO
        for ch in [11, 12, 13, 14]:
            for reg in [16, 17, 18, 19]:
                self.mb.write_coil(address=reg, value=bool(v.dat[ch]['reg'][reg]), unit=ch)
    # ----------------------------------------------------------------------------------------------------------

    def valve_par_to_mb(self, item):    # Trasferimento dello stato di una valvola al registro ModBus dei DO
        ch = v.par[item]['mb']['ch']
        reg = v.par[item]['mb']['reg']
        # print('prova scrittura registro ' + str(reg) + ' della unità ' + str(ch))
        self.mb.write_coil(address=reg, value=bool(v.dat[ch]['reg'][reg]), unit=ch)

        # TODO: Può essere una alternativa???
        # self.mb.write_coil(address=reg, value=bool(v.par[item]['val']), unit=ch)

    def par_to_dat(self, item):     # TODO: Potrebbe non essere necessario
        ch = v.par[item]['mb']['ch']
        reg = v.par[item]['mb']['reg']
        v.dat[ch]['reg'][reg] = v.par[item]['val']
        pass

    def graph_init(self):
        pass



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
