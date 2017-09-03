# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git\QtDesigner\play_boy.ui'
#
# Created: Wed Jul 26 00:13:12 2017
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(262, 118)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "play_boy", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "玩个球", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "缩小 <-----", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "-----> 增大", None, QtGui.QApplication.UnicodeUTF8))

