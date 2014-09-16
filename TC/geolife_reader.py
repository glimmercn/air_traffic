''' The module is for reading trajectory data from Microsoft GeoLife Data Set
    This's written by Kan Huang.
    September 13th'''

from TC.accessory import Trj

def file2trj(filename):
  '''
  create a trajectory from a file
  '''
  tf = open(filename, 'r')
  nodes = [] 
  if tf:
    
    while tf.readline() != '0\n':
      pass
    
    while True:
      line = tf.readline().rstrip()
      if not line or line=='': 
        break
      data = line.split(',')
      nodes.append([float(data[0]), float(data[1]), data[-1]])

    trj = Trj(nodes)
    return trj

  else:
    print('Can\'t open the file')
    return None
  


    
