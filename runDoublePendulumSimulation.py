import matplotlib.pyplot as plt 
import numpy as np
from doublePendulum import *
import pickle
import time

'''This script is where the actual computation of the simulation is done. You enter the inital condtions
and values of mass and lengths and choose weather to update the values via the Runge-Kutta or the velocity verlet.
The entire simulated data is then saved to a file'''

#doublePendulum(length1,length2,mass1,mass2,initailAngle1,initialAngle2,steps,timestep)

#this is where you define the intial conditions for the pendulum you want to simulate
#length is m, mass is kg and angle is degrees
pendulum=doublePendulum(10,10,1,1,90,5,50,0.01)

def runSim(pendulum):
    #here if you want to change the update method then switch which value of update method is commented out, set to 'RK' by default
    
    
    updateMethod='verlet'
    #updateMethod='RK'
   
    #creates a file name that has all the intial condtions in so it is easy to find the file you need
    fileName=('DPsim-L1-'+str(pendulum.length1)+'-L2-'+str(pendulum.length2)+'-M1-'+str(pendulum.mass1)+'-M2-'+str(pendulum.mass2)+'-T1-'+str(pendulum.theta1i)+'-T2-'+str(pendulum.theta2i)+'-timestep-'+str(pendulum.dt)+'-method-'+updateMethod)
    
    #creates lists for all the steps that are filled as the simualtion runs
    timedata=[]
    theta1data=[]
    theta2data=[]
    velocity1data=[]
    velocity2data=[]
    x1data=[]
    x2data=[]
    y1data=[]
    y2data=[]
    Ekdata=[]
    Epdata=[]
    #the constants of the system, things that dont change are the things that define the simulation - used mainly for tagging files
    constants=[pendulum.length1,pendulum.length2,pendulum.mass1,pendulum.mass2,pendulum.theta1i,pendulum.theta2i,pendulum.dt]


    #This for loop is where all the computation is done, n is the total number of steps that will run which is defined when you pick initalconditions
    for i in range(pendulum.n-1):
        if updateMethod=='verlet':
            pendulum.calculateNextStepVerlet()
        elif updateMethod=='RK':
            pendulum.calculateNextStepRK()
        
        #calculate total kinetic and potential energy of system
        Ek=0.5*(pendulum.mass1+pendulum.mass2)*(pendulum.velocity1**2+pendulum.velocity2**2)
        Ep=(pendulum.mass1+pendulum.mass2)*pendulum.g*(pendulum.y1+pendulum.y2)

        #fills the lists 
        timedata.append(pendulum.t[i])
        theta1data.append(pendulum.theta1)
        theta2data.append(pendulum.theta2)
        velocity1data.append(pendulum.velocity1)
        velocity2data.append(pendulum.velocity2)
        x1data.append(pendulum.x1)
        x2data.append(pendulum.x2)
        y1data.append(pendulum.y1)
        y2data.append(pendulum.y2)
        Ekdata.append(Ek)
        Epdata.append(Ep)
    #an array of the data, makes reading and writing to files easier to have it as one list
    simulationData=[timedata,theta1data,theta2data,velocity1data,velocity2data,x1data,x2data,y1data,y2data,Ekdata,Epdata,constants]

    #writes to the file using pickle package
    with open('pendulumData/%s.pkl'% fileName,'wb') as output:
        pickle.dump(simulationData, output, pickle.HIGHEST_PROTOCOL)

runSim(pendulum)
