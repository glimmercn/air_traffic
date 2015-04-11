__author__ = 'kan'


import sys, random
from PyQt4 import QtGui, QtCore

from TC.accessory import *
from TC.NoiseModel import *
from TC.Trajectory import *

from copy import deepcopy

pathSet = None
trajecotries= None




class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

      self.loadButton = QtGui.QPushButton('Load Path File')
      self.connect(self.loadButton, QtCore.SIGNAL("pressed()"), self.loadPath)

      self.drawPathsButton = QtGui.QPushButton('Draw')
      self.canvas = Canvas()
      self.connect(self.drawPathsButton, QtCore.SIGNAL('pressed()'), self.canvas.repaint)

      self.loadEdit = QtGui.QLineEdit("arrangement/100_simple.paths")

      noiseLabel = QtGui.QLabel('Noise Name:')
      self.noiseEdit = QtGui.QLineEdit("Put a number here.")

      self.truncButton = QtGui.QPushButton('Truncate')
      self.connect(self.truncButton, QtCore.SIGNAL('pressed()'), self.truncate)

      self.noiseButton = QtGui.QPushButton('Add Noise')
      self.connect(self.noiseButton, QtCore.SIGNAL('pressed()'), self.addNoise)


      grid = QtGui.QGridLayout()
      grid.setSpacing(10)

      grid.addWidget(self.loadButton, 1, 0)
      grid.addWidget(self.loadEdit, 1, 1)
      grid.addWidget(self.drawPathsButton, 2, 0)

      #grid.addWidget(noiseLabel, 3, 0)
      grid.addWidget(self.truncButton, 4, 0)
      grid.addWidget(self.noiseButton, 5, 0)
      grid.addWidget(self.noiseEdit, 5, 1)

      grid.addWidget(self.canvas, 6, 1, 8, 1)

      self.setLayout(grid)

      self.setGeometry(100, 100, 1000, 1000)
      self.setWindowTitle('Trajectory')
      self.show()



    def loadPath(self):
      global trajecotries, pathSet
      pathFileName = self.loadEdit.text()
      try:
        pathSet = read_trjs(pathFileName)
      except IOError:
        QtGui.QMessageBox.warning(self, "Error", "can't find " + pathFileName)

      ''' the paths will be interpolated immediately.
      pathSet is a copy for reset.
      trjSet is a copy that functions will work on.
      '''
      l = 10
      pathSet.interpolate(l)
      trajecotries = deepcopy(pathSet)
      self.canvas.repaint()

    def truncate(self):
      global trajecotries
      trajecotries.random_truncate()
      self.canvas.repaint()

    def addNoise(self):
      global trajecotries, pathSet
      params = [float(self.noiseEdit.text())]
      trajecotries.add_noise(uniform_square_noise, params)
      self.canvas.repaint()


class Canvas(QtGui.QWidget):

    def __init__(self):
        super(Canvas, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(200, 200, 800, 800)
        self.show()

    def paintEvent(self, e):
      global trajecotries
      qp = QtGui.QPainter()
      qp.begin(self)
      if trajecotries:
        self.drawTrj(qp)
      qp.end()

    def drawTrj(self, qp):
      global trajecotries
      pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
      qp.setPen(pen)
      for trj in trajecotries.trjs:
        trj.gui_draw(qp)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()