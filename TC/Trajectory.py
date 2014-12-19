__author__ = 'kan'

import numpy
import matplotlib.pyplot as plt
import TC.accessory as acc
from TC.Arrangement import Arrangement

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

  def save(self, fname, mode='a'):
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
      trj += acc.interpolate_edge(p1, p2, n)
      trj.append(p2)
    self.nodes = trj

  def add_noise(self, noise_func, params):
    noise_func(self, *params)

  def __eq__(self, other):
    return self.nodes == other.nodes

class TrjSet(object):
  def __init__(self, trjs):
    self.trjs = trjs
    self.noise_type= None

  def save(self, filename = None):
    if filename == None:
      filename = str(len(self.trjs)) + '_' + 'trjs' + '_' + self.noise_type + '.dat'
    ofile = open(filename, 'w')
    nPath = len(self.trjs)
    ofile.write(str(nPath) + '\n')
    ofile.close()

    for trj in self.trjs:
      trj.save(filename, 'a')

  def interpolate(self, slen):
    for trj in self.trjs:
      trj.interpolate(slen)

  def add_noise(self, noise_func, params):
    self.noise_type = noise_func.name
    for trj in self.trjs:
      trj.add_noise(noise_func, params)

  def visualize(self, m, c):
    for trj in self.trjs:
      trj.draw(m, c)

  def random_truncate(self):
    for trj in self.trjs:
      trj.random_truncate()

  def __eq__(self, other):
    b1 = self.noise_type == other.noise_state
    b2 = self.trjs == other.trjs
    return b1 and b2

def read_trjs(fname):
  '''
  read trajectories from a file created by CGAL code
  :param fname:
  :return:
  '''
  f = open(fname)
  nTra = int(f.readline().strip())
  paths = []
  for i in range(nTra):
    nVertex = int(f.readline().strip())
    path = []

    for j in range(nVertex):
      l = f.readline().strip().split()
      assert(len(l) == 2)
      v = [float(x) for x in l]
      path.append(v)

    paths.append(Trj(path))

  return TrjSet(paths)


def data_input(nPath, path_type, arrSize):
  pathFileName = 'arrangement/' + str(nPath) + '_' + path_type + '.paths'
  paths = read_trjs(pathFileName)

  arrFileName = 'arrangement/' + str(arrSize) + '.arr'
  arr = Arrangement()
  arr.input_from_file(arrFileName)

  return paths, arr
