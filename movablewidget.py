from PyQt5 import QtCore, QtGui, QtWidgets

class movableWidget(QtWidgets.QFrame):
    def __init__(self, parent):
        QtWidgets.QFrame.__init__(self, parent)
        self.pressing = False
        self.start = QtCore.QPoint(0, 0)
        self.parent = parent

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
         if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.parent.mapToGlobal(self.movement).x(),
                                self.parent.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            
            self.start = self.end

    def mouseReleaseEvent(self, event):
        self.pressing = False
        