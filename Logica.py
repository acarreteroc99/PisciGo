from PantallaInicial import *
from RegistroUsuario import *
from menuPreBooking import *
from PreBusqueda import *
from infoPiscina import *
import pymysql

class informacion(QtWidgets.QMainWindow, Ui_MainWindowi):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)		


class preBusqueda(QtWidgets.QMainWindow, Ui_MainWindowe):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.infoPiscina=informacion()
		self.buttonBox.rejected.connect(self.cancel)
		self.buttonBox.accepted.connect(self.accept)

	def accept(self):
		if self.lineEdit.text() and cursor.execute("SELECT * FROM Pool WHERE idpool=%s", (self.lineEdit.text())):
			cursor.execute("SELECT * FROM Pool WHERE idpool=%s", (self.lineEdit.text()))
			data=cursor.fetchone()
			self.infoPiscina.label_14.setText(data[8])
			self.infoPiscina.label_2.setText(data[0])
			self.infoPiscina.label_4.setText(str(data[3]))
			self.infoPiscina.label_6.setText(str(data[5]))
			self.infoPiscina.label_8.setText(str(data[6]))
			self.infoPiscina.label_10.setText(str(data[10]))
			self.infoPiscina.label_12.setText(str(data[9]))
			self.infoPiscina.show()

	def cancel(self):
		self.close()


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

class menuIntermedio(QtWidgets.QMainWindow, Ui_MainWindows):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.preBusqueda=preBusqueda()
		self.commandLinkButton.clicked.connect(self.goPreBusqueda)

	def goPreBusqueda(self):
		self.preBusqueda.show()

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.registerWindow=RegisterWindow()
		self.intermedio=menuIntermedio()
		self.pushButton_2.clicked.connect(self.showRegister)
		self.pushButton.clicked.connect(self.login)

	def showRegister(self):
		self.registerWindow.show()

	def login(self):
		if self.lineEdit.text() and self.passwordLineEdit.text():	
			if cursor.execute("SELECT * FROM User WHERE user_name=%s AND password=%s", (self.lineEdit.text(), self.passwordLineEdit.text())):
				self.label.setText("Log In Correcto")
				self.intermedio.show()
				self.close()
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