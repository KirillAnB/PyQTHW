"""
Модуль в котором содержаться потоки Qt
"""

import time
import requests
import psutil
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__delay = None

    def setDelay(self, delay) -> None:

        self.__delay = delay


    def run(self) -> None:
        if self.__delay is None:
            self.__delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.__delay)


class WeatherHandler(QtCore.QThread):
    weather_data_signal = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 5
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        self.__status = True
        while self.__status:
            weather_response = requests.get(self.__api_url)
            weather_data = weather_response.json()
            self.weather_data_signal.emit(weather_data)
            time.sleep(self.__delay)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    my_weather = WeatherHandler(9.179218458361987, 123.46353346347293)
    my_weather.weather_data_signal.connect(lambda x: print(x))
    my_weather.start()
    window = Window()
    window.show()

    app.exec()

