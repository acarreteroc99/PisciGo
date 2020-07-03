import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

'''
# 2. Create an instance of QApplication
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 750, 1500)
window.move(200, 1000)
helloMsg = QLabel('<h1>Chapuzón Seguro</h1>', parent=window)
helloMsg.move(200, 100)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()

    labelCenter = QtWidgets.QLabel(windowExample)

    labelCenter.setText('Center Align')

    windowExample.setWindowTitle('Chapuzon Seguro')
    windowExample.setGeometry(100, 100, 300, 200)

    labelCenter.setFixedWidth(160)
    labelCenter.setStyleSheet("border-radius: 25px;border: 1px solid black;")
    labelCenter.setAlignment(QtCore.Qt.AlignCenter)
    labelCenter.move(80, 120)

    windowExample.show()
    sys.exit(app.exec_())


basicWindow()

