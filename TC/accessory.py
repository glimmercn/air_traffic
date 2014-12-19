'''
Created on Jun 22, 2014

@author: kan
'''

import numpy
from shapely.geometry import *
from pylab import *
import matplotlib.pyplot as plt



class Graph:
  '''
  graph class
  '''
  def __init__(self, points, im):
    '''
    im: incident matrix
    pn: number of nodes in the graph.
    points: nodes
    '''
    self.points = points
    self.im = im
    self.pn = len(points)



def eclidean(p1, p2):
  return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5


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


def random_trj_from_graph(g, l, s = None):
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

def random_trjs_from_graph(g, ls, s = None):
  assert len(ls) > 0
  trjs = []
  for l in ls:
    trjs.append(random_trj_from_graph(g, l, s))

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
  return trj

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



if __name__ == "__main__":
  pass


