from py.PantallaInicial import *
from py.RegistroUsuario import *
from py.menuPreBooking import *
from py.PreBusqueda import *
from py.infoPiscina import *
from py.booking import *
from py.cancelarReserva import *
import pymysql, time
from datetime import datetime, timedelta

class cancel(QtWidgets.QMainWindow, Ui_MainWindoww):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.buttonBox.rejected.connect(self.cancel)
		self.buttonBox.accepted.connect(self.accept)


	def accept(self):
		fecha=self.dateEdit.date()
		if self.numContactLineEdit.text():
			if cursor.execute("SELECT * FROM Booking WHERE user_name=%s AND date=%s AND numPiscina=%s", (uss.username, fecha.toString("yyyy-MM-dd"), self.numContactLineEdit.text())):
				cursor.execute("DELETE FROM Booking WHERE user_name=%s AND date=%s AND numPiscina=%s", (uss.username, fecha.toString("yyyy-MM-dd"), self.numContactLineEdit.text()))
				db.commit()
				self.label.setText("Reserva Eliminada con Éxito")
				time.sleep(2)
				self.close()
			else:
				self.label.setText("No existe dicha reserva")
		else:
			self.label.setText("No se ha especificado código de piscina")

	def cancel(self):
		self.close()

class book(QtWidgets.QMainWindow, Ui_MainWindowx):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.reservar.clicked.connect(self.reserva)
		self.atras.clicked.connect(self.back)

	def back(self):
		self.close()

	def reserva(self):

		fecha=self.calendar.selectedDate()
		info=[fecha, self.timeEdit.time(), self.nPeopleSpinBox.value(), self.grater70SpinBox.value(), self.lower14SpinBox.value(), self.numPiscinas.text()]

		cursor.execute("SELECT capacity, opening_hour, max_time, closing_hour FROM Pool WHERE idpool=%s", (info[-1]))
		data=cursor.fetchone()

		if data is None:
			self.cajitaError.setText("ERROR: Ese codigo de piscina no existe")
		else:
			fechainicio=info[0].toString("MM/dd/yyyy")+" "+info[1].toString() #FECHA COMPLETA
			fechainiciodatetime=datetime.strptime(fechainicio,"%m/%d/%Y %H:%M:%S")
			delta=timedelta(hours=data[2])

			fechafinal=fechainiciodatetime+delta

			t = datetime.strptime(info[1].toString(),"%H:%M:%S") #HORA QUE PIDE
			tdelta=timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)

			if info[2]>0:
				if info[3]>0 and info[4]>0:
					self.cajitaError.setText("Reserva no realizada por seguridad entre edades")
				else:
					if timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)<data[1] or timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)>data[3]:
						self.cajitaError.setText("Está fuera del horario")
					else:
						cursor.execute("SELECT SUM(nPeople), SUM(lower14), SUM(greater70) FROM Booking WHERE numPiscina=%s AND date=%s AND time BETWEEN %s and %s", (info[-1], info[0].toString("yyyy-MM-dd"), fechainiciodatetime.strftime("%H:%M:%S"), fechafinal.strftime("%H:%M:%S")))
						totals=cursor.fetchone()
						if totals[0] is not None:
							print(totals)
							totalppl=totals[0]
							if info[2]>data[0]-totalppl:
								self.cajitaError.setText("Reserva no realizada por insuficiencia de capacidad")
							else:
								if ((totals[1]>0 and info[3]>0) or (totals[2]>0 and info[4]>0)):
									self.cajitaError.setText("Reserva no realizada por seguridad entre edades")
								else:
									if(info[3]+info[4]>info[2]):
										self.cajitaError.setText("ERROR: Incoherencia en los números de personas")
									else:
										if cursor.execute("SELECT * FROM Booking WHERE user_name=%s AND date=%s", (uss.username, info[0].toString("yyyy-MM-dd"))):
											self.cajitaError.setText("Ya tienes una reserva hecha para ese día")
										else:
											cursor.execute("INSERT INTO Booking VALUES (%s, %s, %s, %s, %s, %s, %s);", (uss.username, str(tdelta), str(info[2]), str(info[4]), str(info[3]), info[0].toString("yyyy-MM-dd"), str(info[5])))
											self.cajitaError.setText("Reserva Realizada correctamente!!")
											db.commit()
											time.sleep(2)
											self.close()
						else:
							if(info[3]+info[4]>info[2]):
								self.cajitaError.setText("ERROR: Incoherencia en los números de personas")
							else:
								if cursor.execute("SELECT * FROM Booking WHERE user_name=%s AND date=%s", (uss.username, info[0].toString("yyyy-MM-dd"))):
									self.cajitaError.setText("Ya tienes una reserva hecha para ese día")
								else:
									cursor.execute("INSERT INTO Booking VALUES (%s, %s, %s, %s, %s, %s, %s);", (uss.username, str(tdelta), str(info[2]), str(info[4]), str(info[3]), info[0].toString("yyyy-MM-dd"), str(info[5])))
									self.cajitaError.setText("Reserva Realizada correctamente!!")
									db.commit()
									time.sleep(2)
									self.close()


				#cursor.execute("SELECT capacity FROM Pool WHERE idpool=%s", (info[-1]))
				#data=cursor.fetchone()
				#cursor.execute("SELECT lower14, greater70 FROM Booking WHERE date=")
				
#Año-Mes-Dia

			else: 
				self.cajitaError.setText("No se ha escogido ninguna persona")

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
		else:
			self.label_3.setText("No Existe Tal Código")

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
		self.booking=book()
		self.cancel=cancel()
		self.commandLinkButton.clicked.connect(self.goPreBusqueda)
		self.commandLinkButton_2.clicked.connect(self.gobook)
		self.commandLinkButton_3.clicked.connect(self.cancelReserva)

	def cancelReserva(self):
		self.cancel.show()

	def gobook(self):
		self.booking.show()

	def goPreBusqueda(self):
		self.preBusqueda.show()

class user():
	def __init__(self):
		self.username=''

	def setUser(self, name):
		self.username=name

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
				uss.setUser(self.lineEdit.text())
				self.label.setText("Log In Correcto")
				self.intermedio.show()
				self.close()
			else:
				self.label.setText("Log In Incorrecto")
		else:
			self.label.setText("Falta algún campo")


if __name__ == "__main__":
	db=pymysql.connect("sql7.freemysqlhosting.net","sql7352402","k3elt85NjB","sql7352402")
	uss=user()
	cursor=db.cursor()
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()