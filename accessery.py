'''
Created on Jun 22, 2014

@author: kan
'''

import numpy

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __abs__(self, p):
    self.x = p.x
    self.y = p.y
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

