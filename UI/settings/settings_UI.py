# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(885, 487)
        font = QtGui.QFont()
        font.setPointSize(8)
        settings.setFont(font)
        settings.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.EL101_GB = QtWidgets.QGroupBox(self.centralwidget)
        self.EL101_GB.setGeometry(QtCore.QRect(10, 30, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.EL101_GB.setFont(font)
        self.EL101_GB.setObjectName("EL101_GB")
        self.EL101_P_sep_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_P_sep_LBL.setGeometry(QtCore.QRect(150, 20, 10, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_P_sep_LBL.setFont(font)
        self.EL101_P_sep_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.EL101_P_sep_LBL.setObjectName("EL101_P_sep_LBL")
        self.EL101_power_min_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_power_min_DSB.setGeometry(QtCore.QRect(70, 20, 80, 20))
        self.EL101_power_min_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_power_min_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_power_min_DSB.setDecimals(1)
        self.EL101_power_min_DSB.setMinimum(0.1)
        self.EL101_power_min_DSB.setMaximum(999.9)
        self.EL101_power_min_DSB.setProperty("value", 10.0)
        self.EL101_power_min_DSB.setObjectName("EL101_power_min_DSB")
        self.EL101_power_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_power_LBL.setGeometry(QtCore.QRect(10, 20, 50, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_power_LBL.setFont(font)
        self.EL101_power_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_power_LBL.setObjectName("EL101_power_LBL")
        self.EL101_pressure_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_pressure_LBL.setGeometry(QtCore.QRect(10, 50, 50, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_pressure_LBL.setFont(font)
        self.EL101_pressure_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_pressure_LBL.setObjectName("EL101_pressure_LBL")
        self.EL101_flux_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_flux_LBL.setGeometry(QtCore.QRect(10, 80, 51, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_flux_LBL.setFont(font)
        self.EL101_flux_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_flux_LBL.setObjectName("EL101_flux_LBL")
        self.EL101_power_max_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_power_max_DSB.setGeometry(QtCore.QRect(160, 20, 80, 20))
        self.EL101_power_max_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_power_max_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_power_max_DSB.setDecimals(1)
        self.EL101_power_max_DSB.setMinimum(0.1)
        self.EL101_power_max_DSB.setMaximum(999.9)
        self.EL101_power_max_DSB.setProperty("value", 10.0)
        self.EL101_power_max_DSB.setObjectName("EL101_power_max_DSB")
        self.EL101_power_act_CkB = QtWidgets.QCheckBox(self.EL101_GB)
        self.EL101_power_act_CkB.setGeometry(QtCore.QRect(260, 20, 80, 20))
        self.EL101_power_act_CkB.setObjectName("EL101_power_act_CkB")
        self.EL101_pressure_sep_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_pressure_sep_LBL.setGeometry(QtCore.QRect(150, 50, 10, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_pressure_sep_LBL.setFont(font)
        self.EL101_pressure_sep_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.EL101_pressure_sep_LBL.setObjectName("EL101_pressure_sep_LBL")
        self.EL101_pressure_max_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_pressure_max_DSB.setGeometry(QtCore.QRect(160, 50, 80, 20))
        self.EL101_pressure_max_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_pressure_max_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_pressure_max_DSB.setPrefix("")
        self.EL101_pressure_max_DSB.setDecimals(1)
        self.EL101_pressure_max_DSB.setMinimum(0.0)
        self.EL101_pressure_max_DSB.setMaximum(50.0)
        self.EL101_pressure_max_DSB.setProperty("value", 30.0)
        self.EL101_pressure_max_DSB.setObjectName("EL101_pressure_max_DSB")
        self.EL101_pressure_min_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_pressure_min_DSB.setGeometry(QtCore.QRect(70, 50, 80, 20))
        self.EL101_pressure_min_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_pressure_min_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_pressure_min_DSB.setPrefix("")
        self.EL101_pressure_min_DSB.setDecimals(1)
        self.EL101_pressure_min_DSB.setMinimum(0.0)
        self.EL101_pressure_min_DSB.setMaximum(50.0)
        self.EL101_pressure_min_DSB.setProperty("value", 0.0)
        self.EL101_pressure_min_DSB.setObjectName("EL101_pressure_min_DSB")
        self.EL101_pressure_act_CkB = QtWidgets.QCheckBox(self.EL101_GB)
        self.EL101_pressure_act_CkB.setGeometry(QtCore.QRect(260, 50, 80, 20))
        self.EL101_pressure_act_CkB.setObjectName("EL101_pressure_act_CkB")
        self.EL101_flux_sep_LBL = QtWidgets.QLabel(self.EL101_GB)
        self.EL101_flux_sep_LBL.setGeometry(QtCore.QRect(150, 80, 10, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.EL101_flux_sep_LBL.setFont(font)
        self.EL101_flux_sep_LBL.setAlignment(QtCore.Qt.AlignCenter)
        self.EL101_flux_sep_LBL.setObjectName("EL101_flux_sep_LBL")
        self.EL101_flux_max_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_flux_max_DSB.setGeometry(QtCore.QRect(160, 80, 80, 20))
        self.EL101_flux_max_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_flux_max_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_flux_max_DSB.setPrefix("")
        self.EL101_flux_max_DSB.setDecimals(1)
        self.EL101_flux_max_DSB.setMinimum(0.0)
        self.EL101_flux_max_DSB.setMaximum(50.0)
        self.EL101_flux_max_DSB.setProperty("value", 5.0)
        self.EL101_flux_max_DSB.setObjectName("EL101_flux_max_DSB")
        self.EL101_flux_min_DSB = QtWidgets.QDoubleSpinBox(self.EL101_GB)
        self.EL101_flux_min_DSB.setGeometry(QtCore.QRect(70, 80, 80, 20))
        self.EL101_flux_min_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EL101_flux_min_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.EL101_flux_min_DSB.setPrefix("")
        self.EL101_flux_min_DSB.setDecimals(1)
        self.EL101_flux_min_DSB.setMinimum(0.0)
        self.EL101_flux_min_DSB.setMaximum(50.0)
        self.EL101_flux_min_DSB.setProperty("value", 0.0)
        self.EL101_flux_min_DSB.setObjectName("EL101_flux_min_DSB")
        self.EL101_flux_act_CkB = QtWidgets.QCheckBox(self.EL101_GB)
        self.EL101_flux_act_CkB.setGeometry(QtCore.QRect(260, 80, 80, 20))
        self.EL101_flux_act_CkB.setObjectName("EL101_flux_act_CkB")
        self.ok_PB = QtWidgets.QPushButton(self.centralwidget)
        self.ok_PB.setGeometry(QtCore.QRect(10, 410, 75, 23))
        self.ok_PB.setObjectName("ok_PB")
        self.cancel_PB = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_PB.setGeometry(QtCore.QRect(290, 410, 75, 23))
        self.cancel_PB.setObjectName("cancel_PB")
        settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 21))
        self.menubar.setObjectName("menubar")
        settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)
        settings.setTabOrder(self.EL101_power_min_DSB, self.EL101_power_max_DSB)
        settings.setTabOrder(self.EL101_power_max_DSB, self.EL101_power_act_CkB)
        settings.setTabOrder(self.EL101_power_act_CkB, self.EL101_pressure_min_DSB)
        settings.setTabOrder(self.EL101_pressure_min_DSB, self.EL101_pressure_max_DSB)
        settings.setTabOrder(self.EL101_pressure_max_DSB, self.EL101_pressure_act_CkB)
        settings.setTabOrder(self.EL101_pressure_act_CkB, self.EL101_flux_min_DSB)
        settings.setTabOrder(self.EL101_flux_min_DSB, self.EL101_flux_max_DSB)
        settings.setTabOrder(self.EL101_flux_max_DSB, self.EL101_flux_act_CkB)
        settings.setTabOrder(self.EL101_flux_act_CkB, self.ok_PB)
        settings.setTabOrder(self.ok_PB, self.cancel_PB)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "MainWindow"))
        self.EL101_GB.setTitle(_translate("settings", "EL-101"))
        self.EL101_P_sep_LBL.setText(_translate("settings", "-"))
        self.EL101_power_min_DSB.setPrefix(_translate("settings", "-"))
        self.EL101_power_min_DSB.setSuffix(_translate("settings", "%"))
        self.EL101_power_LBL.setText(_translate("settings", "Power"))
        self.EL101_pressure_LBL.setText(_translate("settings", "Pressure"))
        self.EL101_flux_LBL.setText(_translate("settings", "H2 flux"))
        self.EL101_power_max_DSB.setPrefix(_translate("settings", "+"))
        self.EL101_power_max_DSB.setSuffix(_translate("settings", "%"))
        self.EL101_power_act_CkB.setText(_translate("settings", "Activate"))
        self.EL101_pressure_sep_LBL.setText(_translate("settings", "-"))
        self.EL101_pressure_max_DSB.setSuffix(_translate("settings", " bar"))
        self.EL101_pressure_min_DSB.setSuffix(_translate("settings", " bar"))
        self.EL101_pressure_act_CkB.setText(_translate("settings", "Activate"))
        self.EL101_flux_sep_LBL.setText(_translate("settings", "-"))
        self.EL101_flux_max_DSB.setSuffix(_translate("settings", " Nm3/h"))
        self.EL101_flux_min_DSB.setSuffix(_translate("settings", " Nm3/h"))
        self.EL101_flux_act_CkB.setText(_translate("settings", "Activate"))
        self.ok_PB.setText(_translate("settings", "OK"))
        self.cancel_PB.setText(_translate("settings", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QMainWindow()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())
