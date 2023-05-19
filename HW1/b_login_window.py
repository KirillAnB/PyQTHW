from PySide6 import QtWidgets, QtCore

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Вход в приложение")
        size = QtCore.QSize(300, 150)
        self.setFixedSize(size)

        login_label= QtWidgets.QLabel()
        login_label.setText("login")
        login_label.setMinimumWidth(45)


        password_label = QtWidgets.QLabel()
        password_label.setText("passowrd")
        password_label.setMinimumWidth(45)

        self.login_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layout_login = QtWidgets.QHBoxLayout()
        layout_login.addWidget(login_label)
        layout_login.addWidget(self.login_line_edit)
        layout_password = QtWidgets.QHBoxLayout()
        layout_password.addWidget(password_label)
        layout_password.addWidget(self.password_line_edit)

        self.push_button_registration = QtWidgets.QPushButton()
        self.push_button_registration.setText("Sing in")

        self.push_buttom_ok = QtWidgets.QPushButton("OK")
        self.push_button_chancel = QtWidgets.QPushButton("Chancel")


        layout_registartion = QtWidgets.QHBoxLayout()
        layout_registartion.addSpacerItem(QtWidgets.QSpacerItem(20, 10,QtWidgets.QSizePolicy.Policy.Expanding))
        layout_registartion.addWidget(self.push_button_registration)


        layout_handle = QtWidgets.QHBoxLayout()
        layout_handle.addSpacerItem(QtWidgets.QSpacerItem(20, 10,QtWidgets.QSizePolicy.Policy.Expanding))
        layout_handle.addWidget(self.push_buttom_ok)
        layout_handle.addWidget(self.push_button_chancel)

        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_login)
        layout_main.addLayout(layout_password)
        layout_main.addLayout(layout_registartion)
        layout_main.addLayout(layout_handle)


        self.setLayout(layout_main)






if __name__ == '__main__':
    my_app = QtWidgets.QApplication()

    my_window = LoginWindow()
    my_window.show()
    my_app.exec()