from TC.accessory import *
from TC.geolife_reader import file2trj
import copy
import os

DIR = 'Data/Geolife/Data/'
trjs = []
N = 100

xbound = 50
ybound = 130
for i in range(N+1):
  si = str(i)
  z = '0' * (3 - len(si))
  
  TrjDIR = DIR + z + si + '/Trajectory/'
  flist = os.listdir(TrjDIR)
  
  for f in flist:
    fullname = TrjDIR + f
    trj = file2trj(fullname, xbound, ybound)
    trjs.append(trj)

for trj in trjs:
  trj.draw('.', 'r')

plt.show()
