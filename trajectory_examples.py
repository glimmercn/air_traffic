from TC.accessory import *
from TC.Trajectory import *
import copy

example = 6

if example == 1:
  g= random_graph(15, 1)
  for i in range(10):
    trj = random_path(g, 4)
    trj = interpolate_path(trj, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.02])
    trj.draw('.','r')
  for i in range(15):
    trj = random_path(g, numpy.random.randint(2, 6))
    trj = interpolate_path(trj, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.05])
    trj.draw('.','b')
  plt.show()

if example == 2:
  g= random_graph(20, 1)
  straight_trjs = []
  for i in range(10):
    trj = random_path(g, numpy.random.randint(2, 5))
    straight_trjs.append(interpolate_path(trj, 0.03))
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
    trj = random_path(g, numpy.random.randint(2, 5))
    straight_trjs.append(interpolate_path(trj, 0.03))
  low_noise_trjs, high_noise_trjs = [], []
  for trj in straight_trjs:
    t1 = copy.deepcopy(trj)
    t2 = copy.deepcopy(trj)
    weight = [1, 0.5, 0.3, 0.1]
    add_cum_noise(t1.nodes, weight, scaled_unif, [.02])
    add_cum_noise(t2.nodes, weight, scaled_unif, [.05])
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
    trj = random_path(g1, numpy.random.randint(2, 5))
    trj = interpolate_path(trj, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.05])
    trj.random_truncate()
    trjs1.append(trj)
  for i in range(t2):
    trj = random_path(g2, numpy.random.randint(2, 5))
    trj = interpolate_path(trj, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.05])
    trj.random_truncate()
    trjs2.append(trj)

  for trj in trjs1:
    trj.draw('.', 'b')
  for trj in trjs2:
    trj.draw('.', 'r')
  plt.show()

'''example 5
read trajectories of random path in a segment arrangement.
do not use this example.
'''
if example == 5:
  paths = acc.read_trajectories('paths.txt')

  trjs = []
  for path in paths:
    trjs.append(interpolate_path(path, 300))

  # for trj in trjs:
  #   trj.draw('.', 'b')

  arr = acc.read_arrangement('arr.txt')

  for seg in arr:
    acc.draw_segment(seg, '.', 'r')

  noise_trjs = copy.deepcopy(trjs)

  for trj in noise_trjs:
    add_noise(trj.nodes, scaled_unif, [400])

  for trj in noise_trjs:
    trj.draw('.', 'b')

 # plt.show()

  # save trjs and nose_trjs to files
  filename1 = '50_trajectories_without_noise.txt'
  ofile = open(filename1, 'w')
  ofile.write('50\n')
  ofile.close()

  for trj in trjs:
    trj.save_to_file(filename1, 'a')


  filename2 = '50_trajectories_with_noise.txt'
  ofile = open(filename2, 'w')
  ofile.write('50\n')
  ofile.close()

  for trj in noise_trjs:
    trj.save_to_file(filename2, 'a')


if example == 6:
  paths = acc.read_trajectories('arrangement/paths.data')

  trjs = []
  for path in paths:
    trjs.append(interpolate_path(path, 300))

  # for trj in trjs:
  #   trj.draw('.', 'b')

  arr = acc.read_arrangement('arrangement/arr.data')

  for seg in arr:
    acc.draw_segment(seg, '.', 'r')

  noise_trjs = copy.deepcopy(trjs)

  for trj in noise_trjs:
    # add_noise(trj.nodes, scaled_unif, [400])
    weight = [0.2, 0.5, 0.3]
    trj.random_truncate()
    add_cum_noise(trj.nodes, weight, scaled_unif, [400])

  for trj in noise_trjs:
    trj.draw('.', 'b')

  plt.show()

  # save trjs and nose_trjs to files
  filename1 = '50_trajectories_without_noise.txt'
  ofile = open(filename1, 'w')
  ofile.write('50\n')
  ofile.close()

  for trj in trjs:
    trj.save_to_file(filename1, 'a')


  filename2 = '50_trajectories_with_noise.txt'
  ofile = open(filename2, 'w')
  ofile.write('50\n')
  ofile.close()

  for trj in noise_trjs:
    trj.save_to_file(filename2, 'a')


