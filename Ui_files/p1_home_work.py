# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'P1home2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 888)
        self.actionAbout_control = QAction(MainWindow)
        self.actionAbout_control.setObjectName(u"actionAbout_control")
        self.actionAbout_QT = QAction(MainWindow)
        self.actionAbout_QT.setObjectName(u"actionAbout_QT")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1211, 825))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 630, 1041, 61))
        self.horizontalLayout_25 = QHBoxLayout(self.widget)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_25.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_25.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_25.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_25.addWidget(self.pushButton_7)

        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 48, 1061, 551))
        self.horizontalLayout_27 = QHBoxLayout(self.widget1)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)

        self.groupBox_9 = QGroupBox(self.widget1)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.radioButton = QRadioButton(self.groupBox_9)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_15.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_9)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_15.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_9)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_15.addWidget(self.radioButton_3)


        self.horizontalLayout_23.addWidget(self.groupBox_9)


        self.verticalLayout_17.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.groupBox_10 = QGroupBox(self.widget1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.checkBox = QCheckBox(self.groupBox_10)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_16.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_10)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_16.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_10)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_16.addWidget(self.checkBox_3)


        self.horizontalLayout_24.addWidget(self.groupBox_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_27.addLayout(self.verticalLayout_17)

        self.toolBox = QToolBox(self.widget1)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 526, 429))
        self.verticalLayout_19 = QVBoxLayout(self.page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_17 = QLabel(self.page)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_28.addWidget(self.label_17)

        self.lineEdit_5 = QLineEdit(self.page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QSize(300, 0))
        self.lineEdit_5.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_28.addWidget(self.lineEdit_5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_18 = QLabel(self.page)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_29.addWidget(self.label_18)

        self.lineEdit_6 = QLineEdit(self.page)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy1)
        self.lineEdit_6.setMinimumSize(QSize(300, 0))
        self.lineEdit_6.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_29.addWidget(self.lineEdit_6)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_23 = QLabel(self.page)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_30.addWidget(self.label_23)

        self.lineEdit_7 = QLineEdit(self.page)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setMinimumSize(QSize(300, 0))
        self.lineEdit_7.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_30.addWidget(self.lineEdit_7)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_24 = QLabel(self.page)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_31.addWidget(self.label_24)

        self.lineEdit_8 = QLineEdit(self.page)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setMinimumSize(QSize(300, 0))
        self.lineEdit_8.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_31.addWidget(self.lineEdit_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_31)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.toolBox.addItem(self.page, u"QLineEdit")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_33 = QHBoxLayout(self.page_3)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.textEdit_9 = QTextEdit(self.page_3)
        self.textEdit_9.setObjectName(u"textEdit_9")

        self.horizontalLayout_33.addWidget(self.textEdit_9)

        self.toolBox.addItem(self.page_3, u"QTextEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_34 = QHBoxLayout(self.page_4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.plainTextEdit = QPlainTextEdit(self.page_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_34.addWidget(self.plainTextEdit)

        self.toolBox.addItem(self.page_4, u"QPlainTextEdit")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 526, 429))
        self.horizontalLayout_26 = QHBoxLayout(self.page_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.calendarWidget = QCalendarWidget(self.page_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_26.addWidget(self.calendarWidget)

        self.toolBox.addItem(self.page_2, u"CalendarWidget")

        self.horizontalLayout_27.addWidget(self.toolBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setMinimumSize(QSize(400, 150))
        self.groupBox_2.setMaximumSize(QSize(400, 150))
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy4.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy4)
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy4.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy4)
        self.lineEdit_4.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_11.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setMinimumSize(QSize(300, 150))
        self.groupBox_3.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.textEdit = QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy5)
        self.textEdit.setMinimumSize(QSize(100, 20))
        self.textEdit.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.textEdit_2 = QTextEdit(self.groupBox_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy5.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy5)
        self.textEdit_2.setMinimumSize(QSize(200, 20))
        self.textEdit_2.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_9.addWidget(self.textEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.textEdit_3 = QTextEdit(self.groupBox_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy5.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy5)
        self.textEdit_3.setMinimumSize(QSize(200, 20))
        self.textEdit_3.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_8.addWidget(self.textEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.textEdit_4 = QTextEdit(self.groupBox_3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy5.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy5)
        self.textEdit_4.setMinimumSize(QSize(200, 20))
        self.textEdit_4.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_7.addWidget(self.textEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_11.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy6)
        self.groupBox_4.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.tableWidget = QTableWidget(self.groupBox_4)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        brush = QBrush(QColor(0, 255, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(brush);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        brush1 = QBrush(QColor(0, 254, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush1);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(250, 250, 8, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush3);
        __qtablewidgetitem14.setForeground(brush2);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_21.addWidget(self.tableWidget)


        self.horizontalLayout_11.addWidget(self.groupBox_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy7)
        self.groupBox_7.setMinimumSize(QSize(600, 0))
        self.layoutWidget_2 = QWidget(self.groupBox_7)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 30, 541, 24))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.textEdit_5 = QTextEdit(self.layoutWidget_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 22))
        self.textEdit_5.setFrameShape(QFrame.WinPanel)
        self.textEdit_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.textEdit_5)

        self.layoutWidget_3 = QWidget(self.groupBox_7)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 60, 541, 24))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.textEdit_6 = QTextEdit(self.layoutWidget_3)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMaximumSize(QSize(16777215, 22))
        self.textEdit_6.setFrameShape(QFrame.WinPanel)
        self.textEdit_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.textEdit_6)

        self.layoutWidget_4 = QWidget(self.groupBox_7)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 90, 541, 24))
        self.horizontalLayout_18 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.textEdit_7 = QTextEdit(self.layoutWidget_4)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMaximumSize(QSize(16777215, 22))
        self.textEdit_7.setFrameShape(QFrame.WinPanel)
        self.textEdit_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.textEdit_7)

        self.layoutWidget_5 = QWidget(self.groupBox_7)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(30, 120, 541, 24))
        self.horizontalLayout_19 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_19.addWidget(self.label_22)

        self.textEdit_8 = QTextEdit(self.layoutWidget_5)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setMaximumSize(QSize(16777215, 22))
        self.textEdit_8.setFrameShape(QFrame.WinPanel)
        self.textEdit_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.textEdit_8)


        self.verticalLayout_13.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.widget2 = QWidget(self.groupBox_8)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 40, 581, 110))
        self.horizontalLayout_13 = QHBoxLayout(self.widget2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSlider = QSlider(self.widget2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy8)
        self.verticalSlider.setMinimumSize(QSize(60, 0))
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_8.addWidget(self.verticalSlider)

        self.label_12 = QLabel(self.widget2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSlider_2 = QSlider(self.widget2)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy9)
        self.verticalSlider_2.setMinimumSize(QSize(60, 0))
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_9.addWidget(self.verticalSlider_2)

        self.label_13 = QLabel(self.widget2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSlider_3 = QSlider(self.widget2)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy9.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy9)
        self.verticalSlider_3.setMinimumSize(QSize(60, 0))
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.verticalLayout_10.addWidget(self.verticalSlider_3)

        self.label_14 = QLabel(self.widget2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_10.addWidget(self.label_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSlider_4 = QSlider(self.widget2)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        sizePolicy9.setHeightForWidth(self.verticalSlider_4.sizePolicy().hasHeightForWidth())
        self.verticalSlider_4.setSizePolicy(sizePolicy9)
        self.verticalSlider_4.setMinimumSize(QSize(60, 0))
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.verticalLayout_11.addWidget(self.verticalSlider_4)

        self.label_15 = QLabel(self.widget2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_11.addWidget(self.label_15)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSlider_5 = QSlider(self.widget2)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        sizePolicy9.setHeightForWidth(self.verticalSlider_5.sizePolicy().hasHeightForWidth())
        self.verticalSlider_5.setSizePolicy(sizePolicy9)
        self.verticalSlider_5.setMinimumSize(QSize(60, 0))
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.verticalLayout_12.addWidget(self.verticalSlider_5)

        self.label_16 = QLabel(self.widget2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_12.addWidget(self.label_16)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addWidget(self.groupBox_8)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy7)
        self.groupBox_5.setMinimumSize(QSize(200, 0))
        self.groupBox_5.setBaseSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar = QProgressBar(self.groupBox_5)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy9.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy9)
        self.progressBar.setValue(25)
        self.progressBar.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy7.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy7)
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.label_9)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar_2 = QProgressBar(self.groupBox_5)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy9.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy9)
        self.progressBar_2.setValue(50)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.progressBar_2)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy7.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy7)
        self.label_10.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.label_10)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.progressBar_3 = QProgressBar(self.groupBox_5)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy9.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy9)
        self.progressBar_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.progressBar_3.setValue(75)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_5.addWidget(self.progressBar_3)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.label_11)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy7.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy7)
        self.groupBox_6.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_14 = QPushButton(self.groupBox_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(75, 75))
        self.pushButton_14.setMaximumSize(QSize(75, 75))
        font = QFont()
        font.setPointSize(20)
        self.pushButton_14.setFont(font)

        self.horizontalLayout_22.addWidget(self.pushButton_14)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_6 = QPushButton(self.groupBox_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))
        self.pushButton_6.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setMaximumSize(QSize(75, 75))
        self.pushButton_5.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 75))
        self.pushButton_4.setMaximumSize(QSize(75, 75))
        self.pushButton_4.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addWidget(self.groupBox_6)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_20.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1231, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout_control)
        self.menuHelp.addAction(self.actionAbout_QT)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout_control.setText(QCoreApplication.translate("MainWindow", u"About control", None))
        self.actionAbout_QT.setText(QCoreApplication.translate("MainWindow", u"About QT", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Chancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"RadioButtons", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Suname", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ivanon", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ivan", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"father name", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ivanovich", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+7-111-111-11-11", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"CalendarWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Training", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Control panel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Pilots status", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Heartbeat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Blood Pressure", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pilot 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pilot 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pilot 3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"70", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"120/80", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"OK", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"72", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"125/85", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"OK", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"74", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"140/90", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Warning", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Engines status", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Engine 1", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">OK</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Engine 2", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00aa00;\">OK</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Engine 3", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#ffaa00;\">CHECK</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Engine 4", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00aa00;\">OK</span></p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"ENGINES THROTTLE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ENG 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ENG 2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ENG 3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ENG 4", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TOGA", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Fuel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tank 1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tank 2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tank 3", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Rudders", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Practice", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

