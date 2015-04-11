# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sandia.ui'
#
# Created: Fri Apr 10 19:39:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, random
from TC.accessory import *
from TC.NoiseModel import *
from TC.Trajectory import *

from copy import deepcopy

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
    MainWindow.resize(787, 631)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.canvas = QtGui.QWidget(self.centralwidget)
    self.canvas.setGeometry(QtCore.QRect(190, 10, 581, 571))
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
    self.noise3 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise3.setObjectName(_fromUtf8("noise3"))
    self.gridLayout.addWidget(self.noise3, 3, 0, 1, 2)
    self.noise2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise2.setObjectName(_fromUtf8("noise2"))
    self.gridLayout.addWidget(self.noise2, 2, 0, 1, 2)
    self.noise1 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
    self.noise1.setObjectName(_fromUtf8("noise1"))
    self.gridLayout.addWidget(self.noise1, 1, 0, 1, 2)
    self.nosieButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
    self.nosieButton.setObjectName(_fromUtf8("nosieButton"))
    self.gridLayout.addWidget(self.nosieButton, 0, 0, 1, 2)
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
    self.noise3.setText(_translate("MainWindow", "Noise3", None))
    self.noise2.setText(_translate("MainWindow", "Noise2", None))
    self.noise1.setText(_translate("MainWindow", "Noise1", None))
    self.nosieButton.setText(_translate("MainWindow", "Add Noise", None))
    self.label.setText(_translate("MainWindow", "arg1", None))
    self.label_2.setText(_translate("MainWindow", "arg2", None))
    self.label_3.setText(_translate("MainWindow", "arg3", None))

    self.connect(self.loadButton, QtCore.SIGNAL("pressed()"), self.loadPath)
    self.connect(self.drawButton, QtCore.SIGNAL('pressed()'), self.canvas.repaint)
    self.connect(self.InterpolateButton, QtCore.SIGNAL("pressed()"), self.interpolate)
    self.connect(self.truncButton, QtCore.SIGNAL('pressed()'), self.truncate)

  def loadPath(self):
    global trajecotries, pathSet
    pathFileName = QtGui.QFileDialog.getOpenFileName()
    if pathFileName == "":
      return
    try:
      pathSet = read_trjs(pathFileName)
    except IOError:
      QtGui.QMessageBox.warning(self, "Error", "can't read" + pathFileName)

    trajecotries = deepcopy(pathSet)
    self.canvas.repaint()

  def interpolate(self):
    pass

  def truncate(self):
    pass

def main():

  app = QtGui.QApplication(sys.argv)
  ex = Ui_MainWindow()
  ex.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()