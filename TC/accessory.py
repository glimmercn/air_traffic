'''
Created on Jun 22, 2014

@author: kan
'''

import numpy
from shapely.geometry import *
from pylab import *
import matplotlib.pyplot as plt

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

  def draw(self, m, c):
    plt.plot(*zip(*self.nodes), marker=m, color=c)

  def truncate(self, i, j):
    if i>=0 and j>i and j<=len(self.nodes):
      self.nodes = self.nodes[i:j]


  def random_truncate(self):
    ends = sorted(numpy.random.rand(2))
    first = int(ends[0]*len(self.nodes))
    last = int(ends[1]*len(self.nodes))
    self.truncate(first, last)

class portal:
  
  def __init__(self, center, size):
    self.center = center
    self.size = size
  
  '''check whether this portal hits trajecotry'''
  def hit(self, trj):
    
    for p in trj.nodes:
      if self.contain(p):
        return True
    
    return False
  
  '''check whether this portal contains point p'''
  def contain(self, p):
    c1 = self.center[0]-size/2.0 <= p[0] <= self.center[0]+size/2.0
    c2 = self.center[1]-size/2.0 <= p[1] <= self.center[1]+size/2.0
    return c1 and c2
  
  def distance(self, ptl2):
    return eclidean(self.center, ptl2.center)

class Graph:
  '''
  graph class
  '''
  def __init__(self, points, im):
    self.points = points
    self.im = im
    self.pn = len(points)



def eclidean(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5

def interpolate_edge(p1, p2, n):
  '''
  insert n points between p1, p2
  :param p1:
  :param p2:
  :param n:
  :return:
  '''
  ps = []
  cp1 = p1[:]
  if p1[0] != p2[0]:
    k = (p2[1] - p1[1])/(p2[0]- p1[0])
    Dx = (p2[0] - p1[0])/(n+1)
    for i in range(n):
      dx = Dx * (i+1)
      dy = k * dx
      pi = [cp1[0] + dx, cp1[1]+dy]
      ps.append(pi)
    return ps
  else:
    ps = [[p1[0], p1[1] + (i+1)*(p2[1]-p1[1])/(n+1)] for i in range(n)]
  return ps

def interpolate_path(path, slen):
  '''
  interpolate the path by a given length
  :param path:
  :param slen:the length of the step
  :return:interpolated path(trajectory before perturbation)
  '''
  trj = [path[0]]
  for i in range(len(path)-1):
    p1 = path[i]
    p2 = path[i+1]
    l = eclidean(p1, p2)
    n = int(l/slen)
    trj += interpolate_edge(p1, p2, n)
    trj.append(p2)
  return Trj(trj)

def random_interpolated_path(g, l, slen, s=None):
  '''
  generate a random interpolated path
  :param g:
  :param l:
  :param slen:
  :param s:
  :return:a trajectory
  '''
  if s == None:
    s = numpy.random.randint(0, g.pn)
  p = s
  path = [g.points[p]]
  for i in range(l):
     j = numpy.random.randint(0, len(g.im[p]))
     p = g.im[p][j]
     path.append(g.points[p])
  return interpolate_path(path, slen)



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
  return Graph(points, im)

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
  if yng == None:
    yng = xng
  if yp == None:
    yp = xp
  xl = len(xweight)
  yl = len(yweight)
  xnoise = [0] * xl
  ynoise = [0] * yl
  for p in ps:
    xnoise = [xng(*xp)] + xnoise[:-1]
    xn = 0
    for i in range(xl):
      xn += xnoise[i] * xweight[i]
    p[0] += xn

    ynoise = [yng(*yp)] + ynoise[:-1]
    yn = 0
    for i in range(xl):
      yn += ynoise[i] * yweight[i]
    p[1] += yn


def random_path(g, l, s = None):
  '''
  generate a path from graph g
  :param g: graph
  :param l: the length of the path
  :param s: the start
  :return:
  '''
  if s == None:
    s = numpy.random.randint(0, g.pn)
  p = s
  path = [g.points[p]]
  for i in range(l):
     j = numpy.random.randint(0, len(g.im[p]))
     p = g.im[p][j]
     path.append(g.points[p])
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

'''distributions'''

def scaled_unif(scale):
  '''
  return a random value from -scale/2 to scale/2
  :param scale:
  :return:
  '''
  return (numpy.random.ranf()-0.5)*scale

if __name__ == "__main__":
  g= random_graph(15, 1)
  path = random_path(g, 4)
  trj = interpolate_path(path, 0.02)
  add_noise(trj.nodes, scaled_unif, [0.01])
  trj.draw('o','r')




