from PyQt5 import QtCore, QtGui, QtWidgets

class labelButton(QtWidgets.QLabel, QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        self.signal = False
    clicked = QtCore.pyqtSignal()

    
    def mouseReleaseEvent(self, null):
        if self.signal == True:
        
            self.clicked.emit()
            self.signal = False

    def mousePressEvent(self, null):
        self.signal = True

