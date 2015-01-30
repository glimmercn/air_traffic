__author__ = 'kan'

from TC.accessory import *
from TC.NoiseModel import *
from TC.Trajectory import *

pathFileName = 'arrangement/100_simple.paths'
arrFileName = 'arrangement/30.arr'

trjs = read_trjs(pathFileName)
arr = Arrangement(arrFileName)

l = 400                #This is the distance of an interpolation step
trjs.interpolate(l)    #interpolation
trjs.random_truncate() #truncate each trajectory in trjs from two ends randomly.

'''adding noise to trajectories
function add_noise has two parameters:
the first is the noise function.
the second is a list of parameters required by the noise function.
add_noise will call the noise function with the given parameters for each trajectory in trjs.

In this example, uniform_square_noise is added. We pick a point in a square centered at the
point to replace the point. This noise function only needs one parameter, the ratio between
the length of an edge of the square and the distance between two consecutive points
 in the trajectory.

'''
params = [1]
trjs.add_noise(uniform_square_noise, params)

'''visualization
the first parameter is the marker of a point.
the second parameter is the color.
'''
trjs.visualize('', 'red')
plt.show()


