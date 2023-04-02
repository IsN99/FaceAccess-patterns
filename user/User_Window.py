from PyQt5 import QtCore, QtGui, QtWidgets
import Client_User as Client_User

class Ui_Form(object):
    def setupUi(self, Form):     
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 381, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 171, 161))
        self.label_3.setStyleSheet("background_color = \"background-color: rgb(222, 221, 218);\"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 40, 171, 161))
        self.label_4.setStyleSheet("background_color = \"background-color: rgb(222, 221, 218);\"\n"
"border: 2px solid black;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(self.request_access)
        self.pushButton.clicked.connect(self.select_photo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окно пользователя"))
        self.label.setText(_translate("Form", "Ожидание..."))
        self.pushButton_2.setText(_translate("Form", "ЗАПРОСИТЬ ДОСТУП"))
        self.label_2.setText(_translate("Form", "Не выбрано"))
        self.pushButton.setText(_translate("Form", "Выбрать фото"))
        self.label_3.setText(_translate("Form", "Фото"))
        self.label_4.setText(_translate("Form", "Фото"))

    def request_access(self):
        client = Client_User.User_Client()
        # Запускаем метод access_request из User_Client, передав путь к выбранному файлу
        response = client.access_request(self.selected_photo)
        if response:
            pixmap = QtGui.QPixmap(response)
            # Получаем ширину QLabel
            label_width = self.label_4.width()
            # Масштабируем pixmap для подгонки размера к ширине QLabel
            scaled_pixmap = pixmap.scaledToWidth(label_width)
            # Устанавливаем масштабированный pixmap как изображение, отображаемое в метке
            self.label_4.setPixmap(scaled_pixmap)
            self.label.setText('ОДОБРЕНО')
        else:
            self.label_4.setText('Не распознано')
            self.label.setText('НЕТ ДОСТУПА')

    def select_photo(self):
        # Открываем диалог выбора файла и сохраняем путь к выбранному файлу
        self.selected_photo, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Выбрать файл', '.')
        self.label_2.setText(self.selected_photo)
        # Отображаем выбранное изображение в QLabel
        pixmap = QtGui.QPixmap(self.selected_photo)
        # Получаем ширину QLabel
        label_width = self.label_3.width()
        # Масштабируем изображение до ширины QLabel
        scaled_pixmap = pixmap.scaledToWidth(label_width)
        self.label_3.setPixmap(scaled_pixmap)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
