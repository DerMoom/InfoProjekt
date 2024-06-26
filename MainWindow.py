# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OpenButton.setGeometry(QtCore.QRect(410, 291, 580, 50))
        self.OpenButton.setText("")
        self.OpenButton.setFlat(True)
        self.OpenButton.setObjectName("OpenButton")
        self.CreateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CreateButton.setGeometry(QtCore.QRect(410, 421, 580, 50))
        self.CreateButton.setText("")
        self.CreateButton.setFlat(True)
        self.CreateButton.setObjectName("CreateButton")
        self.about_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.about_Button.setGeometry(QtCore.QRect(410, 551, 580, 50))
        self.about_Button.setText("")
        self.about_Button.setFlat(True)
        self.about_Button.setObjectName("about_Button")
        self.header_panel = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_panel.setGeometry(QtCore.QRect(-50, -50, 1050, 242))
        self.header_panel.setStyleSheet("background: #56855E;\n"
"border-radius: 50px;\n"
"")
        self.header_panel.setText("")
        self.header_panel.setObjectName("header_panel")
        self.Header_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Header_label.setGeometry(QtCore.QRect(20, 50, 281, 92))
        font = QtGui.QFont()
        font.setFamily("Atkinson Hyperlegible")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.Header_label.setFont(font)
        self.Header_label.setStyleSheet("/* Vocab-Trainer */\n"
"\n"
"position: absolute;\n"
"width: 632px;\n"
"height: 92px;\n"
"left: 20px;\n"
"top: 50px;\n"
"\n"
"font-family: \'Atkinson Hyperlegible\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 96px;\n"
"line-height: 119px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.Header_label.setObjectName("Header_label")
        self.authors_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.authors_label.setGeometry(QtCore.QRect(300, 96, 279, 36))
        self.authors_label.setStyleSheet("/* by Moritz and Thor */\n"
"\n"
"position: absolute;\n"
"width: 279px;\n"
"height: 36px;\n"
"left: 652px;\n"
"top: 96px;\n"
"\n"
"font-family: \'Atkinson Hyperlegible\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"display: flex;\n"
"align-items: flex-end;\n"
"\n"
"color: #E3DBA4;\n"
"\n"
"")
        self.authors_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.authors_label.setObjectName("authors_label")
        self.create_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.create_text.setGeometry(QtCore.QRect(410, 421, 580, 50))
        self.create_text.setStyleSheet("/* Create Set */\n"
"\n"
"position: absolute;\n"
"width: 580px;\n"
"height: 50px;\n"
"left: 410px;\n"
"top: 421px;\n"
"\n"
"font-family: \'Atkinson Hyperlegible\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 40px;\n"
"line-height: 50px;\n"
"/* identical to box height */\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #E3DBA4;\n"
"\n"
"")
        self.create_text.setObjectName("create_text")
        self.open_panel = QtWidgets.QLabel(parent=self.centralwidget)
        self.open_panel.setGeometry(QtCore.QRect(400, 266, 640, 100))
        self.open_panel.setStyleSheet("background: #56855E;\n"
"border-radius: 20px;\n"
"")
        self.open_panel.setText("")
        self.open_panel.setObjectName("open_panel")
        self.create_panel = QtWidgets.QLabel(parent=self.centralwidget)
        self.create_panel.setGeometry(QtCore.QRect(400, 396, 640, 100))
        self.create_panel.setStyleSheet("background: #56855E;\n"
"border-radius: 20px;\n"
"")
        self.create_panel.setText("")
        self.create_panel.setObjectName("create_panel")
        self.about_panel = QtWidgets.QLabel(parent=self.centralwidget)
        self.about_panel.setGeometry(QtCore.QRect(400, 526, 640, 100))
        self.about_panel.setStyleSheet("background: #56855E;\n"
"border-radius: 20px;\n"
"")
        self.about_panel.setText("")
        self.about_panel.setObjectName("about_panel")
        self.open_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.open_text.setGeometry(QtCore.QRect(410, 291, 580, 50))
        self.open_text.setStyleSheet("/* Open Set */\n"
"\n"
"position: absolute;\n"
"width: 580px;\n"
"height: 50px;\n"
"left: 410px;\n"
"top: 291px;\n"
"\n"
"font-family: \'Atkinson Hyperlegible\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 40px;\n"
"line-height: 50px;\n"
"/* identical to box height */\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #E3DBA4;\n"
"\n"
"")
        self.open_text.setObjectName("open_text")
        self.about_text = QtWidgets.QLabel(parent=self.centralwidget)
        self.about_text.setGeometry(QtCore.QRect(410, 551, 580, 50))
        self.about_text.setStyleSheet("/* Create Set */\n"
"\n"
"position: absolute;\n"
"width: 580px;\n"
"height: 50px;\n"
"left: 410px;\n"
"top: 421px;\n"
"\n"
"font-family: \'Atkinson Hyperlegible\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 40px;\n"
"line-height: 50px;\n"
"/* identical to box height */\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #E3DBA4;\n"
"\n"
"")
        self.about_text.setObjectName("about_text")
        self.logo_panel = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo_panel.setGeometry(QtCore.QRect(20, 300, 311, 291))
        self.logo_panel.setText("")
        self.logo_panel.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.logo_panel.setScaledContents(True)
        self.logo_panel.setObjectName("logo_panel")
        self.open_panel.raise_()
        self.open_text.raise_()
        self.OpenButton.raise_()
        self.header_panel.raise_()
        self.Header_label.raise_()
        self.authors_label.raise_()
        self.create_panel.raise_()
        self.about_panel.raise_()
        self.create_text.raise_()
        self.about_text.raise_()
        self.CreateButton.raise_()
        self.about_Button.raise_()
        self.logo_panel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
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
        self.actionCreate_Set = QtGui.QAction(parent=MainWindow)
        self.actionCreate_Set.setObjectName("actionCreate_Set")
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCreate_Set)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Intel Grabbers"))
        self.Header_label.setText(_translate("MainWindow", "Ferret"))
        self.authors_label.setText(_translate("MainWindow", "by Moritz & Thor"))
        self.create_text.setText(_translate("MainWindow", "Edit Set"))
        self.open_text.setText(_translate("MainWindow", "Open Set"))
        self.about_text.setText(_translate("MainWindow", "About Us"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Set.setText(_translate("MainWindow", "Create Set"))
