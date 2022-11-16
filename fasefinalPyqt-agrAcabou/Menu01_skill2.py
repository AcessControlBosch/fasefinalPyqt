# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu01_skill2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu01_skill2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Menu01_limitado")
        MainWindow.resize(1290, 841)
        MainWindow.setMinimumSize(QtCore.QSize(1275, 841))
        MainWindow.setMaximumSize(QtCore.QSize(1290, 841))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Botao_Documentos = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Documentos.setGeometry(QtCore.QRect(790, 250, 171, 171))
        self.Botao_Documentos.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(0, 150, 232);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Documentos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/DOCUMENTOS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Documentos.setIcon(icon)
        self.Botao_Documentos.setIconSize(QtCore.QSize(160, 160))
        self.Botao_Documentos.setObjectName("Botao_Documentos")
        self.Botao_Liberar_Maquina = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Liberar_Maquina.setGeometry(QtCore.QRect(330, 250, 171, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Botao_Liberar_Maquina.sizePolicy().hasHeightForWidth())
        self.Botao_Liberar_Maquina.setSizePolicy(sizePolicy)
        self.Botao_Liberar_Maquina.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(0, 136, 74);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Liberar_Maquina.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagens/CADEADO_FECHADO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Liberar_Maquina.setIcon(icon1)
        self.Botao_Liberar_Maquina.setIconSize(QtCore.QSize(160, 160))
        self.Botao_Liberar_Maquina.setObjectName("Botao_Liberar_Maquina")
        self.Botao_Interface_Didatica = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Interface_Didatica.setGeometry(QtCore.QRect(560, 250, 171, 171))
        self.Botao_Interface_Didatica.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(213, 67, 203);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Interface_Didatica.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagens/INTERFACE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Interface_Didatica.setIcon(icon2)
        self.Botao_Interface_Didatica.setIconSize(QtCore.QSize(160, 160))
        self.Botao_Interface_Didatica.setObjectName("Botao_Interface_Didatica")
        self.Botao_Registros = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Registros.setGeometry(QtCore.QRect(460, 450, 174, 170))
        self.Botao_Registros.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(237, 0, 7);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Registros.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagens/REGISTROS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Registros.setIcon(icon3)
        self.Botao_Registros.setIconSize(QtCore.QSize(160, 160))
        self.Botao_Registros.setObjectName("Botao_Registros")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.Label_Menu_De_Usuario = QtWidgets.QLabel(self.centralwidget)
        self.Label_Menu_De_Usuario.setGeometry(QtCore.QRect(190, 60, 875, 121))
        self.Label_Menu_De_Usuario.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 65pt \"Bosch Sans Bold\";")
        self.Label_Menu_De_Usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Menu_De_Usuario.setObjectName("Label_Menu_De_Usuario")
        self.Label_Colaborador = QtWidgets.QLabel(self.centralwidget)
        self.Label_Colaborador.setGeometry(QtCore.QRect(60, 650, 591, 41))
        self.Label_Colaborador.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 15pt \"Bosch Sans Bold\";")
        self.Label_Colaborador.setObjectName("Label_Colaborador")
        self.Label_EDV = QtWidgets.QLabel(self.centralwidget)
        self.Label_EDV.setGeometry(QtCore.QRect(60, 700, 371, 41))
        self.Label_EDV.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 15pt \"Bosch Sans Bold\";")
        self.Label_EDV.setObjectName("Label_EDV")
        self.Botao_Sair = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Sair.setGeometry(QtCore.QRect(1080, 600, 161, 161))
        self.Botao_Sair.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(139, 34, 132);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Sair.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagens/SAIR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Sair.setIcon(icon4)
        self.Botao_Sair.setIconSize(QtCore.QSize(140, 140))
        self.Botao_Sair.setObjectName("Botao_Sair")
        self.Botao_Manutencao = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_Manutencao.setGeometry(QtCore.QRect(680, 450, 174, 170))
        self.Botao_Manutencao.setStyleSheet("QPushButton{\n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style: inside;\n"
"font: 75 9pt \"Bosch Sans Bold\";\n"
"background-color: rgb(237, 0, 7);\n"
"color: rgb(255, 207, 0);\n"
"}")
        self.Botao_Manutencao.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imagens/MANUTENCAO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Botao_Manutencao.setIcon(icon5)
        self.Botao_Manutencao.setIconSize(QtCore.QSize(160, 160))
        self.Botao_Manutencao.setObjectName("Botao_Manutencao")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Botao_Liberar_Maquina.setWhatsThis(_translate("Menu01_limitado", "<html><head/><body><p><br/></p></body></html>"))
        self.Label_Menu_De_Usuario.setText(_translate("Menu01_limitado", "MENU DE USUÁRIO"))
        self.Label_Colaborador.setText(_translate("Menu01_limitado", "COLABORADOR:"))
        self.Label_EDV.setText(_translate("Menu01_limitado", "EDV:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Menu01_skill2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
