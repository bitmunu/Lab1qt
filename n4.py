from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.setWindowIcon(QtGui.QIcon('hehe.ico'))
        Dialog.resize(828, 642)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 250, 311, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(240, 70, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(240, 100, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(240, 130, 141, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(240, 160, 171, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ОКНО БЫСТРОГО ЗАКАЗА"))
        Dialog.setWindowIcon(QtGui.QIcon('hehe.ico'))
        self.checkBox.setText(_translate("Dialog", "Чизбургер"))
        self.checkBox_2.setText(_translate("Dialog", "Двойной чизбургер"))
        self.checkBox_3.setText(_translate("Dialog", "Тройной чизбургер"))
        self.checkBox_4.setText(_translate("Dialog", "ЧизбургЧизбургер"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def whe(self):
        x=""
        if self.checkBox.isChecked():
            x+="Чизбургер\n"
        if self.checkBox_2.isChecked():
            x+="Двойной Чизбургер\n"
        if self.checkBox_3.isChecked():
            x+="Тройной Чизбургер\n"
        if self.checkBox_4.isChecked():
            x+="ЧИЗБУРГ\n"

        self.plainTextEdit.setPlainText(x)


    def clicking(self):
        self.pushButton.clicked.connect(self.whe)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('hehe.ico'))
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.clicking()
    sys.exit(app.exec_())