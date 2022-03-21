# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\blite\Desktop\RESGISTER FASE FINAL DO REGISTER.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Register(object):
    # css
    styleLineEditOk = ("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")

    styleLineEditError = ("QLineEdit {\n"
"    border: 2px solid rgb(255, 85, 127);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")

    # styleExitOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")

    # Funcao

    def checkFields(self):
        # CHECK USER
        if not self.lineEdit_user.text():
            self.lineEdit_user.setStyleSheet( self.styleLineEditError )
        else:
            self.lineEdit_user.setStyleSheet( self.styleLineEditOk )

        # CHECK CPF
        if not self.lineEdit_cpf.text():
            self.lineEdit_cpf.setStyleSheet( self.styleLineEditError )
        else:
            self.lineEdit_cpf.setStyleSheet( self.styleLineEditOk )

        # CHECK NASCIMENTO
        if not self.lineEdit_nascimento.text():
            self.lineEdit_nascimento.setStyleSheet( self.styleLineEditError )
        else:
            self.lineEdit_nascimento.setStyleSheet( self.styleLineEditOk )

        # CHECK PASSWORD
        if not self.lineEdit_password.text():
            self.lineEdit_password.setStyleSheet( self.styleLineEditError )
        else:
            self.lineEdit_password.setStyleSheet( self.styleLineEditOk )


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 790)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 260, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 425, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_voltar = QtWidgets.QPushButton(self.login_area)
        self.pushButton_voltar.setGeometry(QtCore.QRect(85, 490, 125, 50))
        self.pushButton_voltar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label = QtWidgets.QLabel(self.login_area)
        self.label.setGeometry(QtCore.QRect(100, 180, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_register = QtWidgets.QPushButton(self.login_area)
        self.pushButton_register.setGeometry(QtCore.QRect(239, 490, 125, 50))
        self.pushButton_register.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_register.setObjectName("pushButton_register")
        self.line = QtWidgets.QFrame(self.login_area)
        self.line.setGeometry(QtCore.QRect(225, 480, 2, 60))
        self.line.setMinimumSize(QtCore.QSize(2, 0))
        self.line.setWhatsThis("")
        self.line.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.login_area)
        self.frame.setGeometry(QtCore.QRect(165, 50, 121, 121))
        self.frame.setStyleSheet("image: url(:/newPrefix/ok.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(85, 315, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_cpf.setFont(font)
        self.lineEdit_cpf.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_cpf.setText("")
        self.lineEdit_cpf.setMaxLength(32)
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.lineEdit_nascimento = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_nascimento.setGeometry(QtCore.QRect(85, 370, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_nascimento.setFont(font)
        self.lineEdit_nascimento.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_nascimento.setText("")
        self.lineEdit_nascimento.setMaxLength(32)
        self.lineEdit_nascimento.setObjectName("lineEdit_nascimento")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Botao cor box
        self.pushButton_register.clicked.connect( self.checkFields )

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_voltar.setText(_translate("MainWindow", "VOLTAR"))
        self.label.setText(_translate("MainWindow", "USER REGISTER"))
        self.pushButton_register.setText(_translate("MainWindow", "REGISTER"))
        self.lineEdit_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEdit_nascimento.setPlaceholderText(_translate("MainWindow", "NASCIMENTO"))
        self.label_credits.setText(_translate("MainWindow", "Created by: Ruan Carlos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Register()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())