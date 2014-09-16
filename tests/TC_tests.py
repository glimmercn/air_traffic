from nose.tools import *
from TC.geolife_reader import *

def test_file2trj():
  filename = '1.plt'
  trj = file2trj(filename)
  data = [[40.013762,116.306629,'23:14:28'], [40.013856,116.306599, '23:14:30']]
  trj2 = Trj(data)
  
  assert_equal(trj.nodes, trj2.nodes)




                    
