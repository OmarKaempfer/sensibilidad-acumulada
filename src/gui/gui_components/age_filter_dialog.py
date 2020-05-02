# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'age_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgeFilterDialog(object):
    def setupUi(self, AgeFilterDialog):
        AgeFilterDialog.setObjectName("AgeFilterDialog")
        AgeFilterDialog.setWindowModality(QtCore.Qt.WindowModal)
        AgeFilterDialog.resize(246, 109)
        font = QtGui.QFont()
        font.setPointSize(8)
        AgeFilterDialog.setFont(font)
        self.age_dialog_confirmation_button = QtWidgets.QDialogButtonBox(AgeFilterDialog)
        self.age_dialog_confirmation_button.setGeometry(QtCore.QRect(-150, 60, 341, 32))
        self.age_dialog_confirmation_button.setOrientation(QtCore.Qt.Horizontal)
        self.age_dialog_confirmation_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.age_dialog_confirmation_button.setObjectName("age_dialog_confirmation_button")
        self.age_dialog_combo = QtWidgets.QComboBox(AgeFilterDialog)
        self.age_dialog_combo.setGeometry(QtCore.QRect(100, 20, 31, 22))
        self.age_dialog_combo.setObjectName("age_dialog_combo")
        self.age_dialog_combo.addItem("")
        self.age_dialog_combo.addItem("")
        self.age_dialog_age_value_label = QtWidgets.QLabel(AgeFilterDialog)
        self.age_dialog_age_value_label.setGeometry(QtCore.QRect(60, 20, 31, 16))
        self.age_dialog_age_value_label.setObjectName("age_dialog_age_value_label")
        self.age_dialog_age_value_input = QtWidgets.QLineEdit(AgeFilterDialog)
        self.age_dialog_age_value_input.setGeometry(QtCore.QRect(140, 20, 31, 21))
        self.age_dialog_age_value_input.setInputMask("")
        self.age_dialog_age_value_input.setObjectName("age_dialog_age_value_input")

        self.retranslateUi(AgeFilterDialog)
        self.age_dialog_confirmation_button.accepted.connect(AgeFilterDialog.accept)
        self.age_dialog_confirmation_button.rejected.connect(AgeFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AgeFilterDialog)

    def retranslateUi(self, AgeFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        AgeFilterDialog.setWindowTitle(_translate("AgeFilterDialog", "Crear filtro de edad"))
        self.age_dialog_combo.setItemText(0, _translate("AgeFilterDialog", ">"))
        self.age_dialog_combo.setItemText(1, _translate("AgeFilterDialog", "<"))
        self.age_dialog_age_value_label.setText(_translate("AgeFilterDialog", "Edad"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgeFilterDialog = QtWidgets.QDialog()
    ui = Ui_AgeFilterDialog()
    ui.setupUi(AgeFilterDialog)
    AgeFilterDialog.show()
    sys.exit(app.exec_())
