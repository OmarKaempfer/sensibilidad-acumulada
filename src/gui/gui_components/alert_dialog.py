# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlertDialog(object):
    def setupUi(self, AlertDialog):
        AlertDialog.setObjectName("AlertDialog")
        AlertDialog.resize(284, 120)
        self.buttonBox = QtWidgets.QDialogButtonBox(AlertDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 80, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(AlertDialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 161, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AlertDialog)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AlertDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../res/Info_Circle_Symbol_Information_Letter-512.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(AlertDialog)
        self.buttonBox.accepted.connect(AlertDialog.accept)
        self.buttonBox.rejected.connect(AlertDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AlertDialog)

    def retranslateUi(self, AlertDialog):
        _translate = QtCore.QCoreApplication.translate
        AlertDialog.setWindowTitle(_translate("AlertDialog", "Error"))
        self.label.setText(_translate("AlertDialog", "No se ha podido crear el filtro:"))
        self.label_2.setText(_translate("AlertDialog", "Existen campos necesarios vacíos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlertDialog = QtWidgets.QDialog()
    ui = Ui_AlertDialog()
    ui.setupUi(AlertDialog)
    AlertDialog.show()
    sys.exit(app.exec_())
