# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sex_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SexFilterDialog(object):
    def setupUi(self, SexFilterDialog):
        SexFilterDialog.setObjectName("SexFilterDialog")
        SexFilterDialog.setWindowModality(QtCore.Qt.WindowModal)
        SexFilterDialog.resize(246, 90)
        font = QtGui.QFont()
        font.setPointSize(8)
        SexFilterDialog.setFont(font)
        self.sex_dialog_confirmation_button = QtWidgets.QDialogButtonBox(SexFilterDialog)
        self.sex_dialog_confirmation_button.setGeometry(QtCore.QRect(-140, 51, 341, 32))
        self.sex_dialog_confirmation_button.setOrientation(QtCore.Qt.Horizontal)
        self.sex_dialog_confirmation_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.sex_dialog_confirmation_button.setObjectName("sex_dialog_confirmation_button")
        self.sex_dialog_combo = QtWidgets.QComboBox(SexFilterDialog)
        self.sex_dialog_combo.setGeometry(QtCore.QRect(130, 20, 71, 22))
        self.sex_dialog_combo.setObjectName("sex_dialog_combo")
        self.sex_dialog_combo.addItem("")
        self.sex_dialog_combo.addItem("")
        self.sex_dialog_sex_value_label = QtWidgets.QLabel(SexFilterDialog)
        self.sex_dialog_sex_value_label.setGeometry(QtCore.QRect(91, 23, 31, 16))
        self.sex_dialog_sex_value_label.setObjectName("sex_dialog_sex_value_label")

        self.retranslateUi(SexFilterDialog)
        self.sex_dialog_confirmation_button.accepted.connect(SexFilterDialog.accept)
        self.sex_dialog_confirmation_button.rejected.connect(SexFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SexFilterDialog)

    def retranslateUi(self, SexFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        SexFilterDialog.setWindowTitle(_translate("SexFilterDialog", "Crear filtro de sexo"))
        self.sex_dialog_combo.setItemText(0, _translate("SexFilterDialog", "Hombre"))
        self.sex_dialog_combo.setItemText(1, _translate("SexFilterDialog", "Mujer"))
        self.sex_dialog_sex_value_label.setText(_translate("SexFilterDialog", "Sexo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SexFilterDialog = QtWidgets.QDialog()
    ui = Ui_SexFilterDialog()
    ui.setupUi(SexFilterDialog)
    SexFilterDialog.show()
    sys.exit(app.exec_())
