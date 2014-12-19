__author__ = 'kan'
import matplotlib.pyplot as plt

class Arrangement(object):
  def __init__(self):
    self.segments = None

  def input_from_file(self, fname):
    f = open(fname)
    nSeg = int(f.readline().strip())
    segs = []

    for i in range(nSeg):
      l = f.readline().strip().split()
      assert(len(l) == 4)
      seg = [float(x) for x in l]
      segs.append(seg)

    self.segments = segs

  def visualize(self, m, c):
    for seg in self.segments:
      draw_segment(seg, m, c)

def draw_segment(seg, m, c):
  '''
  plot a segment
  :param seg: a 4-tuple
  :param m:
  :param c:
  :return:
  '''
  plt.plot([seg[0], seg[2]], [seg[1], seg[3]], marker = m, color = c)

