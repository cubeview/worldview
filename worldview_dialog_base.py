# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worldview_dialog_base.ui'
#
# Created: Tue Jul 14 21:32:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WorldViewDialogBase(object):
    def setupUi(self, WorldViewDialogBase):
        WorldViewDialogBase.setObjectName(_fromUtf8("WorldViewDialogBase"))
        WorldViewDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(WorldViewDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(WorldViewDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), WorldViewDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), WorldViewDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(WorldViewDialogBase)

    def retranslateUi(self, WorldViewDialogBase):
        WorldViewDialogBase.setWindowTitle(_translate("WorldViewDialogBase", "Worldview", None))

