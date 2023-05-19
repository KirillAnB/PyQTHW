"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.settings = QtCore.QSettings("d_event_filter_settings")
        self.initUi()
        self.initSignals()
        self.initSettings()

    def initUi(self):
        self.ui.comboBox.addItem('hex')
        self.ui.comboBox.addItem('okt')
        self.ui.comboBox.addItem('bin')
        self.ui.comboBox.addItem('dec')
        self.ui.comboBox.setCurrentIndex(0)
    def initSignals(self):
        self.ui.comboBox.currentTextChanged.connect(self.comboBoxChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.hSliderMoved)
        self.ui.dial.valueChanged.connect(self.dialTurned)

    def initSettings(self):
        self.settings = QtCore.QSettings("d_event_filter_kiriand")
        self.ui.lcdNumber.display(self.settings.value('LCD', '0'))
        self.ui.comboBox.setCurrentText(self.settings.value('ComboBox', 'hex'))

    def comboBoxChanged(self):
        if self.ui.comboBox.currentText() == 'hex':
            self.ui.lcdNumber.setHexMode()
        if self.ui.comboBox.currentText() == 'okt':
            self.ui.lcdNumber.setOctMode()
        if self.ui.comboBox.currentText() == 'bin':
            self.ui.lcdNumber.setBinMode()
        if self.ui.comboBox.currentText() == 'dec':
            self.ui.lcdNumber.setDecMode()


    def hSliderMoved(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def dialTurned(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.ui.lcdNumber.display(self.ui.dial.value())

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == 61 or event.key() == 43:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        if event.key() == 45:
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings = QtCore.QSettings("d_event_filter_kiriand")
        self.settings.setValue('LCD', self.ui.lcdNumber.value())
        self.settings.setValue('ComboBox', self.ui.comboBox.currentText())




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
