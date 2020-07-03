from PantallaInicial import *
from RegistroUsuario import *
import pymysql



class RegisterWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.buttonBox.accepted.connect(self.test_apply)
		self.buttonBox.rejected.connect(self.test_cancel)

	def test_apply(self):
		if self.contrasenaLineEdit.text()==self.confContrasenaLineEdit.text():
			#print(self.usuarioLineEdit.text(),self.correoElectronicoLineEdit.text(),self.numContactLineEdit.text(),self.contrasenaLineEdit.text())

			#query="""INSERT INTO User (user_name, user_email, user_phone, password) VALUES (%s, %s, %s, %s);""" % (self.usuarioLineEdit.text(),self.correoElectronicoLineEdit.text().replace("@", "%40"),self.numContactLineEdit.text(),self.contrasenaLineEdit.text())
			query="INSERT INTO User (user_name, user_email, user_phone, password) VALUES (%s, %s, %s, %s);"
			cursor.execute(query, (self.usuarioLineEdit.text(),self.correoElectronicoLineEdit.text().replace("@", "%40"),self.numContactLineEdit.text(),self.contrasenaLineEdit.text()))
			db.commit()		
			self.close()
		else:
			self.confContrasenaLabel.setText("Confirmar contraseña - Las contraseñas no son iguales")

	def test_cancel(self):
		self.close()

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.registerWindow=RegisterWindow()
		self.pushButton_2.clicked.connect(self.showRegister)
		self.pushButton.clicked.connect(self.login)

	def showRegister(self):
		self.registerWindow.show()

	def login(self):
		if self.lineEdit.text() and self.passwordLineEdit.text():	
			if cursor.execute("SELECT * FROM User WHERE user_name=%s AND password=%s", (self.lineEdit.text(), self.passwordLineEdit.text())):
				self.label.setText("Log In Correcto")
				pass
			else:
				self.label.setText("Log In Incorrecto")
		else:
			self.label.setText("Falta algún campo")


if __name__ == "__main__":
	db=pymysql.connect("sql7.freemysqlhosting.net","sql7352402","k3elt85NjB","sql7352402")
	cursor=db.cursor()
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()