import sys
from PyQt5.QtWidgets import *


class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()

        lbl1 = QLabel('One')
        lbl2 = QLabel('Two')
        lbl3 = QLabel('Three')
        lbl4 = QLabel('Four')
        lbl5 = QLabel('Five')

        layout1 = QVBoxLayout()
        layout1.addWidget(lbl1)
        layout1.addWidget(lbl2)
        layout1.addWidget(lbl3)
        layout1.addWidget(lbl4)
        layout1.addWidget(lbl5)

        btn1=QPushButton('One')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')
        btn4 = QPushButton('Four')
        btn5 = QPushButton('Five')

        layout2 = QVBoxLayout()
        layout2.addWidget(btn1)
        layout2.addWidget(btn2)
        layout2.addWidget(btn3)
        layout2.addWidget(btn4)
        layout2.addWidget(btn5)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(layout1)
        mainLayout.addLayout(layout2)

        self.setLayout(mainLayout)
        self.setGeometry(300,300,10,10)
        self.setWindowTitle("My Form")
        self.show()

app = QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)

if __name__ == '__main__':
    window()