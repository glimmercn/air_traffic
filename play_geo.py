from TC.accessory import *
from TC.geolife_reader import file2trj, oneday
from TC.Portal import greedy_k_portal
import copy
import os

DIR = 'Data/Geolife/Data/'
trjs = []
N = 100

xbound = [0, 50]
ybound = [0, 130]
dayn = '20090111'

trjs = oneday(DIR, dayn, xbound, ybound)



for trj in trjs:
  trj.draw('.', 'r')

box = [(39, 40), (116, 118)]
l = 0.02
ptls = greedy_k_portal(trjs, box, l, 2)


for ptl in ptls:
  print(ptl.center)
  ptl.draw('.', 'b')

plt.show()


