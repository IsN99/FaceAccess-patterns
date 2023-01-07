from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow): #выполняет функцию конструктора
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(340, 120)
        self.MainWindow.setAutoFillBackground(True)
        self.MainWindow.setStyleSheet("colot: rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 321, 21))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 75 16pt \"MS Serif\";\n"
"color: rgb(0, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 321, 21))
        self.pushButton.setStyleSheet("font: 12pt \"MS Serif\";\n"
"color: rgb(0, 255, 255);\n"
"\n"
"border-top: 2px solid rgb(0, 255, 255);\n"
"border-left: 2px solid rgb(0, 255, 255);\n"
"border-right: 2px solid rgb(0, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 80, 321, 21))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Serif\";\n"
"color: rgb(0, 255, 255);\n"
"\n"
"border-top: 2px solid rgb(0, 255, 255);\n"
"border-left: 2px solid rgb(0, 255, 255);\n"
"border-right: 2px solid rgb(0, 255, 255);\n"
"border-bottom: 2px solid rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_functions()

        self.UserWindow = None
        self.managewind = None

        self.managewind = None
        self.ManagerWindow = None


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.label.setText(_translate("MainWindow", "ГЛАВНОЕ МЕНЮ"))
        self.pushButton.setText(_translate("MainWindow", "USER"))
        self.pushButton_2.setText(_translate("MainWindow", "MANAGER"))

    def button_functions (self):
        self.pushButton.clicked.connect(lambda: self.userf())
        self.pushButton_2.clicked.connect(lambda: self.managerf())

    def userf (self):
        from userwindow import Ui_UserWindow
        self.MainWindow.close()
        self.UserWindow = QtWidgets.QWidget()
        self.userwind = Ui_UserWindow()
        self.userwind.setupUi(self.UserWindow)
        self.UserWindow.show()


    def managerf (self):
        from managerwindow import Ui_Form
        self.MainWindow.close()
        self.ManagerWindow = QtWidgets.QWidget()
        self.managewind = Ui_Form()
        self.managewind.setupUi(self.ManagerWindow)
        self.ManagerWindow.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
