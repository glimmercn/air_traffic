__author__ = 'kan'

import TC.accessory as acc
import TC.Trajectory

def add_point_noise(point, xng, xp, yng = None, yp = None):
  if yng == None:
    yng = xng
  if yp == None:
    yp = xp
  point[0] += xng(*xp)
  point[1] += yng(*yp)

def add_trj_independent_noise(trj, xng, xp, yng = None, yp = None):
  '''
  add noise to a path
  :param ps:points of path
  :param xng:noise generator of x cordinate.
  :param xp:parameter of x
  :param yng:
  :param yp:
  :return:path with noise
  '''
  ps = trj.nodes
  if yng == None:
    yng = xng
  if yp == None:
    yp = xp
  for p in ps:
    add_point_noise(p, xng, xp)

def add_uniform_square_noise(trj, sizeRatio):
  '''
  this is a special kind of add_trj_independent_noise()
  :param trj:
  :param sizeRatio: the ratio between the distance between two points and the edge length of the square.
  :return:
  '''
  assert(len(trj.nodes) > 1)
  p1 = trj.nodes[0]
  p2 = trj.nodes[1]
  l = sizeRatio * acc.eclidean(p1, p2)
  add_trj_independent_noise(trj, acc.scaled_unif, l)

def add_cumulative_noise(trj, xweight, xng, xparameter, yweight=None, yng = None, yparameter = None):
  '''
  add cumulative noise to trajectory
  :param xweight, yweight: weight of the noise
  :param points:
  :param xng:
  :param xparameter:
  :param yng:
  :param yparameter:
  :return:
  '''
  points = trj.nodes
  if yweight == None:
    yweight = xweight
  if yng == None:
    yng = xng
  if yparameter == None:
    yparameter = xparameter

  xl = len(xweight)
  yl = len(yweight)
  xnoise = [0] * xl
  ynoise = [0] * yl

  for p in points:
    xnoise = [xng(*xparameter)] + xnoise[:-1]
    xn = 0
    for i in range(xl):
      xn += xnoise[i] * xweight[i]
    p[0] += xn

    ynoise = [yng(*yparameter)] + ynoise[:-1]
    yn = 0
    for i in range(xl):
      yn += ynoise[i] * yweight[i]
    p[1] += yn


