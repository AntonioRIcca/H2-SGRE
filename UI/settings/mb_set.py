try:
    from .mb_set_ui import Ui_mb_set
except:
    from mb_set_ui import Ui_mb_set

from PyQt5 import QtWidgets, QtGui, QtCore
from _shared import variables as v


class MbSetting(QtWidgets.QMainWindow):
    def __init__(self):
        super(MbSetting, self).__init__()
        self.ui = Ui_mb_set()
        self.ui.setupUi(self)

        self.items = ['TT216', 'TT217', 'TT218', 'TT219', 'TT220', 'TT310',
                      'TI221', 'TI222', 'TI223', 'TI224', 'TI225', 'TI306',
                      'PI226', 'PI227', 'PI228', 'PI229', 'PI230', 'PI307']

        self.first()

        # self.ui.confirm_BTN.clicked.connect(self.test)

        # self.ui.ok_PB.clicked.connect(self.data)
        # self.ui.cancel_PB.clicked.connect(self.close_window)

    def set_data(self):
        for item in self.items:
            self.ui.__getattribute__(item + '_ch_CB').setCurrentText(str(v.par[item]['mb']['ch']))
            self.ui.__getattribute__(item + '_reg_CB').setCurrentText(str(v.par[item]['mb']['reg']))
            self.ui.__getattribute__(item + '_scale_DSB').setValue(v.par[item]['mb']['scale'])
            self.ui.__getattribute__(item + '_offset_DSB').setValue(v.par[item]['mb']['offset'])

    def store_data(self):
        print('clicked')
        for item in self.items:
            v.par[item]['mb']['ch'] = int(self.ui.__getattribute__(item + '_ch_CB').currentText())
            v.par[item]['mb']['reg'] = int(self.ui.__getattribute__(item + '_reg_CB').currentText())
            v.par[item]['mb']['scale'] = self.ui.__getattribute__(item + '_scale_DSB').value()
            v.par[item]['mb']['offset'] = self.ui.__getattribute__(item + '_offset_DSB').value()
            print(v.par[item]['mb'])

    def first(self):
        self.set_data()
        self.ui.confirm_BTN.clicked.connect(self.store_data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mb_set = QtWidgets.QMainWindow()
    myapp = MbSetting()
    myapp.ui.setupUi(mb_set)
    mb_set.show()
    myapp.first()
    app.exec()
