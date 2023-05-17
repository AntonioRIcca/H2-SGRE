from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mb_set(object):

    def __init__(self):
        self.items = ['TT216', 'TT217', 'TT218', 'TT219', 'TT220', 'TT310',
                      'TI221', 'TI222', 'TI223', 'TI224', 'TI225', 'TI306',
                      'PI226', 'PI227', 'PI228', 'PI229', 'PI230', 'PI307']

        self.registers = []
        for i in range(0, 51):
            self.registers.append(str(i))
        # self.items = ['TT216']

        self.objects = []

    def setupUi(self, mb_set):
        mb_set.setObjectName('mb_set')
        mb_set.resize(1400, 1000)
        self.centralwidget = QtWidgets.QWidget(mb_set)
        self.centralwidget.setObjectName('centralwidget')
        x = 10
        y = 10
        for item in self.items:
            obj = item + '_LBL'
            self.__setattr__(obj, QtWidgets.QLabel(self.centralwidget))
            # self.TT216_LBL = QtWidgets.QLabel(self.centralwidget)
            # self.TT216_LBL.setGeometry(QtCore.QRect(x, y, 100, 20))
            self.__getattribute__(obj).setGeometry(QtCore.QRect(x, y, 100, 20))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.__getattribute__(obj).setFont(font)
            self.__getattribute__(obj).setObjectName(obj)
            self.__getattribute__(obj).setText(item)
            x = x + 70

            obj = item + '_ch_CB'
            self.__setattr__(obj,  QtWidgets.QComboBox(self.centralwidget))
            self.__getattribute__(obj).setGeometry(QtCore.QRect(x, y, 50, 20))
            self.__getattribute__(obj).setObjectName(obj)
            self.__getattribute__(obj).insertItems(0, ['21', '22', '31'])
            self.objects.append(self.__getattribute__(obj))
            x = x + 60

            obj = item + '_reg_CB'
            self.__setattr__(obj,  QtWidgets.QComboBox(self.centralwidget))
            self.__getattribute__(obj).setGeometry(QtCore.QRect(x, y, 50, 20))
            self.__getattribute__(obj).setObjectName(obj)
            self.__getattribute__(obj).insertItems(0, self.registers)
            self.objects.append(self.__getattribute__(obj))

            # self.a = QtWidgets.QComboBox(self.centralwidget)
            # self.a.insertItems(0, self.registers)
            # self.a.setCurrentText('4p')

            x = x + 60

            obj = item + '_scale_DSB'
            self.__setattr__(obj,  QtWidgets.QDoubleSpinBox(self.centralwidget))
            self.__getattribute__(obj).setGeometry(QtCore.QRect(x, y, 100, 20))
            self.__getattribute__(obj).setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.__getattribute__(obj).setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.__getattribute__(obj).setDecimals(10)
            self.__getattribute__(obj).setSingleStep(1e-06)
            self.__getattribute__(obj).setMinimum(0)
            self.__getattribute__(obj).setMaximum(1000)
            self.__getattribute__(obj).setObjectName(obj)
            self.objects.append(self.__getattribute__(obj))
            x = x + 110

            obj = item + '_offset_DSB'
            self.__setattr__(obj,  QtWidgets.QDoubleSpinBox(self.centralwidget))
            self.__getattribute__(obj).setGeometry(QtCore.QRect(x, y, 100, 20))
            self.__getattribute__(obj).setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.__getattribute__(obj).setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
            self.__getattribute__(obj).setDecimals(10)
            self.__getattribute__(obj).setSingleStep(1e-06)
            self.__getattribute__(obj).setMinimum(-1000)
            self.__getattribute__(obj).setMaximum(1000)
            self.__getattribute__(obj).setObjectName(obj)
            self.objects.append(self.__getattribute__(obj))
            x = x + 110

            # self.a = QtWidgets.QDoubleSpinBox(self.centralwidget)

            x = 10
            y = y + 30

        self.cancel_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_BTN.setGeometry(QtCore.QRect(10, y, 60, 20))
        self.cancel_BTN.setObjectName('cancel_BTN')
        self.cancel_BTN.setText('Cancel')

        self.confirm_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_BTN.setGeometry(QtCore.QRect(350, y, 60, 20))
        self.confirm_BTN.setObjectName('confirm_BTN')
        self.confirm_BTN.setText('Confirm')
        self.confirm_BTN.clicked.connect(self.test)
        # self.confirm_BTN.setTabOrder(1)

        mb_set.setCentralWidget(self.centralwidget)

        self.retranslateUi(mb_set)
        QtCore.QMetaObject.connectSlotsByName(mb_set)

        for i in range(0, len(self.objects)-1):
            mb_set.setTabOrder(self.objects[i], self.objects[i+1])

    def retranslateUi(self, mb_set):
        _translate = QtCore.QCoreApplication.translate
        mb_set.setWindowTitle(_translate("mb_set", "MainWindow"))
        # for item in self.items:
        #     self.__getattribute__(item + '_LBL').setText(_translate("mb_set", item))
        #     print('done ' + item)
        # self.TT217_LBL.setText(_translate("mb_set", 'item'))
        # self.TT216_LBL.setText('x')
        # self.TT217_LBL.setText('y')

    def test(self):
        print('test')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mb_set = QtWidgets.QMainWindow()
    ui = Ui_mb_set()
    ui.setupUi(mb_set)
    mb_set.show()
    sys.exit(app.exec_())