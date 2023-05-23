

from PySide6 import QtWidgets
from b_systeminfo_widget import SysInfoWidget
from c_weatherapi_widget import WeatherWindow

class WeatherSystemWindow(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self) -> None:

        self.sysInfo = SysInfoWidget()
        self.weatherInfo = WeatherWindow()

        self.syslayout = QtWidgets.QHBoxLayout()
        self.syslayout.addWidget(self.sysInfo)

        self.weatherLayout = QtWidgets.QHBoxLayout()
        self.weatherLayout.addWidget(self.weatherInfo)

        self.sysFrame = QtWidgets.QFrame()
        self.sysFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sysFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sysFrame.setLayout(self.syslayout)

        self.weatherFrame = QtWidgets.QFrame()
        self.weatherFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weatherFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.weatherFrame.setLayout(self.weatherLayout)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.addWidget(self.sysFrame)
        self.mainLayout.addWidget(self.weatherFrame)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    many_windgets_window = WeatherSystemWindow()

    many_windgets_window.show()

    app.exec()