import numpy as np

''' This class creates a double pendulum objects that stores all the important values as they update
there are 2 diffrernt types of iterativve methods, the velocity verlet and the Runge-Kutta methods, that 
update the velocity and angle of the bob. More importnat quntiites like x and y coordinates can be dervied
from these quantities'''
class doublePendulum():
    g=9.8 # Acceleration due to gravity
    def __init__(self,length1, length2, mass1, mass2, initialAngle1, initialAngle2, steps, timestep):
        #doublePendulum(length1,length2,mass1,mass2,initailAngle2,initialAngle2,steps,timestep)
        self.dt=timestep #timestep
        self.steps=steps
        
        #setting the initial conditions
        self.length1=length1
        self.mass1=mass1
        self.length2=length2
        self.mass2=mass2
        self.t=np.arange(0,self.steps,self.dt) #stored as an array as it is the same in every simulation and is plotted easier
        self.n=len(self.t) #n is the number of iterations that will run for a given set of initial conditons
        self.theta1i=initialAngle1 #saves the intial angle in degrees
        self.theta1=np.radians(initialAngle1)
        self.velocity1=np.radians(0.0) 
        self.theta2i=initialAngle2
        self.theta2=np.radians(initialAngle2)
        self.velocity2=np.radians(0.0) 
        
        #inital x and y for both bobs, used in the animation of the simulation
        self.x1=np.sin(initialAngle1)*self.length1
        self.y1=-np.cos(initialAngle1)*self.length1
        self.x2=self.x1+(np.sin(initialAngle2)*self.length2)
        self.y2=-(self.y1+(np.cos(initialAngle2)*self.length2))


    def calculateAcceleration1(self,theta1,theta2):
        
        '''Acceleration calculation for the first bob takes arguments theta1 and theta2 as they are the 
        corrected values calculated in the Runge-Kutta / verlet method'''
        
        A=self.mass2/self.mass1
        B=self.length2/self.length1
        G=self.g/self.length1
        a = -(((1+A)*G*np.sin(theta1)) + (A*B*self.velocity2**2*np.sin(theta1-theta2)) + (A*np.cos(theta1-theta2)*(self.velocity1**2*np.sin(theta1-theta2) - G*np.sin(theta1)))) / (1+A*(np.sin(theta1-theta2)**2))
        return a 
    
    def calculateAcceleration2(self,theta1,theta2):
        #Acceleration calculation for the seocnd bob same srguments as calculateAcceleration1
        A=self.mass2/self.mass1
        B=self.length2/self.length1
        G=self.g/self.length1        
        a = (((1+A)*(self.velocity1*np.sin(theta1-theta2) - G*np.sin(theta2))) + ( (np.cos(theta1-theta2)) * ( (1+A)*G*np.sin(theta1) + A*B*self.velocity2**2 * np.sin(theta1-theta2)))) / (B*(1+A*(np.sin(theta1-theta2)**2)))
        return a

    def calculateNextStepVerlet(self):
        #this is the velocity verlet iteration method for updating the values of angle and velocity
        self.theta1=self.theta1+(self.velocity1*self.dt+0.5*self.calculateAcceleration1(self.theta1,self.theta2)*self.dt*self.dt)
        self.theta2=self.theta2+(self.velocity2*self.dt+0.5*self.calculateAcceleration2(self.theta1,self.theta2)*self.dt*self.dt)
        self.velocity1=self.velocity1+self.calculateAcceleration1(self.theta1,self.theta2)*self.dt
        self.velocity2=self.velocity2+self.calculateAcceleration2(self.theta1,self.theta2)*self.dt


        self.x1=np.sin(self.theta1)*self.length1
        self.y1=-np.cos(self.theta1)*self.length1
        self.x2=self.x1+(np.sin(self.theta2)*self.length2)
        self.y2=(self.y1-(np.cos(self.theta2)*self.length2))

    def calculateNextStepRK(self):
        #Implementation of Runge-Kutta iteration method
        k1theta1 = self.dt * self.velocity1
        k1theta2 = self.dt * self.velocity2
        k1v1 = self.dt * self.calculateAcceleration1(self.theta1,self.theta2)
        k1v2 = self.dt * self.calculateAcceleration2(self.theta1,self.theta2)

        k2theta1 = self.dt * (self.velocity1 + 0.5 * k1v1)
        k2theta2 = self.dt * (self.velocity2 + 0.5 * k1v2)
        k2v1 = self.dt * self.calculateAcceleration1((self.theta1 + 0.5 * k1theta1), (self.theta2+0.5*k1theta2))
        k2v2 = self.dt * self.calculateAcceleration2((self.theta1 + 0.5 * k1theta1), (self.theta2+0.5*k1theta2))

        k3theta1 = self.dt * (self.velocity1 + 0.5 * k2v1)
        k3theta2 = self.dt * (self.velocity2 + 0.5 * k2v2)
        k3v1 = self.dt * self.calculateAcceleration1((self.theta1 + 0.5 * k2theta1), (self.theta2+0.5*k2theta2))
        k3v2 = self.dt * self.calculateAcceleration2((self.theta1 + 0.5 * k2theta1), (self.theta2+0.5*k2theta2))

        k4theta1 = self.dt * (self.velocity1 + k3v1)
        k4theta2 = self.dt * (self.velocity2 + k3v2)
        k4v1 = self.dt * self.calculateAcceleration1((self.theta1 + k3theta1),(self.theta2+k3theta2))
        k4v2 = self.dt * self.calculateAcceleration2((self.theta1 + k3theta1),(self.theta2+k3theta2))

        #Increse step by calculating a weighted avergae
        self.theta1 = self.theta1 + (k1theta1 + 2 * k2theta1 + 2 * k3theta1 + k4theta1) / 6.0
        self.theta2 = self.theta2 + (k1theta2 + 2 * k2theta2 + 2 * k3theta2 + k4theta2) / 6.0
        self.velocity1 = self.velocity1 + (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1) / 6.0
        self.velocity2 = self.velocity2 + (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2) / 6.0
        
        #Update the cartisain coordinates
        self.x1=np.sin(self.theta1)*self.length1
        self.y1=-np.cos(self.theta1)*self.length1
        self.x2=self.x1+(np.sin(self.theta2)*self.length2)
        self.y2=(self.y1-(np.cos(self.theta2)*self.length2))
