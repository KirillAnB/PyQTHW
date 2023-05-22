"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
from PySide6 import QtWidgets
from a_threads import WeatherHandler
import time

class WeatherWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()


    def initUi(self):

        self.latLabel = QtWidgets.QLabel("Lat.")
        self.latEdit = QtWidgets.QLineEdit()

        self.longLable = QtWidgets.QLabel("Long.")
        self.longEdit = QtWidgets.QLineEdit()

        self.delayLabel = QtWidgets.QLabel("Delay")
        self.delayEdit = QtWidgets.QLineEdit()
        self.delayEdit.setMaximumWidth(30)
        self.delayEdit.setPlaceholderText('5')

        self.latLonDelayLayout = QtWidgets.QHBoxLayout()
        self.latLonDelayLayout.addWidget(self.latLabel)
        self.latLonDelayLayout.addWidget(self.latEdit)
        self.latLonDelayLayout.addWidget(self.longLable)
        self.latLonDelayLayout.addWidget(self.longEdit)
        self.latLonDelayLayout.addWidget(self.delayLabel)
        self.latLonDelayLayout.addWidget(self.delayEdit)

        self.weatherDataText = QtWidgets.QTextEdit()

        self.getWeaterButton = QtWidgets.QPushButton("Get weather")
        self.stopButton = QtWidgets.QPushButton("Stop thread")

        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.addWidget(self.getWeaterButton)
        self.buttonsLayout.addWidget(self.stopButton)

        self.mainWeaterLayout = QtWidgets.QVBoxLayout()
        self.mainWeaterLayout.addLayout(self.latLonDelayLayout)
        self.mainWeaterLayout.addWidget(self.weatherDataText)
        self.mainWeaterLayout.addLayout(self.buttonsLayout)

        self.setLayout(self.mainWeaterLayout)


    def initSignals(self):

        self.getWeaterButton.clicked.connect(self.getWeaterButtonPushed)
        self.stopButton.clicked.connect(self.stopWeatherThread)

    def getWeaterButtonPushed(self):
        del self.weatherDataObject #не уверен в этом моменте, так пытаюсь не дать создать две очереди
        self.createWeatherThread()
        self.latEdit.setDisabled(True)
        self.longEdit.setDisabled(True)
        self.delayEdit.setDisabled(True)
        self.weatherDataObject.start()

    def createWeatherThread(self):
        if self.latEdit.text() and self.longEdit.text():
            lat, lon = float(self.latEdit.text()), float(self.longEdit.text())
        else:
            lat, lon = 9.179218458361987, 123.46353346347293

        self.weatherDataObject = WeatherHandler(lat, lon)
        if self.delayEdit.text():
            delay_value = int(self.delayEdit.text())
            self.weatherDataObject.setDelay(delay_value)
        self.weatherDataObject.weather_data_signal.connect(self.weatherDataEmitted)


    def weatherDataEmitted(self, _dict):

        self.weatherDataText.setText(f"{time.ctime()}, {str(_dict)}")

    def stopWeatherThread(self):
        try:
            self.weatherDataText.setText("........No threads running.......")
            self.latEdit.setDisabled(False)
            self.longEdit.setDisabled(False)
            self.delayEdit.setDisabled(False)
            self.weatherDataObject.setNoneStatus()
        except AttributeError:
            self.weatherDataText.setText("........No threads running.......")










if __name__ == '__main__':
    app = QtWidgets.QApplication()
    weatherWidget = WeatherWindow()

    weatherWidget.show()

    app.exec()
