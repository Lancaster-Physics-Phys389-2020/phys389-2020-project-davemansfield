import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Pendulum():
    def __init__(self,length,mass,angle):
        self.length=length
        self.mass=mass
        self.angle=angle

    def calculateCoordiantes(self,angle,length):
        x=np.sin(angle)*length
        y=np.cos(angle)*length
        return x,y
    

def acceleration(theta):
    g=9.8
    l=12.0
    r=2.0
    m=3.0
    a = -(m*g*r/l)*np.sin(theta)
    return a

def main():
    g=9.8#acceleration due to gravity
    steps=10.0
    dt=0.0025 #timestep
    itheta=90.0 #inital angle
    
    ##########TEMP###########
    t=np.arange(0,steps,dt)
    n=len(t)

    y=np.zeros(n)
    v=np.zeros(n)
    y[0]=np.radians(itheta) #set inital value of theta (angle)
    v[0]=np.radians(0.0) #same for velocity

    for i in range(0,n-1):
        k1y = dt * v[i]
        k1v = dt * acceleration(y[i])

        k2y = dt * (v[i] + 0.5 * k1v)
        k2v = dt * acceleration(y[i] + 0.5 * k1y)

        k3y = dt * (v[i] + 0.5 * k2v)
        k3v = dt * acceleration(y[i] + 0.5 * k2y)

        k4y = dt * (v[i] + k3v)
        k4v = dt * acceleration(y[i] + k3y)

        #next value of y from wighted avergae - (this may be wrong)
        y[i+1] = y[i] + (k1y + 2 * k2y + 2 * k3y + k4y) / 6.0 
        v[i+1] = v[i] + (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0

    plt.plot(t,y)
    plt.title('PEN')
    plt.xlabel('time')
    plt.ylabel('angle')
    plt.grid(True)
    plt.show()



main()
#if __name__ == '__main__':
    #main()