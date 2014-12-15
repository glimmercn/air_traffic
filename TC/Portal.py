__author__ = 'kan'
import TC.accessory as acc
import matplotlib.pyplot as plt

class Portal:

  def __init__(self, center, l):
    self.center = center
    self.l = l

  '''check whether this portal hits trajecotry'''
  def hit(self, trj):

    for p in trj.nodes:
      if self.contain(p):
        return True

    return False

  def __eq__(self, other):
    return self.center == other.center and self.l == other.l

  '''check whether this portal contains point p'''
  def contain(self, p):
    c1 = self.center[0]-self.l/2.0 <= p[0] <= self.center[0]+self.l/2.0
    c2 = self.center[1]-self.l/2.0 <= p[1] <= self.center[1]+self.l/2.0
    return c1 and c2

  def distance(self, ptl2):
    return acc.eclidean(self.center, ptl2.center)

  def draw(self, m, c):
    cx, cy = self.center
    d = self.l/2.0

    p1 = (cx-d, cy-d)
    p2 = (cx+d, cy-d)
    p3 = (cx+d, cy+d)
    p4 = (cx-d, cy+d)

    points = [p1, p2, p3, p4, p1]

    plt.plot(*zip(*points), marker=m, color=c)

def greedy_k_portal(trjs, box, l, k):
  '''
  return list of portals that greedily hit trjs.
  '''
  hlist = [False]*len(trjs)
  ptls = []

  for i in range(k):
    ptls.append(greedy_one_portal(hlist, trjs, box, l, ptls))

  return ptls

def greedy_one_portal(hlist, trjs, box, l, ptls):
  '''
  return one portal to hit most trjs that's not hit
  :param hlist: the trjs that have been hit.
  :param ptls: the portals that has been used.
  :param box: [x1, x2] * [y1, y2]. box is the area where the portal can be placed.
  '''
  xc = box[0][0]
  best = -1
  best_ptl = None
  while xc <= box[0][1]:

    yc = box[1][0]
    while yc <= box[1][1]:
      ptl = Portal((xc, yc), l)
      if ptl not in ptls:
        count = 0
        for i in range(len(hlist)):
          if not hlist[i] and ptl.hit(trjs[i]):
            count += 1

        if count > best:
          best_ptl = ptl
          best = count

      yc += l

    xc += l

  '''update hlist'''
  for i in range(len(hlist)):
    if not hlist[i] and best_ptl.hit(trjs[i]):
      hlist[i] = True

  return best_ptl

def greedy_k_pp(trjs, box, l, k):
  pass

def greedy_one_pp(hlist, trjs, box, l, ptls):
  pass