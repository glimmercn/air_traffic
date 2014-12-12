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


if __name__ == "__main__":
  pass


