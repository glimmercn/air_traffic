from accessory import *
import copy
example = 2

if example == 1:
  g= random_graph(15, 1)
  for i in range(10):
    path = random_path(g, 4)
    trj = interpolate_path(path, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.02])
    trj.draw('.','r')
  for i in range(15):
    path = random_path(g, numpy.random.randint(2, 6))
    trj = interpolate_path(path, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.05])
    trj.draw('.','b')
  plt.show()

if example == 2:
  g= random_graph(20, 1)
  straight_trjs = []
  for i in range(10):
    path = random_path(g, numpy.random.randint(2, 5))
    straight_trjs.append(interpolate_path(path, 0.03))
  low_noise_trjs, high_noise_trjs = [], []
  for trj in straight_trjs:
    t1 = copy.deepcopy(trj)
    t2 = copy.deepcopy(trj)
    add_noise(t1.nodes, scaled_unif, [0.02])
    add_noise(t2.nodes, scaled_unif, [0.05])
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
    path = random_path(g, numpy.random.randint(2, 5))
    straight_trjs.append(interpolate_path(path, 0.03))
  low_noise_trjs, high_noise_trjs = [], []
  for trj in straight_trjs:
    t1 = copy.deepcopy(trj)
    t2 = copy.deepcopy(trj)
    weight = [1, 0.5, 0.3, 0.1]
    add_cum_noise(weight, weight,t1.nodes, scaled_unif, [.02])
    add_cum_noise(weight, weight,t2.nodes, scaled_unif, [.05])
    low_noise_trjs.append(t1)
    high_noise_trjs.append(t2)
  for trj in low_noise_trjs:
    trj.draw('.','b')
  for trj in high_noise_trjs:
    trj.draw('.', 'r')
  plt.show()

