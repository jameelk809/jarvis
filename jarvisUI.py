# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JARVIS(object):
    def setupUi(self, JARVIS):
        JARVIS.setObjectName("JARVIS")
        JARVIS.resize(1385, 892)
        self.centralwidget = QtWidgets.QWidget(JARVIS)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 1381, 881))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Downloads/images/212508.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1210, 800, 61, 31))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 800, 61, 31))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(14, 25, 401, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Downloads/images/00545cb7179c504433d4c8f5e845f286.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(670, 30, 351, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n" "border-radius:none;\n" "color:white;\n" "font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1030, 30, 351, 61))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n" "border-radius:none;\n" "color:white;\n" "font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1040, 610, 311, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Downloads/images/pngegg.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        JARVIS.setCentralWidget(self.centralwidget)

        self.retranslateUi(JARVIS)
        QtCore.QMetaObject.connectSlotsByName(JARVIS)

    def retranslateUi(self, JARVIS):
        _translate = QtCore.QCoreApplication.translate
        JARVIS.setWindowTitle(_translate("JARVIS", "MainWindow"))
        self.pushButton.setText(_translate("JARVIS", "Run"))
        self.pushButton_2.setText(_translate("JARVIS", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JARVIS = QtWidgets.QMainWindow()
    ui = Ui_JARVIS()
    ui.setupUi(JARVIS)
    JARVIS.show()
    sys.exit(app.exec_())