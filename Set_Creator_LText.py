# Form implementation generated from reading ui file 'Set_Creator_LText.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Set_Creator_LText(object):
    def setupUi(self, Set_Creator_LText):
        Set_Creator_LText.setObjectName("Set_Creator_LText")
        Set_Creator_LText.resize(600, 500)
        self.LText_textEdit = QtWidgets.QTextEdit(parent=Set_Creator_LText)
        self.LText_textEdit.setGeometry(QtCore.QRect(20, 40, 561, 181))
        self.LText_textEdit.setObjectName("LText_textEdit")
        self.LText_label = QtWidgets.QLabel(parent=Set_Creator_LText)
        self.LText_label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.LText_label.setObjectName("LText_label")

        self.retranslateUi(Set_Creator_LText)
        QtCore.QMetaObject.connectSlotsByName(Set_Creator_LText)

    def retranslateUi(self, Set_Creator_LText):
        _translate = QtCore.QCoreApplication.translate
        Set_Creator_LText.setWindowTitle(_translate("Set_Creator_LText", "Lückentext hinzufügen"))
        self.LText_label.setText(_translate("Set_Creator_LText", "Lückentext einfügen:"))
