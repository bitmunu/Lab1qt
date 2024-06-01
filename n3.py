from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Калькулятор")
        Dialog.resize(689, 422)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 120, 111, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 180, 111, 51))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(490, 80, 111, 51))
        self.lcdNumber.setObjectName("lcdNumber")


        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(490, 200, 111, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(490, 140, 111, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_4.setGeometry(QtCore.QRect(490, 260, 111, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(390, 90, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 150, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 210, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(390, 270, 81, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 51, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Калькулятор", "Dialog"))
        self.label.setText(_translate("Калькулятор", "Сумма"))
        self.label_2.setText(_translate("Калькулятор", "Разность"))
        self.label_3.setText(_translate("Калькулятор", "Произведение"))
        self.label_4.setText(_translate("Калькулятор", "Частное"))
        self.pushButton.setText(_translate("Калькулятор", "GO"))


    def whee(self):

        if self.plainTextEdit_2.toPlainText() != "0":
            sum= str((int(self.plainTextEdit.toPlainText()) + int(self.plainTextEdit_2.toPlainText())))
            print(sum)
            anti_sum= str((int(self.plainTextEdit.toPlainText()) - int(self.plainTextEdit_2.toPlainText())))
            multiplication= str((int(self.plainTextEdit.toPlainText()) * int(self.plainTextEdit_2.toPlainText())))
            slash= str((int(self.plainTextEdit.toPlainText()) / int(self.plainTextEdit_2.toPlainText())))
            self.lcdNumber.display(sum)
            self.lcdNumber_3.display(anti_sum)
            self.lcdNumber_2.display(multiplication)
            self.lcdNumber_4.display(slash)

        else:
            self.plainTextEdit.setPlainText("ПОЖАЛУЙСТА введите число НЕ РАВНОЕ 0 в окно снизу")



    def clicking(self):
        self.pushButton.clicked.connect(self.whee)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.clicking()
    sys.exit(app.exec_())