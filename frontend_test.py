# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frontend_test.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Lucida Sans"])
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.WidgetCanvas = QWidget(self.centralwidget)
        self.WidgetCanvas.setObjectName(u"WidgetCanvas")
        self.verticalLayout_2 = QVBoxLayout(self.WidgetCanvas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_2.addWidget(self.WidgetCanvas, 1, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)

        self.DataButton = QPushButton(self.widget)
        self.DataButton.setObjectName(u"DataButton")

        self.DeleteButton = QPushButton(self.widget)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.gridLayout.addWidget(self.DataButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.DeleteButton, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Lucida Sans"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.gridLayout_2.addWidget(self.widget_4, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data Series Visualizer", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data Generation", None))
    # retranslateUi

