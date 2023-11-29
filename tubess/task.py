import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class Ui_TaskWindow(object):
    def taskUi(self, MainWindow):
        MainWindow.setObjectName("TaskWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setMaximumSize(QtCore.QSize(16777215, 600))
        self.mainframe.setStyleSheet("#mainframe{\n"
"background-color: rgb(0, 85, 127);\n"
"padding: 40px;\n"
"font-family: Poppins, \'sans-serif\';\n"
"}\n"
"\n"
"#title{\n"
"color: white;\n"
"font-family: Poppins, \'sans-serif\';\n"
"font-size:40px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"#addtask {\n"
"padding:6px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"font-family: Poppins, \'sans-serif\';\n"
"border-radius:8px;\n"
"}\n"
"\n"
"#addtask:hover {\n"
"background-color: rgb(64, 129, 193);\n"
"}\n"
"\n"
"#removetask{\n"
"padding:6px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font-family: Poppins, \'sans-serif\';\n"
"border-radius:8px;\n"
"}\n"
"\n"
"#removetask:hover {\n"
"background-color: rgb(97, 0, 0);\n"
"}\n"
"\n"
"#history{\n"
"padding:6px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);\n"
"font-family: Poppins, \'sans-serif\';\n"
"border-radius:8px;\n"
"}\n"
"\n"
"#history:hover{\n"
"background-color: rgb(0, 90, 66);\n"
"}")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title = QtWidgets.QLabel(self.mainframe)
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)
        self.taskview = QtWidgets.QListView(self.mainframe)
        self.taskview.setMaximumSize(QtCore.QSize(16777215, 400))
        self.taskview.setObjectName("taskview")
        self.gridLayout_2.addWidget(self.taskview, 1, 0, 1, 1)
        self.addtask = QtWidgets.QPushButton(self.mainframe)
        self.addtask.setObjectName("addtask")
        self.gridLayout_2.addWidget(self.addtask, 2, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.removetask = QtWidgets.QPushButton(self.mainframe)
        self.removetask.setObjectName("removetask")
        self.gridLayout_2.addWidget(self.removetask, 3, 0, 1, 1)
        self.history = QtWidgets.QPushButton(self.mainframe)
        self.history.setObjectName("history")
        self.gridLayout_2.addWidget(self.history, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.mainframe, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TaskWindow", "TaskWindow"))
        self.title.setText(_translate("TaskWindow", "STUDYMATE"))
        self.addtask.setText(_translate("TaskWindow", "Tambah tugas"))
        self.removetask.setText(_translate("TaskWindow", "Hapus Tugas"))
        self.history.setText(_translate("TaskWindow", "Riwayat Tugas"))