import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
from doublePendulum import *
import pickle

def main(pendulumObject):
    #calcuate the size of the screen so all sizes of pendulum can fit
    screenSize=pendulumObject.length1+pendulumObject.length2+5

    #calculate the movemnet of pendulum object - NOT A LIVE SIMULATION
    fig = plt.figure()
    ax=fig.add_subplot(111,xlim=(-screenSize,screenSize),ylim=(-screenSize,screenSize))
    ax.grid()

    #the pendulum animation components
    bob1, = ax.plot([],[],lw=1,color='red')
    arm1,= ax.plot([0,0],[pendulumObject.x1[0],pendulumObject.y1[0]],'ko-')
    bob2, = ax.plot([],[],lw=1,color='blue')
    arm2, = ax.plot([pendulumObject.x1[0],pendulumObject.y1[0]],[pendulumObject.x2[0],pendulumObject.y2[0]],'ko-') 

    x1data=[]
    y1data=[]
    x2data=[]
    y2data=[]
    def animate(i):
        x1data.append(pendulumObject.x1[i])
        y1data.append(pendulumObject.y1[i])
        x2data.append(pendulumObject.x2[i])
        y2data.append(pendulumObject.y2[i])
        #show the postion of the bobs and a trail for the last 300 postions to show how its moved
        bob1.set_data(x1data[-300:],y1data[-300:])
        arm1.set_data([0,pendulumObject.x1[i]],[0,pendulumObject.y1[i]])
        bob2.set_data(x2data[-300:],y2data[-300:])
        arm2.set_data([pendulumObject.x1[i],pendulumObject.x2[i]],[pendulumObject.y1[i],pendulumObject.y2[i]])

        return bob1, arm1, bob2, arm2



    animation = FuncAnimation(fig, func=animate,interval =pendulumObject.dt,blit=True)
    plt.show()
    if save:
        animation.save('doublePendulum.mp4')


#doublePendulum(length1,length2,mass1,mass2,initailAngle2,initialAngle2,steps,timestep)
with open('pendulumData\pendulumFile.pkl','rb') as input:
    pendulum=pickle.load(input)
save=False
main(pendulum)