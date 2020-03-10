import matplotlib.pyplot as plt
import numpy as np
from doublePendulum import *
import pickle

    
def plotAvT(pendulumObject):
    #plots angle agaist time
    plt.plot(pendulumObject.t,pendulumObject.theta1,label='theta1',color='red')
    plt.plot(pendulumObject.t,pendulumObject.theta2,label='theta2',color='blue')
    plt.legend()
    plt.title('Double pendulum angles over time')
    plt.xlabel('Time, t')
    plt.ylabel('Angles, $\\theta$')
    plt.show()
    
def plotA1vA2(pendulumObject):
    #plots the angnle of each bob agaisnt one anouther
    plt.plot(pendulumObject.theta1,pendulumObject.theta2)
    plt.title('$\\theta_1$ vs $\\theta_2$')
    plt.xlabel('Theta 1, $\\theta_1$')
    plt.ylabel('theta 2, $\\theta_2$')
    plt.show()

def plotEkvT(pendulumObject):
    #plots the kinetic energy aginst time
    plt.plot(pendulumObject.t,pendulumObject.Ek) 
    plt.title('Kinetic energy over time')
    plt.xlabel('Time, t')
    plt.ylabel('Kinetic energy $E_k$')
    plt.show()
    
def plotEtvt(pendulumObject):
    plt.plot(pendulumObject.t,pendulumObject.Et)
    plt.show()


with open('pendulumData\pendulumFile.pkl','rb') as input:
    pendulum=pickle.load(input)
    plotAvT(pendulum)