from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from gui.gui_components.main_window import Ui_MainWindow  # importing our generated file
from gui.gui_components.age_filter_dialog import Ui_AgeFilterDialog
from gui.gui_components.sex_filter_dialog import Ui_SexFilterDialog
from gui.gui_components.center_filter_dialog import Ui_CenterFilterDialog
from gui.gui_components.service_filter_dialog import Ui_ServiceFilterDialog
from gui.gui_components.alert_dialog import Ui_AlertDialog
from model.report_configuration import ReportConfiguration
from filters.filters import *
from report_generator import sensibilidad_acumulada
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, report_config):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.report_config = report_config
        self.ui.setupUi(self)
        self.ui.add_filter_combo.addItem('Edad')
        self.ui.add_filter_combo.addItem('Sexo')
        self.ui.add_filter_combo.addItem('Servicio')
        self.ui.add_filter_combo.addItem('Centro')
        self.ui.add_filter_button.clicked.connect(lambda: self.open_filter_dialog(self.ui.add_filter_combo.currentText()))
        self.ui.report_generation_button.clicked.connect(lambda: sensibilidad_acumulada("C:/Users/omark/PycharmProjects/sensibilidad-acumulada/test_res/fourth_criteria/resistencia.csv", self.report_config))
        self.ui.delete_filter_button.clicked.connect(lambda: self.remove_filter(self.ui.listWidget.selectedItems()))

    def generate_report(self):

        sensibilidad_acumulada(
            "C:/Users/omark/PycharmProjects/sensibilidad-acumulada/test_res/fourth_criteria/resistencia.csv",
            self.report_config)

    def remove_filter(self, filters_list):
        for list_item in filters_list:
            report_configuration.filter_conditions.pop(list_item.text())
            self.ui.listWidget.takeItem(self.ui.listWidget.row(list_item))

    def open_age_filter_dialog(self):
        AgeFilterDialog = QtWidgets.QDialog()
        ui = Ui_AgeFilterDialog()
        ui.setupUi(AgeFilterDialog)
        self.setDisabled(True)
        AgeFilterDialog.show()

        rx = QRegExp("\d\d\d")
        ui.age_dialog_age_value_input.setValidator(QRegExpValidator(rx))

        response = AgeFilterDialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            if ui.age_dialog_age_value_input.text() == '':
                self.open_alert_dialog(AgeFilterDialog)
                self.open_age_filter_dialog()
                return
            filter_name = 'Edad ' + ui.age_dialog_combo.currentText() + ' ' + ui.age_dialog_age_value_input.text()
            self.report_config\
                .add_filter_condition(filter_name,
                                      get_age_filter_condition(ui.age_dialog_age_value_input.text(), ui.age_dialog_combo.currentText()))
            self.ui.listWidget.addItem(filter_name)
        self.setDisabled(False)

    def open_alert_dialog(self, parent_window):
        AlertDialog = QtWidgets.QDialog()
        ui = Ui_AlertDialog()
        ui.setupUi(AlertDialog)
        parent_window.setDisabled(True)
        AlertDialog.show()
        AlertDialog.exec_()

    def open_sex_filter_dialog(self):
        SexFilterDialog = QtWidgets.QDialog()
        ui = Ui_SexFilterDialog()
        ui.setupUi(SexFilterDialog)
        self.setDisabled(True)
        SexFilterDialog.show()
        response = SexFilterDialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            filter_name = 'Sexo: ' + ui.sex_dialog_combo.currentText()
            self.report_config.add_filter_condition(filter_name, get_sex_condition(ui.sex_dialog_combo.currentText()))
            self.ui.listWidget.addItem(filter_name)
        self.setDisabled(False)
        return

    def open_service_filter_dialog(self):
        ServiceFilterDialog = QtWidgets.QDialog()
        ui = Ui_ServiceFilterDialog()
        ui.setupUi(ServiceFilterDialog)
        self.setDisabled(True)
        ServiceFilterDialog.show()
        response = ServiceFilterDialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            if ui.service_dialog_service_input.text() == '':
                self.open_alert_dialog(ServiceFilterDialog)
                self.open_age_filter_dialog()
                return
            filter_name = 'Servicio: ' + ui.service_dialog_service_input.text()
            self.report_config.add_filter_condition(filter_name, get_service_condition(ui.service_dialog_service_input.text()))
            self.ui.listWidget.addItem(filter_name)
        self.setDisabled(False)
        return

    def open_center_filter_dialog(self):
        CenterFilterDialog = QtWidgets.QDialog()
        ui = Ui_CenterFilterDialog()
        ui.setupUi(CenterFilterDialog)
        self.setDisabled(True)
        CenterFilterDialog.show()
        response = CenterFilterDialog.exec_()
        if response == QtWidgets.QDialog.Accepted:
            if ui.center_dialog_center_input.text() == '':
                self.open_alert_dialog(CenterFilterDialog)
                self.open_age_filter_dialog()
                return
            filter_name = 'Centro: ' + ui.center_dialog_center_input.text()
            self.report_config.add_filter_condition(filter_name, get_center_condition(ui.center_dialog_center_input.text()))
            self.ui.listWidget.addItem(filter_name)
        self.setDisabled(False)
        return

    def open_filter_dialog(self, filter_type):
        if filter_type == 'Edad':
            return self.open_age_filter_dialog()
        if filter_type == 'Sexo':
            return self.open_sex_filter_dialog()
        if filter_type == 'Servicio':
            return self.open_service_filter_dialog()
        if filter_type == 'Centro':
            return self.open_center_filter_dialog()


app = QtWidgets.QApplication([])
report_configuration = ReportConfiguration()
application = MainWindow(report_configuration)
application.show()

sys.exit(app.exec())
