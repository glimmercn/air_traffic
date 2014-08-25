from accessery import *
example = 1

if example == 1:
  g= random_graph(15, 1)
  for i in range(10):
    path = random_path(g, 4)
    trj = interpolate_path(path, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.02])
    trj.draw('.','r')
  for i in range(10):
    path = random_path(g, numpy.random.randint(2, 6))
    trj = interpolate_path(path, 0.03)
    add_noise(trj.nodes, scaled_unif, [0.05])
    trj.draw('.','b')
  plt.show()
