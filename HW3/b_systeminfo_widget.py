"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets
from a_threads import SystemInfo

class SysInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()
        self.initSysLogThread = SystemInfo()
        self.initLogToWidget()

    def initUi(self):
        self.setWindowTitle("System info window")

        self.cpuLabel = QtWidgets.QLabel("CPU usage")
        self.cpuUsageBar = QtWidgets.QProgressBar()
        self.cpuLayout = QtWidgets.QHBoxLayout()
        self.cpuLayout.addWidget(self.cpuLabel)
        self.cpuLayout.addWidget(self.cpuUsageBar)

        self.ramlabel = QtWidgets.QLabel("RAM usage")
        self.ramUsageBar = QtWidgets.QProgressBar()
        self.ramlayout = QtWidgets.QHBoxLayout()
        self.ramlayout.addWidget(self.ramlabel)
        self.ramlayout.addWidget(self.ramUsageBar)

        self.delayLabel = QtWidgets.QLabel("Delay: ")
        self.delayEdit = QtWidgets.QLineEdit()
        self.delayEdit.setPlaceholderText(str(1))
        self.delayEdit.setMaxLength(2)
        self.delayEdit.setFixedSize(25, 20)
        self.delayLayout = QtWidgets.QHBoxLayout()
        self.delayLayout.addWidget(self.delayLabel)
        self.delayLayout.addWidget(self.delayEdit)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.cpuLayout)
        self.mainLayout.addLayout(self.ramlayout)
        self.mainLayout.addLayout(self.delayLayout)
        self.setLayout(self.mainLayout)

    def initLogToWidget(self):
        self.initSysLogThread.systemInfoReceived.connect(self.onSignalReceived)
        self.initSysLogThread.start()

    def onSignalReceived(self, _list):
        self.cpuUsageBar.setValue(_list[0])
        self.ramUsageBar.setValue(_list[1])


    def initSignals(self):
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    sys_widget = SysInfoWidget()

    sys_widget.show()

    app.exec()
