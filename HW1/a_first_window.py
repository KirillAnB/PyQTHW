from PySide6 import QtWidgets, QtCore

class MyQtWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.show()
        self.setWindowTitle('My_First_Window_Title')
        # self.resize(QtCore.QSize(300, 150))
        size = QtCore.QSize()
        size.width()
        size.height()



if __name__ == '__main__':
    my_app = QtWidgets.QApplication()

    my_window = MyQtWindow()
    my_window.show()
    my_app.exec()