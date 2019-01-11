import sys
from PyQt5.QtWidgets import *
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150)
    w.move(350,300)
    w.setWindowTitle("My python GUI Application")
    w.show()
    w2=QWidget()
    w2.show()
    status = app.exec_()
    sys.exit(status)
   
if __name__ == '__main__':
    window()