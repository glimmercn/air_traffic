# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sandia.ui'
#
# Created: Fri Apr 10 19:39:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
__author__ = 'kan huang'

from PyQt4 import QtCore, QtGui
import sys

from TC.accessory import *
from TC.NoiseModel import *
from TC.Trajectory import *

from copy import deepcopy
from random import randint

pathSet = None
trajecotries= None

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
  def __init__(self):
    QtGui.QMainWindow.__init__(self)
    self.setupUi(self)

  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(1000, 850)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.canvas = Canvas(self.centralwidget)
    self.canvas.setGeometry(QtCore.QRect(190, 0, 800, 800))
    self.canvas.setObjectName(_fromUtf8("canvas"))
    self.verticalLayout = QtGui.QVBoxLayout(self.canvas)
    self.verticalLayout.setMargin(0)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
    self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 163, 571))
    self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
    self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
    self.verticalLayout_2.setMargin(0)
    self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
    self.loadButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.loadButton.setObjectName(_fromUtf8("loadButton"))
    self.verticalLayout_2.addWidget(self.loadButton)

    self.saveButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.saveButton.setObjectName(_fromUtf8("saveButton"))
    self.saveButton.setText("Save")
    self.verticalLayout_2.addWidget(self.saveButton)

    self.resetButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.resetButton.setObjectName(_fromUtf8("resetButton"))
    self.verticalLayout_2.addWidget(self.resetButton)
    self.InterpolateButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.InterpolateButton.setObjectName(_fromUtf8("InterpolateButton"))
    self.verticalLayout_2.addWidget(self.InterpolateButton)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setSpacing(4)
    self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.verticalLayout_2.addLayout(self.horizontalLayout)
    self.truncButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.truncButton.setObjectName(_fromUtf8("truncButton"))
    self.verticalLayout_2.addWidget(self.truncButton)
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    self.drawButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.drawButton.setObjectName(_fromUtf8("drawButton"))
    self.horizontalLayout_2.addWidget(self.drawButton)
    self.colorcheckBox = QtGui.QCheckBox(self.verticalLayoutWidget_2)
    self.colorcheckBox.setObjectName(_fromUtf8("colorcheckBox"))
    self.horizontalLayout_2.addWidget(self.colorcheckBox)
    self.verticalLayout_2.addLayout(self.horizontalLayout_2)
    self.gridLayout = QtGui.QGridLayout()
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.arg2Edt = QtGui.QLineEdit(self.verticalLayoutWidget_2)
    self.arg2Edt.setObjectName(_fromUtf8("arg2Edt"))
    self.gridLayout.addWidget(self.arg2Edt, 5, 1, 1, 1)
    self.arg1Edt = QtGui.QLineEdit(self.verticalLayoutWidget_2)
    self.arg1Edt.setObjectName(_fromUtf8("arg1Edt"))
    self.gridLayout.addWidget(self.arg1Edt, 4, 1, 1, 1)
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
    self.arg3Edt = QtGui.QLineEdit(self.verticalLayoutWidget_2)
    self.arg3Edt.setObjectName(_fromUtf8("arg3Edt"))
    self.gridLayout.addWidget(self.arg3Edt, 6, 1, 1, 1)
    self.noise3rButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise3rButton.setObjectName(_fromUtf8("noise3"))
    self.gridLayout.addWidget(self.noise3rButton, 3, 0, 1, 2)
    self.noise2rButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise2rButton.setObjectName(_fromUtf8("noise2"))
    self.gridLayout.addWidget(self.noise2rButton, 2, 0, 1, 2)
    self.noise1rButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise1rButton.setObjectName(_fromUtf8("noise1"))
    self.gridLayout.addWidget(self.noise1rButton, 1, 0, 1, 2)
    self.addNoiseButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.addNoiseButton.setObjectName(_fromUtf8("nosieButton"))
    self.gridLayout.addWidget(self.addNoiseButton, 0, 0, 1, 2)
    self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
    self.label.setObjectName(_fromUtf8("label"))
    self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
    self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
    self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
    self.label_3.setObjectName(_fromUtf8("label_3"))
    self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
    self.verticalLayout_2.addLayout(self.gridLayout)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtGui.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 25))
    self.menubar.setObjectName(_fromUtf8("menubar"))
    MainWindow.setMenuBar(self.menubar)
    self.statusbar = QtGui.QStatusBar(MainWindow)
    self.statusbar.setObjectName(_fromUtf8("statusbar"))
    MainWindow.setStatusBar(self.statusbar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "Trajectory", None))
    self.loadButton.setText(_translate("MainWindow", "Load", None))
    self.InterpolateButton.setText(_translate("MainWindow", "Interpolate", None))
    self.resetButton.setText(_translate("MainWindow", "Reset", None))
    self.truncButton.setText(_translate("MainWindow", "Truncate", None))
    self.drawButton.setText(_translate("MainWindow", "Draw", None))
    self.colorcheckBox.setText(_translate("MainWindow", "Color", None))
    self.noise3rButton.setText(_translate("MainWindow", "Noise3", None))
    self.noise2rButton.setText(_translate("MainWindow", "Noise2", None))
    self.noise1rButton.setText(_translate("MainWindow", "Noise1", None))
    self.addNoiseButton.setText(_translate("MainWindow", "Add Noise", None))
    self.label.setText(_translate("MainWindow", "arg1", None))
    self.label_2.setText(_translate("MainWindow", "arg2", None))
    self.label_3.setText(_translate("MainWindow", "arg3", None))



    self.connect(self.loadButton, QtCore.SIGNAL("pressed()"), self.loadPath)
    self.connect(self.saveButton, QtCore.SIGNAL("pressed()"), self.savePath)
    self.connect(self.drawButton, QtCore.SIGNAL('pressed()'), self.canvas.repaint)
    self.connect(self.InterpolateButton, QtCore.SIGNAL("pressed()"), self.interpolate)
    self.connect(self.truncButton, QtCore.SIGNAL('pressed()'), self.truncate)
    self.connect(self.resetButton, QtCore.SIGNAL('pressed()'), self.reset)
    self.drawButton.clicked.connect(self.canvas.repaint)
    self.colorcheckBox.clicked.connect(self.changeColor)
    self.addNoiseButton.clicked.connect(self.addNoise)


  def changeColor(self):
    self.canvas.iscolor = self.canvas.iscolor ^ True
    self.canvas.repaint()

  def loadPath(self):
    global trajecotries, pathSet
    pathFileName = QtGui.QFileDialog.getOpenFileName()
    if pathFileName == "":
      return
    try:
      pathSet = read_trjs(pathFileName)
    except ValueError:
      QtGui.QMessageBox.warning(self, "Error:", "can't read" + pathFileName)

    if pathSet:
      trajecotries = deepcopy(pathSet)
      self.canvas.repaint()

  def savePath(self):
    global trajecotries
    trajecotries.save()


  def reset(self):
    global trajecotries, pathSet
    trajecotries = deepcopy(pathSet)
    self.canvas.repaint()

  def interpolate(self):
    if trajecotries:
      trajecotries.interpolate(10)
      self.canvas.repaint()

  def truncate(self):
    global trajecotries
    trajecotries.random_truncate()
    self.canvas.repaint()

  def addNoise(self):
    global trajecotries
    if trajecotries:
      print(self.noise1rButton.isChecked())
      if self.noise1rButton.isChecked():
        try:
          pr1 = float(self.arg1Edt.text())
          trajecotries.add_noise(uniform_square_noise, [pr1])
          self.canvas.repaint()
        except ValueError:
          QtGui.QMessageBox.warning(self, "Error", "need a number in arg1")



class Canvas(QtGui.QWidget):
    def __init__(self, widget):
      self.iscolor = False
      super(Canvas, self).__init__(widget)
      self.initUI()

    def initUI(self):
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
      pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
      qp.setPen(pen)

      for trj in trajecotries.trjs:
        if self.iscolor:
          pen = QtGui.QPen(QtGui.QColor(randint(1, 255), randint(1, 255), randint(1, 255), 255), 1, QtCore.Qt.SolidLine)
          qp.setPen(pen)
        trj.gui_draw(qp)

def main():
  app = QtGui.QApplication(sys.argv)
  ex = Ui_MainWindow()
  ex.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()