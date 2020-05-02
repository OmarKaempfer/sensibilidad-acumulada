# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service_filter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServiceFilterDialog(object):
    def setupUi(self, ServiceFilterDialog):
        ServiceFilterDialog.setObjectName("ServiceFilterDialog")
        ServiceFilterDialog.setWindowModality(QtCore.Qt.WindowModal)
        ServiceFilterDialog.resize(246, 88)
        font = QtGui.QFont()
        font.setPointSize(8)
        ServiceFilterDialog.setFont(font)
        self.service_dialog_confirmation_button = QtWidgets.QDialogButtonBox(ServiceFilterDialog)
        self.service_dialog_confirmation_button.setGeometry(QtCore.QRect(-140, 50, 341, 32))
        self.service_dialog_confirmation_button.setOrientation(QtCore.Qt.Horizontal)
        self.service_dialog_confirmation_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.service_dialog_confirmation_button.setObjectName("service_dialog_confirmation_button")
        self.service_dialog_service_value_label = QtWidgets.QLabel(ServiceFilterDialog)
        self.service_dialog_service_value_label.setGeometry(QtCore.QRect(50, 20, 41, 20))
        self.service_dialog_service_value_label.setObjectName("service_dialog_service_value_label")
        self.service_dialog_service_input = QtWidgets.QLineEdit(ServiceFilterDialog)
        self.service_dialog_service_input.setGeometry(QtCore.QRect(100, 20, 111, 20))
        self.service_dialog_service_input.setObjectName("service_dialog_service_input")

        self.retranslateUi(ServiceFilterDialog)
        self.service_dialog_confirmation_button.accepted.connect(ServiceFilterDialog.accept)
        self.service_dialog_confirmation_button.rejected.connect(ServiceFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ServiceFilterDialog)

    def retranslateUi(self, ServiceFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        ServiceFilterDialog.setWindowTitle(_translate("ServiceFilterDialog", "Crear filtro de servicio"))
        self.service_dialog_service_value_label.setText(_translate("ServiceFilterDialog", "Servicio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServiceFilterDialog = QtWidgets.QDialog()
    ui = Ui_ServiceFilterDialog()
    ui.setupUi(ServiceFilterDialog)
    ServiceFilterDialog.show()
    sys.exit(app.exec_())
