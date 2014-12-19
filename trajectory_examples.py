from TC.accessory import *
from TC.Trajectory import *
from TC.NoiseModel import *
import copy

example = 6

if example == 1:
  g= random_graph(15, 1)
  for i in range(10):
    trj = random_trj_from_graph(g, 4)
    trj = trj.interpolate(0.03)
    add_trj_independent_noise(trj, scaled_unif, [0.02])
    trj.draw('.','r')
  for i in range(15):
    trj = random_trj_from_graph(g, numpy.random.randint(2, 6))
    trj = trj.interpolate(0.03)
    add_trj_independent_noise(trj, scaled_unif, [0.05])
    trj.draw('.','b')
  plt.show()

if example == 2:
  g= random_graph(20, 1)
  straight_trjs = []
  for i in range(10):
    trj = random_trj_from_graph(g, numpy.random.randint(2, 5))
    straight_trjs.append(trj.interpolate(0.03))
  low_noise_trjs, high_noise_trjs = [], []

  for trj in straight_trjs:
    t1 = copy.deepcopy(trj)
    t2 = copy.deepcopy(trj)
    add_trj_independent_noise(t1, scaled_unif, [0.02])
    add_trj_independent_noise(t2, scaled_unif, [0.05])
    low_noise_trjs.append(t1)
    high_noise_trjs.append(t2)
  for trj in low_noise_trjs:
    trj.draw('.','b')
  for trj in high_noise_trjs:
    trj.draw('.', 'r')
  plt.show()

if example == 3:
  g= random_graph(20, 1)
  straight_trjs = []
  for i in range(10):
    trj = random_trj_from_graph(g, numpy.random.randint(2, 5))
    straight_trjs.append(trj.interpolate(0.03))
  low_noise_trjs, high_noise_trjs = [], []
  for trj in straight_trjs:
    t1 = copy.deepcopy(trj)
    t2 = copy.deepcopy(trj)
    weight = [1, 0.5, 0.3, 0.1]
    add_cumulative_noise(t1, weight, scaled_unif, [.02])
    add_cumulative_noise(t2, weight, scaled_unif, [.05])
    low_noise_trjs.append(t1)
    high_noise_trjs.append(t2)
  for trj in low_noise_trjs:
    trj.draw('.','b')
  for trj in high_noise_trjs:
    trj.draw('.', 'r')
  plt.show()

# example of G1 vs G2
if example == 4:
  g1 = random_graph(20, 1)
  g2 = random_graph(10, 1)
  tn = 50
  percent = 0.8
  t1 = int(tn * percent)
  t2 = tn - t1

  trjs1, trjs2 = [], []
  for i in range(t1):
    trj = random_trj_from_graph(g1, numpy.random.randint(2, 5))
    trj = trj.interpolate(0.03)
    add_trj_independent_noise(trj, scaled_unif, [0.05])
    trj.random_truncate()
    trjs1.append(trj)
  for i in range(t2):
    trj = random_trj_from_graph(g2, numpy.random.randint(2, 5))
    trj = trj.interpolate(0.03)
    add_trj_independent_noise(trj, scaled_unif, [0.05])
    trj.random_truncate()
    trjs2.append(trj)

  for trj in trjs1:
    trj.draw('.', 'b')
  for trj in trjs2:
    trj.draw('.', 'r')
  plt.show()



if example == 5:
  nPath = 50
  arrSize = 20
  trjs, arr = data_input(nPath, 'simple_uniform', arrSize)
  trjs.interpolate(400)

  # for seg in arr:
  #   acc.draw_segment(seg, '.', 'r')
  # draw_arrangement(arr, 'o', 'r')
  noise_trjs = copy.deepcopy(trjs)
  noise_trjs.random_truncate()
  weight = [.2, .6, .2]
  params = weight, scaled_unif, [700]
  noise_trjs.add_noise(add_cumulative_noise, params)
  noise_trjs.visualize('', 'b')

  plt.show()

  # save trjs and nose_trjs to files
  noise_trjs.save()

if example == 6:
  nPath = 50
  arrSize = 20
  trjs, arr = data_input(nPath, 'simple_uniform', arrSize)
  trjs.interpolate(400)

  # for seg in arr:
  #   acc.draw_segment(seg, '.', 'r')
  # draw_arrangement(arr, 'o', 'r')
  noise_trjs = copy.deepcopy(trjs)
  noise_trjs.random_truncate()
  noise_trjs2 = copy.deepcopy(noise_trjs)

  params = 0.8, scaled_unif, [900]
  noise_trjs.add_noise(add_pull_noise, params)
  noise_trjs.visualize('', 'b')

  weight = [.2, .6, .2]
  params = weight, scaled_unif, [900]
  noise_trjs2.add_noise(add_cumulative_noise, params)
  noise_trjs2.visualize('', 'r')

  draw_arrangement(arr, '*', 'green')
  plt.show()

  # save trjs and nose_trjs to files
  noise_trjs.save()
