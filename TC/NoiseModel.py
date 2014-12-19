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

def add_pull_noise(trj, pullPower, xng, xparameter, yng=None, yparameter=None):
  '''
  noise model. trajectory has the momentone to keep the direction and pullPower
  represents how much it will be pulled by the original trajectory. we expect it
  to be smoother than independent noise
  '''
  if yng == None:
    yng = xng
  if yparameter == None:
    yparameter = xparameter

  ps = trj.nodes
  if len(ps) < 3:
    add_trj_independent_noise(trj, xng, xparameter, yng, yparameter)
  else:
    D = acc.eclidean(ps[0], ps[1])
    add_point_noise(ps[1], xng, xparameter, yng, yparameter)

    for i in range(2, len(ps)):
      p1, p2, p3 = ps[i-2: i+1]
      op3 = p3[:]

      l = acc.eclidean(p1, p2)
      p3[0] = p2[0] + D * (p2[0] - p1[0]) / l
      p3[1] = p2[1] + D * (p2[1] - p1[1]) / l
      add_point_noise(p3, xng, xparameter, yng, yparameter)

      # pull
      p3[0] = pullPower * op3[0] + (1 - pullPower) * p3[0]
      p3[1] = pullPower * op3[1] + (1 - pullPower) * p3[1]