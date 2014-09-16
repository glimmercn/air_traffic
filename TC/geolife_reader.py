''' The module is for reading trajectory data from Microsoft GeoLife Data Set
    This's written by Kan Huang.
    September 13th'''

from TC.accessory import Trj

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

      if x<xbound and y<ybound:
        nodes.append([float(data[0]), float(data[1])])

    trj = Trj(nodes)
    tf.close()
    return trj

  else:
    print('Can\'t open the file')
    tf.close()
    return None
  


    
