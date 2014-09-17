''' The module is for reading trajectory data from Microsoft GeoLife Data Set
    This's written by Kan Huang.
    September 13th'''

from TC.accessory import Trj
import os

def file2trj(filename, xbound, ybound):
  '''
  create a trajectory from a file
  '''
  tf = open(filename, 'r')
  nodes = [] 
  if tf:
    
    for i in range(6):
      tf.readline()
     
    while True:
      line = tf.readline().rstrip()
      if not line or line=='': 
        break
      data = line.split(',')
      x = float(data[0])
      y = float(data[1])

      if xbound[0]<x<xbound[1] and ybound[0]<y<ybound[1]:
        nodes.append([float(data[0]), float(data[1])])

    trj = Trj(nodes)
    tf.close()
    return trj

  else:
    print('Can\'t open the file')
    tf.close()
    return None
  
def oneday(Dir, dayn, xbound, ybound):
  '''
  collect trajectories of geolife in one day
  '''
  trjs = []

  N = 182

  for i in range(N):
    si = str(i)
    z = '0' * (3-len(si))

    TrjDIR = Dir + z + si + '/Trajectory/'
    flist = os.listdir(TrjDIR)

    for f in flist:
      if f[:len(dayn)] == dayn:
        fullname = TrjDIR + f
        trj = file2trj(fullname, xbound, ybound)
        trjs.append(trj)

  return trjs


def alltrj(Dir, dayn, xbound, ybound):
  '''
  collect all trajectories of geolife
  '''
  trjs = []

  N = 182

  for i in range(N):
    si = str(i)
    z = '0' * (3-len(si))

    TrjDIR = Dir + z + si + '/Trajectory/'
    flist = os.listdir(TrjDIR)

    for f in flist:
      fullname = TrjDIR + f
      trj = file2trj(fullname, xbound, ybound)
      trjs.append(trj)

  return trjs
