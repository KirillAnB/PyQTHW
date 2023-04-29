from PySide6 import QtWidgets, QtCore

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Вход в приложение")
        size = QtCore.QSize(300, 100)
        self.resize(size)



if __name__ == '__main__':
    my_app = QtWidgets.QApplication()

    my_window = LoginWindow()
    my_window.show()
    my_app.exec()