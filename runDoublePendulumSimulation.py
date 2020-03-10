import matplotlib.pyplot as plt
import numpy as np
from doublePendulum import *
import pickle

#doublePendulum(length1,length2,mass1,mass2,initailAngle2,initialAngle2,steps,timestep)

def main():
    test=doublePendulum(10,20,1,1,10,10,200,0.01)

    for i in range(test.n-1):
        #test.calculateNextStepRK(i)
        test.calculateNextStepVerlet(i)
        ##print (test.theta1[i])


    with open('pendulumData\pendulumFile.pkl','wb') as output:
        pickle.dump(test, output, pickle.HIGHEST_PROTOCOL)
    
main()
