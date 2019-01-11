import sys
from PyQt5.QtWidgets import *

class MyForm(QWidget):
    def __init__(self):
        super(MyForm,self).__init__()
        lbl= QLabel('My first GUI Element!',self)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('My Form')
        self.show()
app = QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)

if __name__ == '__main__':
    MyForm()