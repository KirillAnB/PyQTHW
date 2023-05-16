"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore, QtGui
import time

from ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def getWindowState(self):
        if self.window().isActiveWindow():
            return 'Active window'
        elif self.window().isHidden():
            return 'Hidden window'
        elif self.window().isVisible():
            return 'Visible window'
        elif self.window().isEnabled():
            return 'Enabled window'
    def initSignals(self):
        self.ui.pushButtonGetData.clicked.connect(self.getCurrentData)
        self.ui.pushButtonLT.clicked.connect(self.moveToLeftTop)
        self.ui.pushButtonRT.clicked.connect(self.moveToRightTop)
        self.ui.pushButtonCenter.clicked.connect(self.moveToCenter)
        self.ui.pushButtonLB.clicked.connect(self.moveToLeftBottom)
        self.ui.pushButtonRB.clicked.connect(self.moveToRightBottom)
        self.ui.pushButtonMoveCoords.clicked.connect(self.goToNewPosition)
    def getCurrentData(self):
        windows_count = str(len(QtWidgets.QApplication.screens()))
        current_window = self.objectName()
        display_size = self.screen().availableSize()
        current_screen = self.screen().name()
        window_size = self.size()
        window_min_size = self.minimumSize()
        current_coordinates = (self.window().x(), self.window().y())
        window_center_coorinates = (self.window().x() + self.size().width()//2, self.window().y() + self.size().height()//2)
        window_state = self.getWindowState()
        status = f"""{time.ctime()}\nwindows count is {windows_count},\ncurrent window is {current_window},\ndisplay size is {display_size},\ncurrent screen is {current_screen},\nwindow size is {window_size},\nminimumu size is {window_min_size},\ncurrent coordinates are {current_coordinates},\nwindow center is at {window_center_coorinates},\nwindow state is {window_state},\n"""
        self.ui.plainTextEdit.setPlainText(status)

    def moveToCenter(self):
        window_size = self.screen().availableSize()
        x = (window_size.width()-self.size().width()) // 2
        y = (window_size.height() - self.size().height()) // 2
        self.move(x, y)

    def moveToLeftTop(self):
        self.move(0, 0)

    def moveToRightTop(self):
        screen = self.screen().availableGeometry()
        self.move(screen.width()-self.size().width(), 0)

    def moveToRightBottom(self):
        screen = self.screen().availableGeometry()
        self.move(screen.width()-self.size().width(), screen.height()-self.size().height())

    def moveToLeftBottom(self):
        screen = self.screen().availableGeometry()
        self.move(0, screen.height()-self.size().height())


    def goToNewPosition(self):
        old_x, old_y = self.window().x(), self.window().y()
        new_x, new_y = self.ui.spinBoxX.value(), self.ui.spinBoxY.value()
        self.move(new_x, new_y)


    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(time.ctime(),event.oldPos(), event.pos())

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(f'{time.ctime()} resized\nnew size is {self.size()}')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
