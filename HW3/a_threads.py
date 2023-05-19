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


# class SystemInfo(QtCore.QThread):
#     systemInfoReceived = QtCore.QThread(list) # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных
#
#     def run(self) -> None:  # TODO переопределить метод run
#         if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
#             self.delay = 1  # TODO то устанавливайте значение 1
#
#         while True:  # TODO Запустите бесконечный цикл получения информации о системе
#             cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
#             ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
#             self.systemInfoReceived.emit([cpu_value, ram_value]) # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
#             time.sleep(self.delay) # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


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
        while self.__status:
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """
            weather_response = requests.get(self.__api_url)
            weather_data = weather_response.json()
            print(weather_response.status_code)
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

