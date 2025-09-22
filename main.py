import copy
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib

from UI.mainUI import Ui
from _shared import variables as v
from threading import Thread
from functools import partial
import time
import datetime

import sqlite3

from DAT.modbus import Modbus

# -- Rescaling della schermata ----------------
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------------------------


class Main:
    def __init__(self):
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # Necessaria per il rescaling

        self.app = QtWidgets.QApplication(sys.argv)

        # -- Necessario per il rescaling --------------
        self.app.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
        self.mainwindow = QtWidgets.QMainWindow()
        # ---------------------------------------------

        # -- Inizializzazione delle variabili delle finestre -----------
        self.sim = None
        self.set = None
        self.mb_set = None
        self.main = None

        self.conn = None
        self.c = None

        self.ax_p = None
        self.ax_power = None
        self.ax_pressure = None
        self.ax_flux = None
        # --------------------------------------------------------------

        self.mb = Modbus()

        # Elenco dei dispositivi
        self.devices = ['EL101', 'FC301A', 'FC301B']

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
        self.start_t = time.perf_counter()      # tempo assoluto dell'avvio del softarwe

        self.db_init()                          # Inizializzo il database di archivio

        # self.app = QtWidgets.QApplication(sys.argv)

        f0 = Thread(target=self.interface_open())
        f0.start()

    def db_init(self):      # Inizializzazione del database

        # il database avrà come nome la data e l'ora, in formato YYYYMMDD_hhmmss
        now = datetime.datetime.now()
        dbname = now.strftime('%Y%m%d_%H%M%S') + '.db'

        self.conn = sqlite3.connect('_database/' + dbname)  # connessione al database
        self.c = self.conn.cursor()                         # cursore di esecuzione

        for elem in self.devices:
            # Tabella dei dispositivi di potenza
            self.c.execute('CREATE TABLE IF NOT EXISTS ' + elem + '('
                                                                  'time REAL, '
                                                                  'power REAL,'
                                                                  'pressure REAL, '
                                                                  'flux REAL,'
                                                                  'status TEXT)')

        # tabella delle elettrovalvole
        self.c.execute('CREATE TABLE IF NOT EXISTS valves('
                       'time REAL, '
                       'EV103 TEXT,'
                       'EV104 TEXT,'
                       'EV302 TEXT,'
                       'EV303 TEXT)')

        # Tabella delle pressioni
        self.c.execute('CREATE TABLE IF NOT EXISTS pressures('
                       'time REAL, '
                       'PI226 REAL,'
                       'PI227 REAL,'
                       'PI228 REAL,'
                       'PI229 REAL,'
                       'PI230 REAL,'
                       'PI307 REAL)')

        # Tabella delle temperature
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

    def db_append(self, t=0):   # Aggiornamento del database

        # creazione delle stringhe di scrittura sul database delle pressioni e delle temperature
        t_string = (t,)
        p_string = (t,)
        for d in self.disp:
            if d[:1] == 'T':
                t_string = t_string + (v.par[d]['val'],)
            else:
                p_string = p_string + (v.par[d]['val'],)

        # scrittura su database delle temperature
        db_string = 'INSERT INTO temperatures VALUES ('
        for _ in t_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, t_string)

        # scrittura su database delle pressioni
        db_string = 'INSERT INTO pressures VALUES ('
        for _ in p_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, p_string)

        # scrittura su database dello stato delle elettrovalvole
        v_string = (t, )
        for valve in self.valves:
            v_string = v_string + (str(v.par[valve]['val']), )
        db_string = 'INSERT INTO valves VALUES ('
        for _ in v_string:
            db_string = db_string + '?, '
        db_string = db_string[:len(db_string) - 2] + ')'
        self.c.execute(db_string, v_string)

        # Scruttura su database delle letture di potenza, pressione e flusso di H2 dei dispositivi di potenza
        par = ['power', 'pressure', 'flux']
        for dev in ['EL101', 'FC301A', 'FC301B']:
            par_string = (t, )
            for p in par:
                par_string = par_string + (v.par[dev][p], )
            par_string = par_string + (str(v.par[dev]['status']),)
            db_string = 'INSERT INTO ' + dev + '  VALUES ('
            for _ in par_string:
                db_string = db_string + '?, '
            db_string = db_string[:len(db_string) - 2] + ')'
            self.c.execute(db_string, par_string)

        self.conn.commit()

    #
    def simul(self):        # Azione al pulsante fake
        if not v.sel_util:  # se la finestra di simulazione è chiusa, deve aprirla
            f1 = Thread(target=self.simul_open())
            f1.start()
            f1.join()
        else:               # se è aperta, dece chiuderla
            self.sim.close()

    def simul_open(self):   # Apertuta della finestra simulazione (Fake)
        from UI._simulation.sim import Sim
        self.sim = Sim()
        self.sim.show()
        v.sel_util = True

    def settings(self):         # Azione pulsante Settings
        if not v.sel_settings:  # se la finestra di settings è chiusa, deve aprirla
            f2 = Thread(target=self.settings_open())
            f2.start()
            f2.join()
            v.sel_settings = True
        else:                   # se è aperta, dece chiuderla
            v.sel_settings = False
            self.set.close()

    def settings_open(self):    # Apertura della finestra Settings
        from UI.settings.settings import Settings
        self.set = Settings()
        self.set.show()
        v.sel_settings = True

    def mb_config(self):        # Azione del pulsante ModBus Settngs
        if not v.sel_mb:        # se la finestra di configurazione Modbus è chiusa, deve aprirla
            f_mbs = Thread(target=self.mb_config_open())
            f_mbs.start()
            f_mbs.join()
            v.sel_mb = True
        else:                   # se è perta, deve chiuderla
            v.sel_mb = False
            self.mb_set.close()

    def mb_config_open(self):   # Apertura della finestra Modbus Config
        from UI.settings.mb_set import MbSetting
        self.mb_set = MbSetting()
        self.mb_set.show()
        v.sel_mb = True

    def interface_open(self):   # Impostazione e apertuda dell'interfaccia
        self.main = Ui()

        self.graph_init()   # Inizializzazione dei Trend

        self.FC301_activation()

        # -- Definizione delle azioni --------------------------------------------------------------------
        self.main.ui.EL101_start_PB.clicked.connect(self.EL101_switch)
        self.main.ui.FC301_start_PB.clicked.connect(self.FC301_switch)
        # self.main.ui.fake_BTN.clicked.connect(self.simul) # TODO: da riattivare per la simulazione attiva
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

    def EL101_switch(self):     # cambia lo stato della variabile "start" per EL101
        v.par['EL101']['start'] = self.main.ui.EL101_start_PB.isChecked()
        self.valve_switch()     # richiamo delle funzioni relative alle valvole

    def FC301_switch(self):     # cambia lo stato della variabile "start" per le fuel cell
        for disp in ['FC301', 'FC301A', 'FC301B']:
            v.par[disp]['start'] = self.main.ui.FC301_start_PB.isChecked()
        self.valve_switch()     # richiamo delle funzioni relative alle valvole

    def FC301_activation(self):     # verifica sulle fuel cell
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

    def valve_clicked(self, _, valve):  # funzione al click sulle icone delle valvole
        # la valvola cliccata ("valve") deve cambiare stato: si inverte il valore in v.par
        v.par[valve]['val'] = not v.par[valve]['val']

        # lo stesso valore viene scritto in v.dat
        ch = v.par[valve]['mb']['ch']       # canale del dispositivo che aziona la valvola "valve"
        reg = v.par[valve]['mb']['reg']     # registro modbus della valvìola "valve"
        v.dat[ch]['reg'][reg] = v.par[valve]['val']

        # viene scritto il registro corrispondente su ModBus    TODO: Da capire se si vuole spostare in refresh
        self.valve_par_to_mb(item=valve)

    def valve_switch(self):     # Commutazione delle valvole, richiamato da azioni specifiche
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

        self.main.ui.EL101_pressure_DSB.setValue(v.par['EL101']['pressure'])
        self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301']['power'])
        # self.main.ui.FC301_Pread_DSB.setValue(v.par['FC301A']['power'] + v.par['FC301B']['power'])
        self.main.ui.FC301_H2_DSB.setValue(v.par['FC301']['flux'])

        for d in self.disp:
            self.main.ui.__getattribute__(d + '_DSB').setValue(v.par[d]['val'])
        # ----------------------------------------------------------------------------------------------------------

        self.valve_draw()       # Aggiornamento grafico delle valvole
        self.visual_flux()      # Aggiornamento grafico dei flussi
        self.alarm_check()      # TODO: Bisogna definire la logica degli allarmi
        self.led_set()          # Aggiornamento dei led

        self.main.ui.fake_BTN.setChecked(v.sel_util)            # Aggiornamento dello stato del pulsante FAKE
        self.main.ui.settings_BTN.setChecked(v.sel_settings)    # Aggiornamento dello stato del pulsante SETTINGS

        self.t = time.perf_counter() - self.start_t     # tempo dall'inizio dell'esecuzione
        self.dt = time.perf_counter() - self.t_last     # tempo del singolo ciclo di refresh
        self.t_last = time.perf_counter()

        self.db_append(int(self.t))                     # Aggiornamento del database
        self.graph_update()                             # Aggiornamento dei grafici

    def set_params(self):   # Lettura dei parametri dall'interfaccia e scrittura in v.par
        for elem in self.devices:
            v.par[elem]['power_set'] = self.main.ui.__getattribute__(elem + '_Pset_DSB').value()
        v.par['FC301A']['activated'] = self.main.ui.FC301A_activation_CkB.isChecked()
        v.par['FC301B']['activated'] = self.main.ui.FC301B_activation_CkB.isChecked()
        v.par['FC301']['split'] = self.main.ui.FC301_split_CkB.isChecked()

        # se la casella SPLIT è attiva, si ripartisce la potenza sulle due fuel cell
        if self.main.ui.FC301_split_CkB.isChecked():
            for elem in ['FC301A', 'FC301B']:
                v.par[elem]['power_set'] = self.main.ui.FC301_Pset_DSB.value() / 2
                self.main.ui.__getattribute__(elem + '_Pset_DSB').setValue(v.par[elem]['power_set'])

        else:   # se lo split non è attivo, la potenza dipende solo dalle FC attive
            v.par['FC301A']['power_set'] = self.main.ui.FC301A_Pset_DSB.value()
            v.par['FC301B']['power_set'] = self.main.ui.FC301B_Pset_DSB.value()
            self.main.ui.FC301_Pset_DSB.setValue(v.par['FC301A']['power_set'] * int(v.par['FC301A']['activated']) +
                                                 v.par['FC301B']['power_set'] * int(v.par['FC301B']['activated']))

    def visual_flux(self):  # rappresentazione grafica dei flussi

        # -- Gestione Fake semplificata dei flussi (solo se si esclude SIM.ui ----------------------------------------
        if v.par['FC301']['start']:
            for fc in ['FC301A', 'FC301B']:
                v.par[fc]['activated'] = self.main.ui.__getattribute__(fc + '_activation_CkB').isChecked()
                if v.par[fc]['activated']:
                    v.par[fc]['power'] = v.par[fc]['power_set']
                    v.par[fc]['flux'] = v.par[fc]['power_set'] / 2.5 * 2
                else:
                    v.par[fc]['power'] = 0
                    v.par[fc]['flux'] = 0
        else:
            for fc in ['FC301A', 'FC301B']:
                v.par[fc]['power'] = 0
                v.par[fc]['flux'] = 0

        v.par['FC301']['flux'] = v.par['FC301A']['flux'] + v.par['FC301B']['flux']
        v.par['FC301']['power'] = v.par['FC301A']['power'] + v.par['FC301B']['power']

        if v.par['EL101']['start']:
            v.par['EL101']['power'] = v.par['EL101']['power_set']
            v.par['EL101']['flux'] = v.par['EL101']['power_set'] * 0.12
        else:
            v.par['EL101']['power'] = 0
            v.par['EL101']['flux'] = 0
        # ------------------------------------------------------------------------------------------------------------

        # Il flusso in uscita all'elettrolizzatore esiste se l'elettolizzatore è su START e il suo stato
        # non è OFF o StandBy, e se l'elettrovalvola relativa è aperta
        el = v.par['EL101']['start'] and v.par['EL101']['flux'] > 0 and v.par['EL101']['status'] != 'off' \
             and v.par['EL101']['status'] != 'standby' and v.par['EV104']['val']
        self.main.ui.EL101_out_LN.setVisible(el)

        # Il flusso in ingresso alle fuelcell esiste se almeno una FC è attiva con stato ON, se è avviata
        # la generazione, se il MFC rileva flusso, e se l'elettrovalvola relativa è aperta
        fc = ((v.par['FC301A']['status'] == 'on' or v.par['FC301B']['status'] == 'on')
              and v.par['EV303']['val'] and v.par['FC301']['start'] and v.par['FC301']['flux'] > 0)
        self.main.ui.FC301_in_LN.setVisible(fc)

        # La linea destra e superire ha flusso se sono alimentate le FC o se è aperto il vent EV302
        for elem in ['dx', 'up']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(fc or v.par['EV302']['val'])

        # Il flusso sulle linee delle bombole esiste se è in funzione l'EL, le FC o una delle valvole di vent
        for elem in ['vessel', 'S201', 'S202', 'S203', 'S204', 'S205']:
            self.main.ui.__getattribute__(elem + '_LN').setVisible(el or fc or v.par['EV103']['val']
                                                                   or v.par['EV302']['val'])

        # settaggio delle linee di vent
        self.main.ui.EV103_LN.setVisible(v.par['EV103']['val'])
        self.main.ui.EV302_LN.setVisible(v.par['EV302']['val'])
        self.main.ui.vent_LN.setVisible(v.par['EV103']['val'] or v.par['EV302']['val'])

    def simulation(self):   # Calcolo dei parametri in base alla schermata Simulations
        # estrapolazione dei valori di EL101 a partire dai valori percentuali della Simulazione
        v.par['EL101']['power'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['power'] / 100)
        v.par['EL101']['flux'] = v.par['EL101']['power'] * 3.3 / 1.2 * 0.06 * v.sim['EL101']['flux'] / 100
        v.par['EL101']['pressure'] = self.main.ui.EL101_Pset_DSB.value() * (v.sim['EL101']['pressure'] / 100)

        # La pressione dell'elettrolizzatore è pari al massimo della pressione delle bombole
        a = []
        for i in ['S201', 'S202', 'S203', 'S204', 'S205']:
            a.append(v.sim[i]['pressure'])
            v.par[i] = copy.deepcopy(v.sim[i])
        v.par['EL101']['pressure'] = max(a) * v.sim['EL101']['pressure'] / 100

    def alarm_check(self):  # Verifica degli stati di allarme
        states = ['off', 'alert', 'warning']

        for dev in self.devices:
            log = ''

            # La verifica dell'allarme viene eseguita se il dispositivo è attivato e se viene richiesta una potenza
            # superiore a 0
            if v.par[dev]['start'] and v.par[dev]['power_set'] != 0:
                for p in ['power', 'pressure', 'flux']:
                    if p == 'power':    # per la potenza, l'allarme si calcola in relazione allo scostamento relativo
                        val = v.par[dev]['power'] / v.par[dev]['power_set']
                        a = [1 - v.alarm[dev][p]['tr-'] / 100, 1 + v.alarm[dev][p]['tr+'] / 100]
                    else:
                        val = v.par[dev][p]
                        a = [v.alarm[dev][p]['tr-'], v.alarm[dev][p]['tr+']]
                    # "val" è il valore della grandezza da analizzare
                    # "a" è la lista degli estremi dell'intervallo di ammissibilità del valore

                    # il dispositivo è in allarme se l'allarme è attivo, e se il parametro è al di fuori dei range di
                    # ammissibilità
                    if v.alarm[dev][p]['on'] and (val > a[1] or val < a[0]):
                        # se il dispositivo è in allarme, viene conteggiato il tempo di allarme, e il dispositivo si
                        # considera in ALERT (status = 1)
                        status = 1
                        v.alarm[dev][p]['time'] += self.dt

                        # se il tempo di alert supera il tempo di soglia, lo stato diventa WARNING (status = 2)
                        if v.alarm[dev][p]['time'] >= v.alarm[dev][p]['delay']:
                            status = 2

                    else:   # se l'allarme per la grandezza indicata non è attivo...
                        status = 0                      # ...lo status di allarme è OFF...
                        v.alarm[dev][p]['time'] = 0     # ...e si azzera il tempo di alert.

                    if status > 0:  # Se il parametro è in WARNING o in ALERT si compone il messaggio di errore
                        if log != '':   # Se nel log c'era già qualcosa si aggiunge un rigo
                            log = log + '\n'
                        log = log + states[status] + ' ' + p + ' for device ' + dev

                    # la relativa voce in v.alarm diventa "off", "warning" o "alert"
                    v.alarm[dev][p]['status'] = states[status]

            # Se il componente è disattivo o non eroga/riceve potenza, si azzerano i tempi di alert per tutte le
            # grandezze
            else:
                for p in ['power', 'pressure', 'flux']:
                    v.alarm[dev][p]['time'] = 0

            self.main.ui.__getattribute__(dev + '_log_TE').setText(log)    # Scrittura del log del dispositivo

    def led_set(self):      # Aggiornamento dei led
        for dev in self.devices:

            states = ['off', 'alert', 'warning']
            if v.par[dev]['start']:    # Il controllo si fa solo se il dispositivo è stato avviato
                if v.par[dev]['power_set'] > 0:    # se la potenza è maggiore di zero, il dispositivo è in ON
                    v.par[dev]['status'] = 'on'
                else:                               # altrimento il dispositivo è in standby
                    v.par[dev]['status'] = 'standby'

                i = 0       # indica lo stato di allarme maggiore per il dispositivo
                for p in ['power', 'pressure', 'flux']:
                    i = max(i, states.index(v.alarm[dev][p]['status']))

                if i > 0:   # dispositivo in Warning / Allarme
                    v.par[dev]['status'] = states[i]   # scrittura dello stato

            else:                       # Il dispositivo è in OFF
                v.par[dev]['status'] = 'off'

    def mb_to_par(self):    # trasferimento dei valori da modbus a v.dat e quindi a v.par
        v.mb_conn = True    # se una lettura dal registro fallisce, diventa False

        # Lettura dei segnali analogici
        for ch in [21, 22, 31]:     # todo: probabilmente i canali devono essere letti dalla configurazione
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
        for ch in [11, 12, 13, 14]:     # todo: probabilmente i canali devono essere letti dalla configurazione
            k = list(v.dat[ch]['reg'].keys())   # lista dei registri da leggere

            # per ogni unità (canale), ci sono 4 segnali di input (read_coils) e 4 di output (read_holding)
            regs = self.mb.read_holding(ch=ch, reg=0, count=4) + list(self.mb.read_coils(ch=ch, reg=16, count=4))[:4]
            # read_coils legge sempre 8 registri, li tronco a 4

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
        self.mb.write_coil(address=reg, value=bool(v.dat[ch]['reg'][reg]), unit=ch)

        # TODO: Può essere una alternativa???
        # self.mb.write_coil(address=reg, value=bool(v.par[item]['val']), unit=ch)

    def par_to_dat(self, item):     # TODO: Potrebbe non essere necessario
        ch = v.par[item]['mb']['ch']
        reg = v.par[item]['mb']['reg']
        v.dat[ch]['reg'][reg] = v.par[item]['val']
        pass

    def graph_init(self):   # Inizializzazione dei Trend

        # Creazione del FidureCanvas per i trend Potenza, Pressione e FLusso H2 dei dispositivi di potenza
        for par in ['power', 'pressure', 'flux']:
            # Ogni Canvas si chiama "canv_PROPRIETÀ"
            self.__setattr__('canv_' + par, FigureCanvas(plt.Figure(figsize=(3, 2))))

            # In ogni Canvas, si aggiunge un diagramma chiamato "ax_PROPRIETÀ"
            self.__setattr__('ax_' + par, self.__getattribute__('canv_' + par).figure.subplots())

            # Il Canvas viene aggiunto alla relativa Vertical Box Layout della ui
            self.main.ui.__getattribute__('graph_' + par + '_VBL').addWidget(self.__getattribute__('canv_' + par))

            # Per ogni dispositivo, si crea una linea del grafico chiamata "line_DISPOSITIVO_PROPRIETÀ"
            for el in ['EL101', 'FC301A', 'FC301B']:
                self.__setattr__('line_' + el + '_' + par,
                                 self.__getattribute__('ax_' + par).plot([0, 100], [0, 10], label=el)[0])

            # impostazione della legenda
            self.__setattr__('handles_' + par, self.__getattribute__('ax_' + par).get_legend_handles_labels()[0])
            self.__setattr__('labels_' + par, self.__getattribute__('ax_' + par).get_legend_handles_labels()[1])
            self.__getattribute__('ax_' + par).legend(self.__getattribute__('handles_' + par),
                                                      self.__getattribute__('labels_' + par))

        self.graph_update()

    def graph_update(self):     # Aggiornamento dei Trend
        # Impostazione dello stile
        font = {
            'weight': 'normal',
            'size': 8
        }
        matplotlib.rc('font', **font)

        for par in ['power', 'pressure', 'flux']:
            # Acquisizione dei dati dal database dei dispositivi
            max_t, max_v = 0, 0     # valori massimi degli assi delle ascisse e ordinate
            for el in ['EL101', 'FC301A', 'FC301B']:
                str_t = 'SELECT time FROM ' + el                # stringa di acquisizione del tempo
                str_v = 'SELECT ' + par + ' FROM ' + el         # stringa di acquisizione dei valori
                t_line = [t[0] for t in self.c.execute(str_t)]  # lista dei valori dell'ascissa
                p_line = [p[0] for p in self.c.execute(str_v)]  # lista dei valori dell'ordinata
                max_t, max_v = max(max_t, max(t_line)), max(max_v, max(p_line))

                # inserimento dei valori del tempo e della grandezza nella linea relativa
                self.__getattribute__('line_' + el + '_' + par).set_xdata(t_line)
                self.__getattribute__('line_' + el + '_' + par).set_ydata(p_line)

            # impostazioni degli estremi degli assi
            # il valore massimo delle liste è aumentato del 10%; viene aggiuntoi 0.1 per evutare che sia 0 (inizio)
            self.__getattribute__('ax_' + par).set_ylim([0, max_v * 1.1 + 0.1])
            self.__getattribute__('ax_' + par).set_xlim([0, max_t * 1.1 + 0.1])

            # impostazione deititoli degli assi
            self.__getattribute__('ax_' + par).set_xlabel('Time [sec]')
            self.ax_power.set_ylabel('Power [kW]')
            self.ax_pressure.set_ylabel('Pressure [barg]')
            self.ax_flux.set_ylabel('H2 Flux [Nm3/h]')

            self.__getattribute__('canv_' + par).draw()
            self.__getattribute__('canv_' + par).flush_events()


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
