from nose.tools import *
from TC.geolife_reader import *
from TC.accessory import *

def test_file2trj():
  filename = '1.plt'
  trj = file2trj(filename, [0, 100], [0, 200])
  data = [[40.013762,116.306629], [40.013856,116.306599]]
  trj2 = Trj(data)
  
  assert_equal(trj.nodes, trj2.nodes)

def test_portal():
  ptl = Portal([0, 0], 5)

  t1 = ptl.contain([2, 2])
  assert_equal(t1, True)

  t2 = ptl.contain([0, 10])
  assert_equal(t2, False)

#  trj = Trj([[-10, 1], [10, -1]])
#  t3 = ptl.hit(trj)
#  assert_equal(t3, True)



                    
