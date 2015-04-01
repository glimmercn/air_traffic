__author__ = 'kan'


import sys, random
from PyQt4 import QtGui, QtCore

from TC.accessory import *
from TC.NoiseModel import *
from TC.Trajectory import *

pathFileName = 'arrangement/100_simple.paths'
arrFileName = 'arrangement/30.arr'

pathSet = None
trjSet = None
arr = None



class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

      self.loadButton = QtGui.QPushButton('Load Path File')
      self.connect(self.loadButton, QtCore.SIGNAL("pressed()"), self.loadPath)

      self.drawPathsButton = QtGui.QPushButton('Draw Paths')
      review = QtGui.QLabel('Review')

      self.loadEdit = QtGui.QLineEdit()
      authorEdit = QtGui.QLineEdit()
      reviewEdit = Canvas()

      grid = QtGui.QGridLayout()
      grid.setSpacing(10)

      grid.addWidget(self.loadButton, 1, 0)
      grid.addWidget(self.loadEdit, 1, 1)

      grid.addWidget(self.drawPathsButton, 2, 0)
      grid.addWidget(authorEdit, 2, 1)

      grid.addWidget(review, 3, 0)
      grid.addWidget(reviewEdit, 3, 1, 5, 1)

      self.setLayout(grid)

      self.setGeometry(200, 200, 1000, 1000)
      self.setWindowTitle('Trajectory')
      self.show()



    def loadPath(self):
      pathFileName = self.loadEdit.text()
      trjSet = read_trjs(pathFileName)
      print(len(trjSet.trjs))

class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(200, 200, 800, 800)
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawTrj(qp)
        qp.end()

    def drawTrj(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        if trjSet:
          for trj in trjSet.trjs:
            trj.gui_draw(qp)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()