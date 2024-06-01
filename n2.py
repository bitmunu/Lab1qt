from PyQt5.QtWidgets import QApplication

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("1.2")
        Dialog.resize(689, 422)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(440, 120, 104, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 120, 104, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("CAT2", "CAT2"))
        self.plainTextEdit_2.setPlainText(_translate("CAT2", ""))
        self.pushButton.setText(_translate("CAT2", "ВЫЧИСЛИТЬ"))


    def whe(self):

        if self.plainTextEdit_2.toPlainText() is not None:
            x = str(eval(self.plainTextEdit_2.toPlainText()))
            self.plainTextEdit.setPlainText(x)
        else:
            self.plainTextEdit.setPlainText("ПОЖАЛУЙСТА введите выражение в окно слева")


    def clicking(self):
        self.pushButton.clicked.connect(self.whe)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.clicking()
    sys.exit(app.exec_())