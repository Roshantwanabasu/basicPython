import sys
from PyQt5.QtWidgets import *


class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        btn1=QPushButton('one')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')
        btn4 = QPushButton('Four')
        btn5 = QPushButton('Five')
        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        self.setLayout(layout)
        self.setGeometry(300,300,10,10)
        self.setWindowTitle("My Form")
        self.show()

app = QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)

if __name__ == '__main__':
    window()