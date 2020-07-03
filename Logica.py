from PantallaInicial import *
from RegistroUsuario import *

class RegisterWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.registerWindow=RegisterWindow()
		self.pushButton_2.clicked.connect(self.showRegister)

	def showRegister(self):
		self.registerWindow.show()


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()