from PySide6 import QtWidgets, QtCore
from Ui_files.p1_home_work import Ui_MainWindow


class ControlPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация окна-панели управления
        :return:
        """
        pass

if __name__ == '__main__':
    my_app = QtWidgets.QApplication()

    my_window = ControlPanel()
    my_window.show()

    my_app.exec()
