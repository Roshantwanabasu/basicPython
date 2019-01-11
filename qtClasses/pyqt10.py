#http://pyqt.sourceforge.net/Docs/PyQt5/installation.html
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        slider = QSlider(Qt.Vertical)
        slider.valueChanged.connect(self.lcd.display)

        vbox.addWidget(self.lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 100, 100)
        self.setWindowTitle("My Form")
        self.show()

app = QApplication(sys.argv)
mainWindow = MyForm()
status = app.exec_()
sys.exit(status)

if __name__ == '__main__':
    window()