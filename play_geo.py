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
dayn = '20081208'

trjs = oneday(DIR, dayn, xbound, ybound)



for trj in trjs:
  trj.draw('.', 'r')

box = [(20, 40), (0, 100)]
l = 10
ptls = greedy_k_portal(trjs, box, l, 2)


for ptl in ptls:
  print(ptl.center)
  ptl.draw('.', 'b')

plt.show()

#
#
#
# count = 0
# for i in range(N+1):
#   si = str(i)
#   z = '0' * (3 - len(si))
#
#   TrjDIR = DIR + z + si + '/Trajectory/'
#   flist = os.listdir(TrjDIR)
#
#   for f in flist:
#     count += 1
#     fullname = TrjDIR + f
#     trj = file2trj(fullname, xbound, ybound)
#     trjs.append(trj)

