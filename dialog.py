# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 451, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_dir = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dir.setObjectName("label_dir")
        self.horizontalLayout.addWidget(self.label_dir)
        self.terminologyDir = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.terminologyDir.setObjectName("terminologyDir")
        self.horizontalLayout.addWidget(self.terminologyDir)
        self.btn_browse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.terminologyTable = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.terminologyTable.setObjectName("terminologyTable")
        self.verticalLayout.addWidget(self.terminologyTable)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_dir.setText(_translate("Form", "Directory: "))
        self.btn_browse.setText(_translate("Form", "Browse"))

