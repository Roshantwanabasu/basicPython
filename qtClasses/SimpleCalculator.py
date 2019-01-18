import sys
from PyQt5.QtWidgets import *


class Calc(QWidget):

    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowTitle("Simple Calculator")
        numOne = QLabel("Enter 1st number")
        numTwo = QLabel("Enter 2nd number")
        self.firstNum = QLineEdit()
        self.secondNum = QLineEdit()
        self.selectOperation = QComboBox()
        self.selectOperation.addItems(["Add", "Subtract", "Multiply", "Divide"])
        btn = QPushButton('Calculate')
        Result = QLabel("Result:")
        self.OperationAnswer = QLabel()
        calcLayout = QGridLayout()
        calcLayout.addWidget(numOne, 0, 0)
        calcLayout.addWidget(self.firstNum, 0, 1)
        calcLayout.addWidget(numTwo, 1, 0)
        calcLayout.addWidget(self.secondNum, 1, 1)
        calcLayout.addWidget(self.selectOperation, 2, 0)
        calcLayout.addWidget(btn, 2, 1)
        calcLayout.addWidget(Result, 3, 0)
        calcLayout.addWidget(self.OperationAnswer, 3, 1)
        self.setLayout(calcLayout)
        btn.clicked.connect(self.OnButtonClick)
        self.show()

    def OnButtonClick(self):
        numOne = int(self.firstNum.text())
        numTwo = int(self.secondNum.text())

        if self.selectOperation.currentIndex() == 0:
            sum = numTwo + numOne
        elif self.selectOperation.currentIndex() == 1:
            sum = numOne - numTwo
        elif self.selectOperation.currentIndex() == 2:
            sum = numOne * numTwo
        else :
            sum = numOne / numTwo

        self.OperationAnswer.setText(str(sum))



app = QApplication(sys.argv)
mainWindow = Calc()
status = app.exec_()
sys.exit(status)

