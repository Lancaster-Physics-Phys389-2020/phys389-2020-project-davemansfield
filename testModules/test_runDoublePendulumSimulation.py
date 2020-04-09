from doublePendulum import *
import runDoublePendulumSimulation 

test=doublePendulum(10,10,1,1,50,50,200,0.01)

def test_runSim():
    #again this function dosnt explicitly return a value so if all goes well it should return a None type
    assert runDoublePendulumSimulation.runSim(test) == None

