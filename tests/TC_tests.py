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

def test_greedy_k_portal():
  
  trj1 = Trj([[0.5, 0.5], [2, 0.5]])
  trj2 = Trj([[0.5, 0.6], [2, 0.6]])
  trj3 = Trj([[0.6, 0.3], [0.6, 2]])
  trj4 = Trj([[1.2, 2.0], [2.0, 2.0]])

  trjs = [trj1, trj2, trj3, trj4]
  
  ptl1 = Portal((0.0, 0.0), 2.0)
  ptl2 = Portal((2.0, 2.0), 2.0)

  box = [[0.0, 4.0], [0.0, 4.0]]
  l = 2

  ptlg1 = greedy_k_portal(trjs, box, l, 1)
  ptlg2 = greedy_k_portal(trjs, box, l, 2)
  
  assert_equal(ptlg1[0], ptl1)
  assert_equal(ptlg2[0], ptl1)
  assert_equal(ptlg2[1], ptl2)
#  trj = Trj([[-10, 1], [10, -1]])
#  t3 = ptl.hit(trj)
#  assert_equal(t3, True)



                    
