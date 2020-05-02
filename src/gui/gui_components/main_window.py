# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 40, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.add_filter_button = QtWidgets.QPushButton(self.groupBox)
        self.add_filter_button.setGeometry(QtCore.QRect(100, 70, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_filter_button.setFont(font)
        self.add_filter_button.setObjectName("add_filter_button")
        self.filter_type_label = QtWidgets.QLabel(self.groupBox)
        self.filter_type_label.setGeometry(QtCore.QRect(10, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filter_type_label.setFont(font)
        self.filter_type_label.setObjectName("filter_type_label")
        self.add_filter_combo = QtWidgets.QComboBox(self.groupBox)
        self.add_filter_combo.setGeometry(QtCore.QRect(100, 30, 101, 22))
        self.add_filter_combo.setObjectName("add_filter_combo")
        self.report_generation_button = QtWidgets.QPushButton(self.centralwidget)
        self.report_generation_button.setGeometry(QtCore.QRect(520, 340, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.report_generation_button.setFont(font)
        self.report_generation_button.setObjectName("report_generation_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 40, 311, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.delete_filter_button = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_filter_button.setGeometry(QtCore.QRect(20, 240, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_filter_button.setFont(font)
        self.delete_filter_button.setObjectName("delete_filter_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CSV de resistencia"))
        self.groupBox.setTitle(_translate("MainWindow", "Crear filtro"))
        self.add_filter_button.setText(_translate("MainWindow", "Añadir"))
        self.filter_type_label.setText(_translate("MainWindow", "Tipo de filtro"))
        self.report_generation_button.setText(_translate("MainWindow", "Generar informe"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filtros"))
        self.delete_filter_button.setText(_translate("MainWindow", "Eliminar filtro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
