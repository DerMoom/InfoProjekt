# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.Header.setFont(font)
        self.Header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Header.setObjectName("Header")
        self.verticalLayout.addWidget(self.Header)
        self.OpenButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OpenButton.setObjectName("OpenButton")
        self.verticalLayout.addWidget(self.OpenButton)
        self.CreateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CreateButton.setObjectName("CreateButton")
        self.verticalLayout.addWidget(self.CreateButton)
        self.SettingsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SettingsButton.setObjectName("SettingsButton")
        self.verticalLayout.addWidget(self.SettingsButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Intel Grabbers"))
        self.Header.setText(_translate("MainWindow", "Intel Grabbers"))
        self.OpenButton.setText(_translate("MainWindow", "Open Set"))
        self.CreateButton.setText(_translate("MainWindow", "Create Set"))
        self.SettingsButton.setText(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
