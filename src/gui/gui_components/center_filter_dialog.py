# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'center_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CenterFilterDialog(object):
    def setupUi(self, CenterFilterDialog):
        CenterFilterDialog.setObjectName("CenterFilterDialog")
        CenterFilterDialog.setWindowModality(QtCore.Qt.WindowModal)
        CenterFilterDialog.resize(246, 89)
        font = QtGui.QFont()
        font.setPointSize(8)
        CenterFilterDialog.setFont(font)
        self.center_dialog_confirmation_button = QtWidgets.QDialogButtonBox(CenterFilterDialog)
        self.center_dialog_confirmation_button.setGeometry(QtCore.QRect(-140, 50, 341, 32))
        self.center_dialog_confirmation_button.setOrientation(QtCore.Qt.Horizontal)
        self.center_dialog_confirmation_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.center_dialog_confirmation_button.setObjectName("center_dialog_confirmation_button")
        self.center_dialog_center_value_label = QtWidgets.QLabel(CenterFilterDialog)
        self.center_dialog_center_value_label.setGeometry(QtCore.QRect(40, 20, 41, 20))
        self.center_dialog_center_value_label.setObjectName("center_dialog_center_value_label")
        self.center_dialog_center_input = QtWidgets.QLineEdit(CenterFilterDialog)
        self.center_dialog_center_input.setGeometry(QtCore.QRect(90, 20, 111, 20))
        self.center_dialog_center_input.setObjectName("center_dialog_center_input")

        self.retranslateUi(CenterFilterDialog)
        self.center_dialog_confirmation_button.accepted.connect(CenterFilterDialog.accept)
        self.center_dialog_confirmation_button.rejected.connect(CenterFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CenterFilterDialog)

    def retranslateUi(self, CenterFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        CenterFilterDialog.setWindowTitle(_translate("CenterFilterDialog", "Crear filtro de centro"))
        self.center_dialog_center_value_label.setText(_translate("CenterFilterDialog", "Centro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CenterFilterDialog = QtWidgets.QDialog()
    ui = Ui_CenterFilterDialog()
    ui.setupUi(CenterFilterDialog)
    CenterFilterDialog.show()
    sys.exit(app.exec_())
