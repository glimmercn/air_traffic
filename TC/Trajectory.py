__author__ = 'kan'

import numpy
import matplotlib.pyplot as plt
import TC.accessory as acc

class Trj(object):
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
    # ends = sorted(numpy.random.rand(2))
    # first = int(ends[0]*len(self.nodes))
    # last = int(ends[1]*len(self.nodes))
    ends = numpy.random.rand(2)
    first = int(ends[0] * 0.5 * len(self.nodes))
    last = int((ends[1] * 0.5 + 0.5) * len(self.nodes))
    self.truncate(first, last)

  def save_to_file(self, fname, mode='a'):
    ofile = open(fname, mode)
    nNode = len(self.nodes)
    ofile.write(str(nNode) + '\n')

    for i in range(nNode):
      x, y = self.nodes[i]
      ofile.write(str(x) + ' ' + str(y) + '\n')

    ofile.close()

  def interpolate(self, slen):
    path = self.nodes
    trj = [path[0]]
    for i in range(len(path)-1):
      p1 = path[i]
      p2 = path[i+1]
    l = acc.eclidean(p1, p2)
    n = int(l/slen)
    trj += interpolate_edge(p1, p2, n)
    trj.append(p2)
    self.nodes = trj

  def add_noise(self, noise_func, params):
    noise_func(self, params)

  def __eq__(self, other):
    return self.nodes == other.nodes

class TrjSet(object):



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
    l = acc.eclidean(p1, p2)
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
  return acc.Graph(points, im)

def independent_noise(trj, xng, xp, yng = None, yp = None):
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
    p[0] += xng(*xp)
    p[1] += yng(*yp)

def additive_noise(trj, xweight, xng, xparameter, yweight=None, yng = None, yparameter = None):
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

def uniform_square_noise(trj, sizeRatio):
  '''
  \delta = random point in a square centered at node
  :param trj:
  :param sizeRatio: the ratio between the distance between two points and the edge length of the square.
  :return:
  '''
  assert(len(trj.nodes) > 1)
  p1 = trj.nodes[0]
  p2 = trj.nodes[1]
  l = sizeRatio * acc.eclidean(p1, p2)
  independent_noise(trj.nodes, acc.scaled_unif, l)

def trjs_add_noise(trjs, noise_func, parameter):
  for trj in trjs:
    noise_func(trj, parameter)

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

def save_trjs(trjs, filename):
  ofile = open(filename, 'w')
  nPath = len(trjs)
  ofile.write(str(nPath) + '\n')
  ofile.close()

  for trj in trjs:
    trj.save_to_file(filename, 'a')

