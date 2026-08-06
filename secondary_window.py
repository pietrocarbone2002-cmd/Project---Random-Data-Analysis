# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondary_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(615, 337)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sec_layout = QWidget(Dialog)
        self.sec_layout.setObjectName(u"sec_layout")
        self.gridLayout_4 = QGridLayout(self.sec_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.title = QLabel(self.sec_layout)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Lucida Sans"])
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.title, 0, 0, 1, 4)

        self.random_walk_radio = QRadioButton(self.sec_layout)
        self.random_walk_radio.setObjectName(u"random_walk_radio")

        self.gridLayout_4.addWidget(self.random_walk_radio, 1, 0, 1, 1)

        self.mean_reverting_radio = QRadioButton(self.sec_layout)
        self.mean_reverting_radio.setObjectName(u"mean_reverting_radio")

        self.gridLayout_4.addWidget(self.mean_reverting_radio, 1, 3, 1, 1)

        self.generate_data = QPushButton(self.sec_layout)
        self.generate_data.setObjectName(u"generate_data")

        self.gridLayout_4.addWidget(self.generate_data, 3, 1, 1, 2)

        self.RandomWalkWidget = QWidget(self.sec_layout)
        self.RandomWalkWidget.setObjectName(u"RandomWalkWidget")
        self.gridLayout_2 = QGridLayout(self.RandomWalkWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.start_value_enter = QLineEdit(self.RandomWalkWidget)
        self.start_value_enter.setObjectName(u"start_value_enter")

        self.gridLayout_2.addWidget(self.start_value_enter, 0, 1, 1, 1)

        self.start_value = QLabel(self.RandomWalkWidget)
        self.start_value.setObjectName(u"start_value")

        self.gridLayout_2.addWidget(self.start_value, 0, 0, 1, 1)

        self.steps_enter = QLineEdit(self.RandomWalkWidget)
        self.steps_enter.setObjectName(u"steps_enter")

        self.gridLayout_2.addWidget(self.steps_enter, 1, 1, 1, 1)

        self.bias_value_enter = QLineEdit(self.RandomWalkWidget)
        self.bias_value_enter.setObjectName(u"bias_value_enter")

        self.gridLayout_2.addWidget(self.bias_value_enter, 2, 1, 1, 1)

        self.bias_value = QLabel(self.RandomWalkWidget)
        self.bias_value.setObjectName(u"bias_value")

        self.gridLayout_2.addWidget(self.bias_value, 2, 0, 1, 1)

        self.steps_value = QLabel(self.RandomWalkWidget)
        self.steps_value.setObjectName(u"steps_value")

        self.gridLayout_2.addWidget(self.steps_value, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.RandomWalkWidget, 2, 0, 1, 2)

        self.MeanRevertingWidget = QWidget(self.sec_layout)
        self.MeanRevertingWidget.setObjectName(u"MeanRevertingWidget")
        self.gridLayout_3 = QGridLayout(self.MeanRevertingWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sigma_value_enter = QLineEdit(self.MeanRevertingWidget)
        self.sigma_value_enter.setObjectName(u"sigma_value_enter")

        self.gridLayout_3.addWidget(self.sigma_value_enter, 2, 1, 1, 1)

        self.steps_mr_enter = QLineEdit(self.MeanRevertingWidget)
        self.steps_mr_enter.setObjectName(u"steps_mr_enter")

        self.gridLayout_3.addWidget(self.steps_mr_enter, 1, 1, 1, 1)

        self.start_point = QLabel(self.MeanRevertingWidget)
        self.start_point.setObjectName(u"start_point")

        self.gridLayout_3.addWidget(self.start_point, 0, 0, 1, 1)

        self.start_point_enter = QLineEdit(self.MeanRevertingWidget)
        self.start_point_enter.setObjectName(u"start_point_enter")

        self.gridLayout_3.addWidget(self.start_point_enter, 0, 1, 1, 1)

        self.steps_mr = QLabel(self.MeanRevertingWidget)
        self.steps_mr.setObjectName(u"steps_mr")

        self.gridLayout_3.addWidget(self.steps_mr, 1, 0, 1, 1)

        self.sigma_value = QLabel(self.MeanRevertingWidget)
        self.sigma_value.setObjectName(u"sigma_value")

        self.gridLayout_3.addWidget(self.sigma_value, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.MeanRevertingWidget, 2, 2, 1, 2)

        self.MeanRevertingWidget.raise_()
        self.random_walk_radio.raise_()
        self.mean_reverting_radio.raise_()
        self.generate_data.raise_()
        self.title.raise_()
        self.RandomWalkWidget.raise_()

        self.gridLayout.addWidget(self.sec_layout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Data Generation", None))
        self.random_walk_radio.setText(QCoreApplication.translate("Dialog", u"Random Walk", None))
        self.mean_reverting_radio.setText(QCoreApplication.translate("Dialog", u"Mean Reverting", None))
        self.generate_data.setText(QCoreApplication.translate("Dialog", u"Generate Data", None))
        self.start_value.setText(QCoreApplication.translate("Dialog", u"Start Value", None))
        self.bias_value.setText(QCoreApplication.translate("Dialog", u"Bias", None))
        self.steps_value.setText(QCoreApplication.translate("Dialog", u"Number of steps", None))
        self.start_point.setText(QCoreApplication.translate("Dialog", u"Start Value", None))
        self.steps_mr.setText(QCoreApplication.translate("Dialog", u"Number of steps", None))
        self.sigma_value.setText(QCoreApplication.translate("Dialog", u"Sigma", None))
    # retranslateUi

