# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 210)
        self.header_label = QtWidgets.QLabel(parent=About)
        self.header_label.setGeometry(QtCore.QRect(0, 10, 400, 30))
        self.header_label.setObjectName("header_label")
        self.mainbody_label = QtWidgets.QLabel(parent=About)
        self.mainbody_label.setGeometry(QtCore.QRect(0, 50, 400, 150))
        self.mainbody_label.setObjectName("mainbody_label")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Us"))
        self.header_label.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">About Us</span></p></body></html>"))
        self.mainbody_label.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">This project was created for a school project by,</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Moritz Jüttner</span></p><p align=\"center\"><span style=\" font-size:10pt;\">&amp;</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Thor Poser</span></p><p align=\"center\"><span style=\" font-size:10pt;\">with the intent of making learning a fun and rewarding experience</span></p></body></html>"))