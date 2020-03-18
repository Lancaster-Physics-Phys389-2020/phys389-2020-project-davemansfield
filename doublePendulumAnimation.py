import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy
import pickle

'''This script runs a matplotlib animation that can be saved as an mp4. It takes reads data of a simulation from a file and plots
the x and y coordinate of the bob as it moves showing its trail behind. It is not a live simualtion and to show you must first use 
runDoublePendulumSimulation.py with a set of inital condtions to save the neccacerry data
'''

def main(x1,x2,y1,y2,constants):
    #main is passed these arguments which are all lists and are the computed values for all steps of the double pendulum
    #calcuate the size of the screen so all sizes of pendulum can fit
    screenSize=constants[0]+constants[1]+5

    #calculate the movemnet of pendulum object - NOT A LIVE SIMULATION
    fig = plt.figure()
    ax=fig.add_subplot(111,xlim=(-screenSize,screenSize),ylim=(-screenSize,screenSize))
    ax.grid()

    #the pendulum animation components and thier intial positions
    bob1, = ax.plot([],[],lw=1,color='red')
    arm1,= ax.plot([0,0],[x1[0],y1[0]],'ko-')
    bob2, = ax.plot([],[],lw=1,color='blue')
    arm2, = ax.plot([x1[0],y1[0]],[x2[0],y2[0]],'ko-') 

    #these lists save all the x and y coordinates of the bob, these are calculated in the update step done in runDoublePendulumSimulation.py
    x1data=[]
    x2data=[]
    y1data=[]
    y2data=[]
    def animate(i):
        #FuncAnimation is part of matplotlib and is an iterative subroutine hence the iterator i
        #adds the i'th x and y postion to each bob then plots it
        x1data.append(x1[i])
        y1data.append(y1[i])
        x2data.append(x2[i])
        y2data.append(y2[i])
        #show the postion of the bobs and a trail for the last 300 postions to show how its moved
        #To show for all posions remove all 4 '[-300:]'
        bob1.set_data(x1data[-300:],y1data[-300:])
        arm1.set_data([0,x1[i]],[0,y1[i]])
        bob2.set_data(x2data[-300:],y2data[-300:])
        arm2.set_data([x1[i],x2[i]],[y1[i],y2[i]])

        return bob1, arm1, bob2, arm2


    #this makes use of FuncAnimation from matplotlib. The interval is the timestep given in runDoublePendulumSimulation.py
    animation = FuncAnimation(fig, func=animate,interval =constants[6],blit=True)
    plt.show()
    #you can choose weather or not to save the simualtion as an mp4, set to False as a default
#doublePendulum(length1,length2,mass1,mass2,initailAngle2,initialAngle2,steps,timestep)

#the name of the file contaitnng the simualtion data you want to see animnated
fileToRead='DPsim-L1-10-L2-20-M1-1-M2-1-T1-10-T2-45-timestep-0.01-method-RK'
with open('pendulumData/%s.pkl'% fileToRead,'rb') as input:
    pendulum=pickle.load(input)

main(pendulum[5],pendulum[6],pendulum[7],pendulum[8],pendulum[11])