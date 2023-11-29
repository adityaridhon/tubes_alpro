
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setStyleSheet("#mainframe{\n"
"background-color: rgb(0, 85, 127);\n"
"padding: 50px;\n"
"}\n"
"\n"
"#title{\n"
"color: white;\n"
"font-family: Poppins, \'sans-serif\';\n"
"font-size:40px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#subline{\n"
"color: white;\n"
"font-family: Poppins, \'sans-serif\';\n"
"font-size:20px;\n"
"}\n"
"\n"
"#startbtn{\n"
"background-color: rgb(85, 85, 127);\n"
"padding:8px;\n"
"border-radius:8px;\n"
"transition: 0.8s;\n"
"color:white;\n"
"font-size: 20px\n"
"}\n"
"\n"
"#startbtn:hover{\n"
"background-color: rgb(255, 170, 255);\n"
"}")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.subline = QtWidgets.QLabel(self.mainframe)
        self.subline.setMaximumSize(QtCore.QSize(16777215, 100))
        self.subline.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.subline.setObjectName("subline")
        self.gridLayout_2.addWidget(self.subline, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.mainframe)
        self.title.setMaximumSize(QtCore.QSize(16777215, 100))
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)
        self.startbtn = QtWidgets.QPushButton(self.mainframe)
        self.startbtn.setAutoExclusive(True)
        self.startbtn.setObjectName("startbtn")
        
        self.gridLayout_2.addWidget(self.startbtn, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.mainframe, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("STUDYMATE", "STUDYMATE"))
        self.subline.setText(_translate("MainWindow", "Selamat belajar di STUDYMATE, ayo kerjakan tugasmu!"))
        self.title.setText(_translate("MainWindow", "STUDYMATE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SubWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
