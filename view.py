# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledRrDYmf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 612)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMaximumSize(QSize(16777215, 50))
        self.topbar.setFrameShape(QFrame.StyledPanel)
        self.topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.plot1btn = QPushButton(self.topbar)
        self.plot1btn.setObjectName(u"plot1btn")
        self.plot1btn.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.plot1btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.topbar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plot1 = QFrame(self.content)
        self.plot1.setObjectName(u"plot1")
        self.plot1.setFrameShape(QFrame.StyledPanel)
        self.plot1.setFrameShadow(QFrame.Raised)
        self.plotlayout = QVBoxLayout(self.plot1)
        self.plotlayout.setObjectName(u"plotlayout")

        self.horizontalLayout_2.addWidget(self.plot1)

        self.plot2 = QFrame(self.content)
        self.plot2.setObjectName(u"plot2")
        self.plot2.setFrameShape(QFrame.StyledPanel)
        self.plot2.setFrameShadow(QFrame.Raised)
        self.plotlayout2 = QVBoxLayout(self.plot2)
        self.plotlayout2.setObjectName(u"plotlayout2")

        self.horizontalLayout_2.addWidget(self.plot2)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plot1btn.setText(QCoreApplication.translate("MainWindow", u"Plot #1", None))
    # retranslateUi

