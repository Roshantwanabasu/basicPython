import sys
from PyQt5.QtWidgets import *


class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()

       
        self.lbl =QLabel('Hello')

        btn = QPushButton('Submit')
        btn.clicked.connect(self.handleClicked)



        lbl1 = QLabel('First')
        lbl2 = QLabel('Last')
        lbl3 = QLabel('Gender')
        lbl4 = QLabel('Age')
        first = QLineEdit()
        last = QLineEdit()
        gender = QComboBox()
        gender.addItems(['Male','Female'])
        age = QSpinBox()
        age.setMinimum(18)

        mainLayout = QGridLayout()
        mainLayout.addWidget(lbl1,0,0)
        mainLayout.addWidget(lbl2, 1, 0)
        mainLayout.addWidget(lbl3, 2, 0)
        mainLayout.addWidget(lbl4, 3, 0)
        mainLayout.addWidget(self.lbl)
        mainLayout.addWidget(btn)


        mainLayout.addWidget(first,0,1)
        mainLayout.addWidget(last,1,1)
        mainLayout.addWidget(gender,2,1)
        mainLayout.addWidget(age,3,1)
        mainLayout.addWidget(self.lbl,4,1)
        mainLayout.addWidget(btn,5,1)


        self.setLayout(mainLayout)
        self.setGeometry(300,300,10,10)
        self.setWindowTitle("My Form")
        self.show()

    def handleClicked(self):
        self.lbl.setText("Botton Clicked!")

app = QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)

if __name__ == '__main__':
    window()