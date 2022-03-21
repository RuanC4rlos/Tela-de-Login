import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_login import Tela_Login
from tela_register import Tela_Register

class UiMain(QtWidgets.QWidget):

    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()


        self.tela_login = Tela_Login()
        self.tela_login.setupUi((self.stack0))

        self.tela_register = Tela_Register()
        self.tela_register.setupUi((self.stack1))

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)


class Main(QMainWindow, UiMain):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.tela_login.pushButton_login.clicked.connect(self.botaoLogin)
        self.tela_login.pushButton_register.clicked.connect(self.abrirTelaRegister)
        self.tela_register.pushButton_register.clicked.connect(self.botaoRegister)
        self.tela_register.pushButton_voltar.clicked.connect(self.botaoVoltar)
    def botaoLogin(self):
        senha = self.tela_login.lineEdit_password.text()
        nome = self.tela_login.lineEdit_user.text()

        with open('usuarios.txt','r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()

        with open( 'senhas.txt', 'r' ) as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n',''),usuarios))

        senhas = list( map( lambda x: x.replace( '\n', '' ),senhas) )

        logado = False

        for i in range(len(usuarios)):
            if nome == usuarios[i] and senha == senhas[i]:
                QMessageBox.information( None, 'POOII', 'Usuario Logado!' )
                logado = True

                self.tela_login.lineEdit_user.setText( '' )
                self.tela_login.lineEdit_password.setText( '' )

        if not logado:
            QMessageBox.information( None, 'POOII', 'Usuario ou senha incorreto!' )
            self.tela_login.lineEdit_user.setText( '' )
            self.tela_login.lineEdit_password.setText( '' )

    def botaoRegister(self):
        nome = self.tela_register.lineEdit_user.text()
        cpf = self.tela_register.lineEdit_cpf.text()
        nascimento = self.tela_register.lineEdit_nascimento.text()
        senha = self.tela_register.lineEdit_password.text()

        if not(nome == '' or senha == '' or cpf == '' or nascimento == '' ):

            #verifica se login e senha ja n estao cadastrados
            with open( 'usuarios.txt', 'r' ) as arquivoUsuario:
                usuarios = arquivoUsuario.readlines()

            with open( 'senhas.txt', 'r' ) as arquivoUsuario:
                senhas = arquivoUsuario.readlines()

            with open( 'cpf.txt', 'r' ) as arquivoUsuario:
                cpfs = arquivoUsuario.readlines()


            usuarios = list( map( lambda x: x.replace( '\n', '' ), usuarios ) )

            senhas = list( map( lambda x: x.replace( '\n', '' ), senhas ) )

            cpfs = list( map( lambda x: x.replace( '\n', '' ), cpfs ) )

            cadastro = False

            #Verifica se ja existe o cadastro
            for i in range( len( usuarios ) ):
                if nome == usuarios[i] and senha == senhas[i] or cpf == cpfs[i]:
                    cadastro = True

            if cadastro == False:
                #insere no arquivo
                with open('usuarios.txt','a') as arquivoUsuario:
                    arquivoUsuario.write(nome + '\n')

                with open('senhas.txt','a') as arquivoUsuario:
                    arquivoUsuario.write(senha + '\n')

                with open( 'cpf.txt', 'a' ) as arquivoUsuario:
                    arquivoUsuario.write(cpf + '\n' )

                with open( 'nascimento.txt', 'a' ) as arquivoUsuario:
                    arquivoUsuario.write(nascimento + '\n' )

                self.tela_register.lineEdit_user.setText( '' )
                self.tela_register.lineEdit_cpf.setText( '' )
                self.tela_register.lineEdit_nascimento.setText( '' )
                self.tela_register.lineEdit_password.setText( '' )
                QMessageBox.information( None, 'REGISTER', 'Registrado com sucesso!' )
            else:
                self.tela_register.lineEdit_user.setText( '' )
                self.tela_register.lineEdit_cpf.setText( '' )
                self.tela_register.lineEdit_nascimento.setText( '' )
                self.tela_register.lineEdit_password.setText( '' )
                QMessageBox.information( None, 'POOII', 'Login ou senha existentes!\nDigite novamente!' )
        else:
            QMessageBox.information(None,'POOII','Todos os valores devem ser preenchidos!')

    def botaoVoltar(self):
        self.tela_register.lineEdit_user.setText( '' )
        self.tela_register.lineEdit_cpf.setText( '' )
        self.tela_register.lineEdit_nascimento.setText( '' )
        self.tela_register.lineEdit_password.setText( '' )
        self.QtStack.setCurrentIndex( 0 )

    def abrirTelaRegister(self):
        self.QtStack.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())