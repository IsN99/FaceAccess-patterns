from PyQt5 import QtCore, QtWidgets 
from Client_Manager import Manager_Client 
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 450)
        Form.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 261, 401))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(Form)
        self.tableView_2.setGeometry(QtCore.QRect(280, 40, 261, 401))
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 10, 261, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 10, 261, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(555, 10, 171, 431))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")  
        self.lineEdit.setPlaceholderText('Name')            
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText('Id')
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText('Name')
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")    
        self.lineEdit_4.setPlaceholderText('Id')   
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText('Id')  
        self.verticalLayout_4.addWidget(self.lineEdit_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(self.create)
        self.pushButton_4.clicked.connect(self.update)
        self.pushButton_5.clicked.connect(self.delete)
        self.pushButton_6.clicked.connect(self.restore)

        self.pushButton_7.clicked.connect(self.get_History)
        self.pushButton_8.clicked.connect(self.get_Empls)

        self.pushButton_3.clicked.connect(self.select_photo)
        self.pushButton.clicked.connect(self.select_photo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "Обновить"))
        self.pushButton_8.setText(_translate("Form", "Обновить"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))
        self.pushButton.setText(_translate("Form", "Файл фото"))
        self.pushButton_4.setText(_translate("Form", "Изменить"))
        self.pushButton_3.setText(_translate("Form", "Файл фото"))
        self.pushButton_5.setText(_translate("Form", "Удалить"))
        self.pushButton_6.setText(_translate("Form", "Восстановить"))

        
    
    def select_photo(self):
        # Открываем диалог выбора файла и сохраняем путь к выбранному файлу
        self.selected_photo, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Выбрать файл', '.')

    def create (self):
        try:
            manager = Manager_Client()
            manager.create(self.lineEdit.text(),self.selected_photo)
        except:
            pass
    
    def delete (self):
        try:
            manager = Manager_Client()
            manager.delete(self.lineEdit_4.text())
        except:
            pass

    def update (self):
        try:
            manager = Manager_Client()
            manager.update(self.lineEdit_2.text(),self.lineEdit_3.text(),self.selected_photo)
        except:
            pass

    def restore (self):
        try:
            manager = Manager_Client()
            manager.restore(self.lineEdit_5.text())
        except:
            pass

    def get_History (self):
        try:
            manager = Manager_Client()
            history = manager.get_history()

            model = QStandardItemModel(0, len(history[0]))
            header_labels = list(history[0].keys())
            model.setHorizontalHeaderLabels(header_labels)  
            for row, dictionary in enumerate(history):
                items = [QStandardItem(str(dictionary.get(key, ''))) for key in header_labels]
                model.appendRow(items)

            self.tableView.setModel(model)
            self.tableView.resizeColumnsToContents()
        except:
            pass

    def get_Empls (self):
        try:
            manager = Manager_Client()
            empls = manager.get_empls()

            model = QStandardItemModel(0, len(empls[0]))
            header_labels = list(empls[0].keys())
            model.setHorizontalHeaderLabels(header_labels)  
            for row, dictionary in enumerate(empls):
                items = [QStandardItem(str(dictionary.get(key, ''))) for key in header_labels]
                model.appendRow(items)

            self.tableView_2.setModel(model)
            self.tableView_2.resizeColumnsToContents()
        except:
            pass   
    

        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
