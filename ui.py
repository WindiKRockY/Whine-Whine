# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 420, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listfile_win = QtWidgets.QListWidget(self.centralwidget)
        self.listfile_win.setGeometry(QtCore.QRect(560, 90, 91, 311))
        self.listfile_win.setStyleSheet("color:black;\n"
"border:2 px solid black;\n"
"border-radius:10 px")
        self.listfile_win.setObjectName("listfile_win")
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(190, 420, 81, 41))
        self.left_btn.setObjectName("left_btn")
        self.right_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn_3.setGeometry(QtCore.QRect(290, 420, 81, 41))
        self.right_btn_3.setObjectName("right_btn_3")
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(560, 50, 91, 31))
        self.file.setObjectName("file")
        self.bw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bw_btn.setGeometry(QtCore.QRect(390, 420, 81, 41))
        self.bw_btn.setObjectName("bw_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(90, 420, 81, 41))
        self.right_btn.setObjectName("right_btn")
        self.sharp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sharp_btn.setGeometry(QtCore.QRect(480, 420, 81, 41))
        self.sharp_btn.setObjectName("sharp_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 50, 431, 341))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.left_btn.setText(_translate("MainWindow", "Left"))
        self.right_btn_3.setText(_translate("MainWindow", "Miror"))
        self.file.setText(_translate("MainWindow", "File"))
        self.bw_btn.setText(_translate("MainWindow", "B/W"))
        self.right_btn.setText(_translate("MainWindow", "Right"))
        self.sharp_btn.setText(_translate("MainWindow", "Sharpness"))
        self.label.setText(_translate("MainWindow", "Picture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
