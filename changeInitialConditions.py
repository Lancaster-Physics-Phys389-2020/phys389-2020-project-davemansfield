from runDoublePendulumSimulation import *
import matplotlib.pyplot as plt 
import numpy as np
from doublePendulum import *
import pickle
'''This script is used to run multiple simulations at once for a given inital condtion  that is changing in a range.
This may be useful, for example, to test lots of angles to see what angle will casue the second bob to flip
'''

#doublePendulum(length1,length2,mass1,mass2,initailAngle1,initialAngle2,steps,timestep)
#here set the range and the test value to condition
# to add multiple you may add a nested for loop with a diffrent iterator 
for condition in range(10,13,1):
    pendulum=doublePendulum(10,20,1,1,condition,10,200,0.01)
    runSim(pendulum)