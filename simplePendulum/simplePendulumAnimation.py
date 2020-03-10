import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
from simplePendulum import *

#this is not a general function needs to be passed an object

def main(pendulumObject):
    #calculate the movemnet of pendulum object - NOT A LIVE SIMULATION
    for i in range(0,pendulumObject.n-1):
        pendulumObject.calculateNextStep(i)

    fig = plt.figure()
    ax=fig.add_subplot(111,xlim=(-10,10),ylim=(-10,10))
    ax.grid()

    #the pendulum animation components
    bob, = ax.plot([],[],lw=1,color='red')
    arm,= ax.plot([0,0],[pendulumObject.xi,pendulumObject.yi],'ro-')

    xdata=[]
    ydata=[]
    def animate(i):
        xdata.append(pendulumObject.x[i])
        ydata.append(pendulumObject.y[i])
        bob.set_data(xdata[-300:],ydata[-300:])
        arm.set_data([0,pendulumObject.x[i]],[0,pendulumObject.y[i]])

        return bob, arm



    animation = FuncAnimation(fig, func=animate,interval =pendulumObject.dt,blit=True)
    plt.show()

#Pendulum(self,length,mass,initialAngle,steps,timestep)
test=Pendulum(10,3.0,30.0,100.0,0.001)  
main(test)