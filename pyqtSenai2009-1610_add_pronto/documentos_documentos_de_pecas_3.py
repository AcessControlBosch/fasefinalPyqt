# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'documentos_documentos_de_pecas_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_peca03(object):
    def setupUi(self, peca03):
        peca03.setObjectName("peca03")
        peca03.resize(1290, 841)
        peca03.setMinimumSize(QtCore.QSize(1290, 841))
        peca03.setMaximumSize(QtCore.QSize(1290, 841))
        peca03.setStyleSheet("background-color: rgb(255, 255, 255);")
        peca03.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(peca03)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.label_numero_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_numero_3.setGeometry(QtCore.QRect(40, 30, 150, 150))
        self.label_numero_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_numero_3.setStyleSheet("\n"
"border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"font: 75 85pt \"Bosch Sans Bold\";\n"
"border-radius: 75px;\n"
"background-color: rgb(155, 228, 179);\n"
"\n"
"")
        self.label_numero_3.setScaledContents(False)
        self.label_numero_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_numero_3.setWordWrap(False)
        self.label_numero_3.setIndent(-1)
        self.label_numero_3.setObjectName("label_numero_3")
        self.botao_home = QtWidgets.QPushButton(self.centralwidget)
        self.botao_home.setGeometry(QtCore.QRect(1150, 10, 120, 120))
        self.botao_home.setStyleSheet("\n"
"border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;\n"
"font: 75 65pt \"Bosch Sans Bold\";\n"
"border-radius: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.botao_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/Home.Documentos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_home.setIcon(icon)
        self.botao_home.setIconSize(QtCore.QSize(105, 105))
        self.botao_home.setObjectName("botao_home")
        self.label_imagem = QtWidgets.QLabel(self.centralwidget)
        self.label_imagem.setGeometry(QtCore.QRect(560, 320, 121, 111))
        self.label_imagem.setObjectName("label_imagem")
        peca03.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(peca03)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        peca03.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(peca03)
        self.statusbar.setObjectName("statusbar")
        peca03.setStatusBar(self.statusbar)

        self.retranslateUi(peca03)
        QtCore.QMetaObject.connectSlotsByName(peca03)

    def retranslateUi(self, peca03):
        _translate = QtCore.QCoreApplication.translate
        peca03.setWindowTitle(_translate("peca03", "MainWindow"))
        self.label_numero_3.setText(_translate("peca03", "3"))
        self.label_imagem.setText(_translate("peca03", "imagem"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    peca03 = QtWidgets.QMainWindow()
    ui = Ui_peca03()
    ui.setupUi(peca03)
    peca03.show()
    sys.exit(app.exec_())