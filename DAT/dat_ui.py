# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dat_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dat(object):
    def setupUi(self, dat):
        dat.setObjectName("dat")
        dat.resize(320, 280)
        dat.setMouseTracking(False)
        dat.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(dat)
        self.centralwidget.setObjectName("centralwidget")
        self.i1_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i1_DSB.setGeometry(QtCore.QRect(80, 20, 62, 20))
        self.i1_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i1_DSB.setReadOnly(True)
        self.i1_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i1_DSB.setDecimals(3)
        self.i1_DSB.setMaximum(20.0)
        self.i1_DSB.setObjectName("i1_DSB")
        self.di1_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di1_LBL.setGeometry(QtCore.QRect(190, 140, 80, 20))
        self.di1_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di1_LBL.setObjectName("di1_LBL")
        self.i2_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i2_LBL.setGeometry(QtCore.QRect(20, 50, 50, 20))
        self.i2_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i2_LBL.setObjectName("i2_LBL")
        self.i2_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i2_DSB.setGeometry(QtCore.QRect(80, 50, 62, 20))
        self.i2_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i2_DSB.setReadOnly(True)
        self.i2_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i2_DSB.setDecimals(3)
        self.i2_DSB.setMaximum(20.0)
        self.i2_DSB.setObjectName("i2_DSB")
        self.i4_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i4_DSB.setGeometry(QtCore.QRect(80, 110, 62, 20))
        self.i4_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i4_DSB.setReadOnly(True)
        self.i4_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i4_DSB.setDecimals(3)
        self.i4_DSB.setMaximum(20.0)
        self.i4_DSB.setObjectName("i4_DSB")
        self.i3_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i3_LBL.setGeometry(QtCore.QRect(20, 80, 50, 20))
        self.i3_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i3_LBL.setObjectName("i3_LBL")
        self.i3_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i3_DSB.setGeometry(QtCore.QRect(80, 80, 62, 20))
        self.i3_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i3_DSB.setReadOnly(True)
        self.i3_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i3_DSB.setDecimals(3)
        self.i3_DSB.setMaximum(20.0)
        self.i3_DSB.setObjectName("i3_DSB")
        self.i4_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i4_LBL.setGeometry(QtCore.QRect(20, 110, 50, 20))
        self.i4_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i4_LBL.setObjectName("i4_LBL")
        self.i8_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i8_LBL.setGeometry(QtCore.QRect(20, 230, 50, 20))
        self.i8_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i8_LBL.setObjectName("i8_LBL")
        self.i5_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i5_LBL.setGeometry(QtCore.QRect(20, 140, 50, 20))
        self.i5_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i5_LBL.setObjectName("i5_LBL")
        self.i6_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i6_DSB.setGeometry(QtCore.QRect(80, 170, 62, 20))
        self.i6_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i6_DSB.setReadOnly(True)
        self.i6_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i6_DSB.setDecimals(3)
        self.i6_DSB.setMaximum(20.0)
        self.i6_DSB.setObjectName("i6_DSB")
        self.i8_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i8_DSB.setGeometry(QtCore.QRect(80, 230, 62, 20))
        self.i8_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i8_DSB.setReadOnly(True)
        self.i8_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i8_DSB.setDecimals(3)
        self.i8_DSB.setMaximum(20.0)
        self.i8_DSB.setObjectName("i8_DSB")
        self.i5_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i5_DSB.setGeometry(QtCore.QRect(80, 140, 62, 20))
        self.i5_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i5_DSB.setReadOnly(True)
        self.i5_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i5_DSB.setDecimals(3)
        self.i5_DSB.setMaximum(20.0)
        self.i5_DSB.setObjectName("i5_DSB")
        self.i6_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i6_LBL.setGeometry(QtCore.QRect(20, 170, 50, 20))
        self.i6_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i6_LBL.setObjectName("i6_LBL")
        self.i7_DSB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.i7_DSB.setGeometry(QtCore.QRect(80, 200, 62, 20))
        self.i7_DSB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i7_DSB.setReadOnly(True)
        self.i7_DSB.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.i7_DSB.setDecimals(3)
        self.i7_DSB.setMaximum(20.0)
        self.i7_DSB.setObjectName("i7_DSB")
        self.i7_LBL = QtWidgets.QLabel(self.centralwidget)
        self.i7_LBL.setGeometry(QtCore.QRect(20, 200, 50, 20))
        self.i7_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.i7_LBL.setObjectName("i7_LBL")
        self.do1_PB = QtWidgets.QPushButton(self.centralwidget)
        self.do1_PB.setGeometry(QtCore.QRect(190, 20, 110, 20))
        self.do1_PB.setCheckable(True)
        self.do1_PB.setDefault(False)
        self.do1_PB.setObjectName("do1_PB")
        self.do2_PB = QtWidgets.QPushButton(self.centralwidget)
        self.do2_PB.setGeometry(QtCore.QRect(190, 50, 110, 20))
        self.do2_PB.setCheckable(True)
        self.do2_PB.setDefault(False)
        self.do2_PB.setObjectName("do2_PB")
        self.do3_PB = QtWidgets.QPushButton(self.centralwidget)
        self.do3_PB.setGeometry(QtCore.QRect(190, 80, 110, 20))
        self.do3_PB.setCheckable(True)
        self.do3_PB.setDefault(False)
        self.do3_PB.setObjectName("do3_PB")
        self.do4_PB = QtWidgets.QPushButton(self.centralwidget)
        self.do4_PB.setGeometry(QtCore.QRect(190, 110, 110, 20))
        self.do4_PB.setCheckable(True)
        self.do4_PB.setDefault(False)
        self.do4_PB.setObjectName("do4_PB")
        self.di2_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di2_LBL.setGeometry(QtCore.QRect(190, 170, 80, 20))
        self.di2_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di2_LBL.setObjectName("di2_LBL")
        self.di3_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di3_LBL.setGeometry(QtCore.QRect(190, 200, 80, 20))
        self.di3_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di3_LBL.setObjectName("di3_LBL")
        self.di4_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di4_LBL.setGeometry(QtCore.QRect(190, 230, 80, 20))
        self.di4_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di4_LBL.setObjectName("di4_LBL")
        self.di1_led_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di1_led_LBL.setGeometry(QtCore.QRect(280, 140, 20, 20))
        self.di1_led_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di1_led_LBL.setObjectName("di1_led_LBL")
        self.di4_led_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di4_led_LBL.setGeometry(QtCore.QRect(280, 230, 20, 20))
        self.di4_led_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di4_led_LBL.setObjectName("di4_led_LBL")
        self.di2_led_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di2_led_LBL.setGeometry(QtCore.QRect(280, 170, 20, 20))
        self.di2_led_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di2_led_LBL.setObjectName("di2_led_LBL")
        self.di3_led_LBL = QtWidgets.QLabel(self.centralwidget)
        self.di3_led_LBL.setGeometry(QtCore.QRect(280, 200, 20, 20))
        self.di3_led_LBL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.di3_led_LBL.setObjectName("di3_led_LBL")
        dat.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dat)
        self.statusbar.setObjectName("statusbar")
        dat.setStatusBar(self.statusbar)

        self.retranslateUi(dat)
        QtCore.QMetaObject.connectSlotsByName(dat)

    def retranslateUi(self, dat):
        _translate = QtCore.QCoreApplication.translate
        dat.setWindowTitle(_translate("dat", "MainWindow"))
        self.i1_DSB.setSuffix(_translate("dat", " mA"))
        self.di1_LBL.setText(_translate("dat", "Digital Input 1"))
        self.i2_LBL.setText(_translate("dat", "I_(2)"))
        self.i2_DSB.setSuffix(_translate("dat", " mA"))
        self.i4_DSB.setSuffix(_translate("dat", " mA"))
        self.i3_LBL.setText(_translate("dat", "I_(3)"))
        self.i3_DSB.setSuffix(_translate("dat", " mA"))
        self.i4_LBL.setText(_translate("dat", "I_(4)"))
        self.i8_LBL.setText(_translate("dat", "I_(8)"))
        self.i5_LBL.setText(_translate("dat", "I_(5)"))
        self.i6_DSB.setSuffix(_translate("dat", " mA"))
        self.i8_DSB.setSuffix(_translate("dat", " mA"))
        self.i5_DSB.setSuffix(_translate("dat", " mA"))
        self.i6_LBL.setText(_translate("dat", "I_(6)"))
        self.i7_DSB.setSuffix(_translate("dat", " mA"))
        self.i7_LBL.setText(_translate("dat", "I_(7)"))
        self.do1_PB.setText(_translate("dat", "Digital Output 1"))
        self.do2_PB.setText(_translate("dat", "Digital Output 2"))
        self.do3_PB.setText(_translate("dat", "Digital Output 3"))
        self.do4_PB.setText(_translate("dat", "Digital Output 4"))
        self.di2_LBL.setText(_translate("dat", "Digital Input 2"))
        self.di3_LBL.setText(_translate("dat", "Digital Input 3"))
        self.di4_LBL.setText(_translate("dat", "Digital Input 4"))
        self.di1_led_LBL.setText(_translate("dat", "led"))
        self.di4_led_LBL.setText(_translate("dat", "led"))
        self.di2_led_LBL.setText(_translate("dat", "led"))
        self.di3_led_LBL.setText(_translate("dat", "led"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dat = QtWidgets.QMainWindow()
    ui = Ui_dat()
    ui.setupUi(dat)
    dat.show()
    sys.exit(app.exec_())
