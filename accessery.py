'''
Created on Jun 22, 2014

@author: kan
'''

import numpy
from shapely.geometry import *

class Trj:
  '''
  trajectory class
  '''
  nodes = None

  def __init__(self, ns):
    '''
    Constructor
    '''
    self.nodes = ns

class Graph:
  '''
  graph class
  '''
 def __init__(self, points, im):
   '''
   :param points:
   :param im: incident matrix
   :return:
   '''
   self.points = points
   self.im = im
   self.pn = len(points)

def heter_interpolate(p1, p2, n, rg, params):
  '''
  insert n points between p1, p2
  :param p1:
  :param p2:
  :param n:
  :param rg: random number generator
  :param params: the parameters of rg
  :return:
  '''
  ps = []
  if p1.x != p2.x:
    k = (p2.y - p1.y)/(p2.x - p1.x)
    pnew = Point(p1)

    for i in range(n):
      dx = rg(params)
      dy = k * rg(params)
      pnew.x += dx
      pnew.y += dy
      ps.append(Point(pnew))
    return ps
  else:
    pnew = Point(p1)
    for i in range(n):
      dy = rg(params)
      pnew.y += dy
      ps.append(Point(pnew))
    return ps

def random_graph(n, p=0.5):
  '''
  generate a graph whose nodes are uniformly distributed in [0, 1]*[0,1]
  :param n: the number of nodes
  :param p: how many edges in the graph
  :return:
  '''
  points = numpy.random.rand(n, 2)
  im = [[] for i in range(n)]  #incident matrix
  for i in range(n-1):
    for j in range(i+1, n):
      if numpy.random.random_sample() < p:
        im[i].append(j)
        im[j].append(i)
  return points,im

def add_uniform_noise(nx, ny):
  '''
  add uniform noise to trajectory
  :param nx: noise on x
  :param ny: noise on y
  :return: trajectory with noise
  '''
def add_noise(ps, xng, xp, yng = None, yp = None):
  '''
  add noise to a path
  :param ps:points of path
  :param xng:noise generator of x cordinate.
  :param xp:parameter of x
  :param yng:
  :param yp:
  :return:path with noise
  '''
  if yng == None:
    yng = xng
  if yp == None:
    yp = xp
  for p in ps:
    p[0] += xng(*xp)
    p[1] += yng(*yp)

def add_cum_noise(xweight, yweight, ps, xng, xp, yng = None, yp = None):
  '''
  add cumulative noise to trajectory
  :param xweight, yweight: weight of the noise
  :param ps:
  :param xng:
  :param xp:
  :param yng:
  :param yp:
  :return:
  '''
  xl = len(xweight)
  yl = len(yweight)
  xnoise = [0] * xl
  ynoise = [0] * yl
  for p in ps:
    xn = xng(*xp)
    for i in range(xl):
      xn += xnoise[i] * xweight[i]
    p[0] += xn
    xnoise = [xn] + xnoise[:-1]

    yn = yng(*yp)
    for i in range(xl):
      yn += ynoise[i] * yweight[i]
    p[1] += yn
    ynoise = [yn] + ynoise[:-1]
  

def random_path(g, l, s = None):
  '''
  generate a path from graph g
  :param g: graph
  :param l: the length of the path
  :param s: the start
  :return:
  '''
  if s == None:
    s = numpy.random.randomint(0, g.pn)
  p = s
  path = [p]
  for i in range(l):
     j = numpy.random.randomint(0, len(g.im[p]))
     p = g.im[p][j]
     path.append(p)
  return path

def shortest_path(g, s, t):
  '''
  return the shortest path from s to t in g
  :param g:
  :param s:
  :param t:
  :return:
  '''
  pass





