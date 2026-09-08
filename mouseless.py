#!/usr/bin/python2
# author:   hruskam
# source:   https://hruskam.wordpress.com/2015/11/14/mouseless/
#           http://phoebe.inf.upol.cz/~hruskam/temporary/mouseless.py

# description:
#   mouseless is a small python script, which enables fast movement of
#   mouse cursor by successive division of screen. In effect, one can reach
#   every pixel in small number of steps (logarithmic in size of screen)
#   by using adequate keys on numeric keypad.
#   An example of process of division is shown on the following video.
#   https://www.youtube.com/watch?v=OsefVqkWpgs

# requirements: python2 python2-qt4 xdotool

# run mouseless: (bind script to hotkeys examples)
# Left Hand:    Ctrl+Shift+A or Hyper_L + A (Capslock + A)
# Right Hand:   Alt_R + Semicolon
# Numpad:       Pause/Break key


# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:03:06 2013

@author: hruskam
"""

verbose = True

# import libraries
from PyQt4 import QtGui, Qt, QtCore
import sys
import itertools as it
import subprocess as sp
import re

# configuration
xdotool_bin = '/usr/bin/xdotool'

# graphics
pen_width    = 1
# pen used for the innermost grid
final_pen    = QtGui.QPen(QtGui.QColor(255, 0, 0, 255), pen_width, QtCore.Qt.DashLine)
# pen used for the rest of grids
nonfinal_pen = QtGui.QPen(QtGui.QColor(  0, 0, 0, 255), pen_width, QtCore.Qt.SolidLine)
# opacity of the main window
win_opacity  = 0.25

# keys used for exiting the application
exit_keys = [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter, QtCore.Qt.Key_Escape, QtCore.Qt.Key_Semicolon, QtCore.Qt.Key_Plus]
# keys used for going to previous grid
back_keys = [QtCore.Qt.Key_Backspace, QtCore.Qt.Key_Space, QtCore.Qt.Key_0]

# mapping keypad to selection tuples
qk   = QtCore.Qt

keyd = {qk.Key_7: (-1, -1), qk.Key_8: ( 0, -1), qk.Key_9: ( 1, -1),
        qk.Key_4: (-1,  0), qk.Key_5: ( 0,  0), qk.Key_6: ( 1,  0),
        qk.Key_1: (-1,  1), qk.Key_2: ( 0,  1), qk.Key_3: ( 1,  1),
        qk.Key_Q: (-1, -1), qk.Key_W: ( 0, -1), qk.Key_E: ( 1, -1),
        qk.Key_A: (-1,  0), qk.Key_S: ( 0,  0), qk.Key_D: ( 1,  0),
        qk.Key_Z: (-1,  1), qk.Key_X: ( 0,  1), qk.Key_C: ( 1,  1),
        qk.Key_U: (-1, -1), qk.Key_I: ( 0, -1), qk.Key_O: ( 1, -1),
        qk.Key_J: (-1,  0), qk.Key_K: ( 0,  0), qk.Key_L: ( 1,  0),
        qk.Key_M: (-1,  1), qk.Key_Comma: ( 0,  1), qk.Key_Period: ( 1,  1)}

# mouse moving using xdotool
def mouse_move(x, y):
  sp.check_call([xdotool_bin, 'mousemove', "%d" % x, "%d" % y])

# perform mouse move to center of an QRect
def mouse_move_center(qr):
  mouse_move(qr.center().x(), qr.center().y())

# auxiliary functions from fplib (not yet on pypi)
# performs flattening of the list
def unlist1(value):
  return list(it.chain(*value))

# retrieves the list without its last element
def nolast(l):
  return l[:-1]

# retrievies set of lists, which start 
def prefixes(l):
  return map(lambda i: l[:(i + 1)], range(len(l)))

# centered scale of rectangle
def qt_centered_scale(qr, scale):
  qc = Qt.QRect(qr)
  t  = Qt.QTransform().fromScale(scale, scale)
  qr = t.mapRect(qr)
  qr.translate(qc.center() - qr.center())
  return qr

# obtain final rectangle, based on user selections 
# e.g. if selections are [(-1, -1), (0, 0)]
#      that means the user selected 7 (upper left) and 5 (center)
# in each step, the rectangle is scaled (three times smaller), preserving
# its center; and shifted accordingly
def get_selections_final_rect(selections):
  qr = QtGui.QDesktopWidget().screenGeometry()
  for d_x, d_y in selections:
    qr  = qt_centered_scale(qr, 1.0 / 3)
    qr.translate(d_x * qr.width(), d_y * qr.height())
  return qr

class GridScene(QtGui.QGraphicsScene):
  def __init__(self, parent=None):
    QtGui.QGraphicsScene.__init__(self, parent)
    qr = QtGui.QDesktopWidget().screenGeometry()
    self.draw_grid(qr, nonfinal_pen)

  def draw_grid(self, qr, pen, n=3):
    for y in range(qr.top(), qr.bottom(), qr.height() / n):
      self.addLine(qr.left(), y, qr.right(), y, pen=pen)
    for x in range(qr.left(), qr.right(), qr.width() / n):
      self.addLine(x, qr.top(), x, qr.bottom(), pen=pen)

class GridWindow(QtGui.QMainWindow):
  
  def __init__(self, parent=None):
    # initialize user selections to empty
    self.selections = []
    # 
    QtGui.QMainWindow.__init__(self, parent)
    self.scene = GridScene()
    view       = QtGui.QGraphicsView(self.scene)
    # hide scrollbars
    view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    # simple layout
    hbox = QtGui.QHBoxLayout()
    hbox.setSpacing(0)
    hbox.setMargin(0)
    hbox.addWidget(view)
    # window properties
    self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)  
    self.setWindowState(self.windowState() | QtCore.Qt.WindowActive)
    self.setWindowOpacity(win_opacity)
    # 
    mainWidget = QtGui.QWidget()
    mainWidget.setLayout(hbox)
    
    def widgetKeypress(event):
      key = event.key()

      def update_to_user_selections():
        self.scene.clear()
        for sels in [[]] + prefixes(self.selections):
          qr  = get_selections_final_rect(sels)
          pen = final_pen if len(sels) == len(self.selections) else nonfinal_pen
          self.scene.draw_grid(qr, pen)
        mouse_move_center(qr)

      # if key is in numeric keypad, then add selection
      if key in keyd.keys():
        self.selections.append(keyd[key])
      # if key is in backspace keys, then remove last selection
      elif key in back_keys:
        self.selections = nolast(self.selections)
      # exit if key is in exit keys
      elif key in exit_keys:
        sys.exit()
      
      update_to_user_selections()

    mainWidget.keyPressEvent = widgetKeypress
    self.setCentralWidget(mainWidget)

# mouse_move(screen_width() / 2, screen_height() / 2)
app    = QtGui.QApplication(['mouseless'])
screen = QtGui.QDesktopWidget().screenGeometry()

# create main window maximized
window = GridWindow()
window.showMaximized()
#
sys.exit(app.exec_())
