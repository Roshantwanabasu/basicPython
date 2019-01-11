from __future__ import print_function
import sys
from PyQt5 import QtGui
app = QtGui.QApplication(sys.argv)
Window = QtGui.QWidget()
Window.resize(250,150)
Window.move(300,300)
Window.setWindowTitle("My First GUI APP")
Window.Show()
Status = app.exec_()
sys.exit(status)