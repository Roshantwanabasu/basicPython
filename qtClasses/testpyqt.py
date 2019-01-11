from PyQt4 import QtGui, QtCore
import sys
from twisted.internet.protocol import Factory, Protocol
_fromUtf8 = QtCore.QString.fromUtf8

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self,reactor, parent=None):
        super(Ui_MainWindow,self).__init__(parent)
        self.reactor=reactor
        self.pf = Factory()
        self.pf.protocol = Protocol
        self.reactor.listenTCP(3609, self.pf) # listen on port 1234

    def setupUi(self,MainWindow):
        #MainWindow=QtGui.QMainWindow() # <-- Just use passed MainWindow.
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(903, 677)
        self.centralwidget = QtGui.QWidget(MainWindow)
        #then rest of the ui components.

if  __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    try:
        import qt4reactor
    except ImportError:
        from twisted.internet import qt4reactor
    qt4reactor.install()

    from twisted.internet import reactor
    MainWindow = QtGui.QMainWindow() # <-- Instantiate QMainWindow object.
    ui = Ui_MainWindow(reactor)
    ui.setupUi(MainWindow)
    MainWindow.show()

    reactor.run()
