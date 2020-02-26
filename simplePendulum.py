import matplotlib.pyplot as plt
import numpy as np

class Pendulum():
    g=9.8
    def __init__(self,length,mass,initialAngle,steps,timestep):
        self.dt=timestep #timestep
        self.length=length
        self.mass=mass
        self.steps=steps

        self.t=np.arange(0,self.steps,self.dt) #are these two lines nessacerry?
        self.n=len(self.t) 

        self.theta=np.zeros(self.n)
        self.velocity=np.zeros(self.n)
        self.theta[0]=np.radians(initialAngle)
        self.velocity[0]=np.radians(0.0) 

        self.xi=np.sin(initialAngle)*self.length #inital x and y
        self.yi=np.cos(initialAngle)*self.length

    def calculateXCoordinate(self,angle): #these may not be needed
        x=np.sin(angle)*self.length
        return x

    def calculateYCoordinate(self,angle):
        y=np.cos(angle)*self.length
        return y

    def calculateAcceleration(self,theta):
        a = -(self.g/self.length)*np.sin(theta)
        return a 

    def calculateNextStep(self,i):
        k1theta = self.dt * self.velocity[i]
        k1v = self.dt * self.calculateAcceleration(self.theta[i])

        k2theta = self.dt * (self.velocity[i] + 0.5 * k1v)
        k2v = self.dt * self.calculateAcceleration(self.theta[i] + 0.5 * k1theta)

        k3theta = self.dt * (self.velocity[i] + 0.5 * k2v)
        k3v = self.dt * self.calculateAcceleration(self.theta[i] + 0.5 * k2theta)

        k4theta = self.dt * (self.velocity[i] + k3v)
        k4v = self.dt * self.calculateAcceleration(self.theta[i] + k3theta)

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