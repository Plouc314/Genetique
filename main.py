import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import HomeWindow

app = QtWidgets.QApplication(sys.argv)
home = HomeWindow()
home.show()
sys.exit(app.exec_())