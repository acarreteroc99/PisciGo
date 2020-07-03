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
		pass #Aquí que todo ok y a la base de datos

	def test_cancel(self):
		self.close()

class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.db=pymysql.connect("sql7.freemysqlhosting.net","sql7352402","k3elt85NjB","sql7352402")
		self.cursor=self.db.cursor()
		self.registerWindow=RegisterWindow()
		self.pushButton_2.clicked.connect(self.showRegister)

	def showRegister(self):
		self.registerWindow.show()


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()