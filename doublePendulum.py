import matplotlib.pyplot as plt
import numpy as np

class doublePendulum():
    g=9.8
    def __init__(self,length1, length2, mass1, mass2, initialAngle1, initialAngle2, steps, timestep):
        #doublePendulum(length1,length2,mass1,mass2,initailAngle2,initialAngle2,steps,timestep)
        self.dt=timestep #timestep
        self.steps=steps
        
        self.length1=length1
        self.mass1=mass1
        self.length2=length2
        self.mass2=mass2

        self.t=np.arange(0,self.steps,self.dt)
        self.n=len(self.t) #n is the number of iterations

        #Creates array of 0s with the amount of elements that will be calculated when the program runs
        self.Ek=np.zeros(self.n) #Kinetic energy
        self.Ek[0]=0
        self.Ep=np.zeros(self.n) #Potential energy
        self.Ep[0]=-self.mass1*self.g*self.length1*np.cos(initialAngle1)+self.mass2*self.g*(self.length1*np.cos(initialAngle1)+self.length2*np.cos(initialAngle2))
        self.Et=np.zeros(self.n) #Total energy
        self.Et[0]=self.Ek[0]+self.Ep[0]

        self.theta1=np.zeros(self.n)
        self.velocity1=np.zeros(self.n)
        self.theta1[0]=np.radians(initialAngle1)
        self.velocity1[0]=np.radians(0.0) 
        
        self.theta2=np.zeros(self.n)
        self.velocity2=np.zeros(self.n)
        self.theta2[0]=np.radians(initialAngle2)
        self.velocity2[0]=np.radians(0.0) 

        #Cartiesian coordinates
        self.x1=np.zeros(self.n)
        self.y1=np.zeros(self.n)
        self.x2=np.zeros(self.n)
        self.y2=np.zeros(self.n)
        
        #inital x and y for both bobs
        self.x1[0]=np.sin(initialAngle1)*self.length1
        self.y1[0]=-np.cos(initialAngle1)*self.length1
        self.x2[0]=self.x1[0]+(np.sin(initialAngle2)*self.length2)
        self.y2[0]=-(self.y1[0]+(np.cos(initialAngle2)*self.length2))


    def calculateAcceleration1(self,theta1,theta2,i):
        #Acceleration calculation for the first bob
        A=self.mass2/self.mass1
        B=self.length2/self.length1
        G=self.g/self.length1
        a = -(((1+A)*G*np.sin(theta1)) + (A*B*self.velocity2[i]**2*np.sin(theta1-theta2)) + (A*np.cos(theta1-theta2)*(self.velocity1[i]**2*np.sin(theta1-theta2) - G*np.sin(theta1)))) / (1+A*(np.sin(theta1-theta2)**2))
        return a 
    
    def calculateAcceleration2(self,theta1,theta2,i):
        #Acceleration calculation for the seocnd bob
        A=self.mass2/self.mass1
        B=self.length2/self.length1
        G=self.g/self.length1        
        a = (((1+A)*(self.velocity1[i]*np.sin(theta1-theta2) - G*np.sin(theta2))) + ( (np.cos(theta1-theta2)) * ( (1+A)*G*np.sin(theta1) + A*B*self.velocity2[i]**2 * np.sin(theta1-theta2)))) / (B*(1+A*(np.sin(theta1-theta2)**2)))
        return a

    def calculateEnergy(self,i,td1,td2):
        #calculates the angular velociy for kinetic energy formula
        E=0.5*self.mass1*(td1)**2*self.length1**2 + 0.5*self.mass2*( (td1)**2*self.length1**2+(td2)**2*self.length2**2 + 2*td1*self.length1*td2*self.length2*np.cos(self.theta1[i]-self.theta2[i]) )
        return E


    def calculateNextStepVerlet(self,i):
        self.theta1[i+1]=self.theta1[i]+(self.velocity1[i]*self.dt+0.5*self.calculateAcceleration1(self.theta1[i],self.theta2[i],i)*self.dt*self.dt)
        self.theta2[i+1]=self.theta2[i]+(self.velocity2[i]*self.dt+0.5*self.calculateAcceleration2(self.theta1[i],self.theta2[i],i)*self.dt*self.dt)
        self.velocity1[i+1]=self.velocity1[i]+self.calculateAcceleration1(self.theta1[i],self.theta2[i],i)*self.dt
        self.velocity2[i+1]=self.velocity2[i]+self.calculateAcceleration2(self.theta1[i],self.theta2[i],i)*self.dt

        self.x1[i]=np.sin(self.theta1[i])*self.length1
        self.y1[i]=-np.cos(self.theta1[i])*self.length1
        self.x2[i]=self.x1[i]+(np.sin(self.theta2[i])*self.length2)
        self.y2[i]=(self.y1[i]-(np.cos(self.theta2[i])*self.length2))

    def calculateNextStepRK(self,i):
        #Implementation of Runge-Kutta
        k1theta1 = self.dt * self.velocity1[i]
        k1theta2 = self.dt * self.velocity2[i]
        k1v1 = self.dt * self.calculateAcceleration1(self.theta1[i],self.theta2[i],i)
        k1v2 = self.dt * self.calculateAcceleration2(self.theta1[i],self.theta2[i],i)
        k1E = self.calculateEnergy(i,k1theta1,k1theta2)

        k2theta1 = self.dt * (self.velocity1[i] + 0.5 * k1v1)
        k2theta2 = self.dt * (self.velocity2[i] + 0.5 * k1v2)
        k2v1 = self.dt * self.calculateAcceleration1((self.theta1[i] + 0.5 * k1theta1), (self.theta2[i]+0.5*k1theta2),i)
        k2v2 = self.dt * self.calculateAcceleration2((self.theta1[i] + 0.5 * k1theta1), (self.theta2[i]+0.5*k1theta2),i)
        k2E = self.calculateEnergy(i,k2theta1,k2theta2) + 0.5*k1E

        k3theta1 = self.dt * (self.velocity1[i] + 0.5 * k2v1)
        k3theta2 = self.dt * (self.velocity2[i] + 0.5 * k2v2)
        k3v1 = self.dt * self.calculateAcceleration1((self.theta1[i] + 0.5 * k2theta1), (self.theta2[i]+0.5*k2theta2),i)
        k3v2 = self.dt * self.calculateAcceleration2((self.theta1[i] + 0.5 * k2theta1), (self.theta2[i]+0.5*k2theta2),i)
        k3E = self.calculateEnergy(i,k3theta1,k3theta2) + 0.5*k2E

        k4theta1 = self.dt * (self.velocity1[i] + k3v1)
        k4theta2 = self.dt * (self.velocity2[i] + k3v2)
        k4v1 = self.dt * self.calculateAcceleration1((self.theta1[i] + k3theta1),(self.theta2[i]+k3theta2),i)
        k4v2 = self.dt * self.calculateAcceleration2((self.theta1[i] + k3theta1),(self.theta2[i]+k3theta2),i)
        k4E=self.calculateEnergy(i,k4theta1,k4theta2) + k3E

        #Increse step by calculating a weighted avergae
        self.theta1[i+1] = self.theta1[i] + (k1theta1 + 2 * k2theta1 + 2 * k3theta1 + k4theta1) / 6.0
        self.theta2[i+1] = self.theta2[i] + (k1theta2 + 2 * k2theta2 + 2 * k3theta2 + k4theta2) / 6.0
        self.velocity1[i+1] = self.velocity1[i] + (k1v1 + 2 * k2v1 + 2 * k3v1 + k4v1) / 6.0
        self.velocity2[i+1] = self.velocity2[i] + (k1v2 + 2 * k2v2 + 2 * k3v2 + k4v2) / 6.0
        
        self.Ek[i+1] = (k1E + 2 * k2E + 2 * k3E + k4E) / 6.0
        self.Ep[i+1]=-self.mass1*self.g*self.length1*np.cos(self.theta1[i+1])-self.mass2*self.g*(self.length1*np.cos(self.theta1[i+1])+self.length2*np.cos(self.theta2[i+1]))

        #Update the cartisain coordinates
        self.x1[i]=np.sin(self.theta1[i])*self.length1
        self.y1[i]=-np.cos(self.theta1[i])*self.length1
        self.x2[i]=self.x1[i]+(np.sin(self.theta2[i])*self.length2)
        self.y2[i]=(self.y1[i]-(np.cos(self.theta2[i])*self.length2))

        self.Et[i+1]=self.Ek[i+1]+self.Ep[i+1]