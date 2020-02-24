import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

g=9.8
dt=0.0025

class Pendulum():
    def __init__(self,length,mass,initialAngle,steps):
        self.length=length
        self.mass=mass
        self.steps=steps

        self.t=np.arange(0,self.steps,dt) #are these two lines nessacerry?
        self.n=len(self.t) 

        self.theta=np.zeros(self.n)
        self.velocity=np.zeros(self.n)
        self.theta[0]=np.radians(initialAngle)
        self.velocity[0]=np.radians(0.0) 

    def calculateCoordiantes(self,angle,length):
        x=np.sin(angle)*length
        y=np.cos(angle)*length
        return x,y

    def calculateAcceleration(self,theta):
        a = -(g/self.length)*np.sin(theta)
        return a 

    def calculateNextStep(self,i):
        k1theta = dt * self.velocity[i]
        k1v = dt * self.calculateAcceleration(self.theta[i])

        k2theta = dt * (self.velocity[i] + 0.5 * k1v)
        k2v = dt * self.calculateAcceleration(self.theta[i] + 0.5 * k1theta)

        k3theta = dt * (self.velocity[i] + 0.5 * k2v)
        k3v = dt * self.calculateAcceleration(self.theta[i] + 0.5 * k2theta)

        k4theta = dt * (self.velocity[i] + k3v)
        k4v = dt * self.calculateAcceleration(self.theta[i] + k3theta)

        #next value of y from wighted avergae - (this may be wrong)
        self.theta[i+1] = self.theta[i] + (k1theta + 2 * k2theta + 2 * k3theta + k4theta) / 6.0 
        self.velocity[i+1] = self.velocity[i] + (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0
    
    def plot(self):
        #plots angle agaist time
        plt.plot(self.t,self.theta)
        plt.title('SIMPLE PENDULUM')
        plt.xlabel('time')
        plt.ylabel('theta')
        plt.grid(True)
        plt.show()


def main():
    testpen=Pendulum(12.0,3.0,90.0,10.0)
    for i in range(0,testpen.n-1):
        testpen.calculateNextStep(i)
    testpen.plot()


if __name__ == '__main__':
    main()