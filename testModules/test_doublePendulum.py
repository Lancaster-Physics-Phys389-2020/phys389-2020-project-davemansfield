from doublePendulum import *

#here the angles passed to test don't matter as the fucntion is passed angles that should be from the update step
#but since we are testing I have selected a few values at random
test=doublePendulum(10,10,1,1,50,50,200,0.01)
def test_calculateAcceleration1():
    #since no steps have been updated yet the velocity of both bobs is 0
    #this is the value the acceleration should produce but since the accuracy of my calculater and python are not the same
    #I have rounded the results to see if they are the same to 5.dp
    assert round(test.calculateAcceleration1(10,10),5)==round(0.53314068,5)
    assert round(test.calculateAcceleration1(30,30),5)==round(0.96827099,5)
    assert round(test.calculateAcceleration1(60,60),5)==round(0.29871440,5)
    assert round(test.calculateAcceleration1(150,150),5)==round(0.70057890,5)

def test_calculateAcceleration2():
    #intailly this should always be zero and since we are testing the inital steps all must be 0
    assert test.calculateAcceleration2(10,10)==0
    assert test.calculateAcceleration2(50,50)==0
    assert test.calculateAcceleration2(130,130)==0


def test_calculateNextStepVerlet():
    #this value does not return a value explicitly so if nothing goes wrong it will return None
    assert test.calculateNextStepVerlet() == None

def test_calculateNextStepRk():
    assert test.calculateNextStepRK() == None