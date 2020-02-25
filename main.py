import matplotlib.pyplot as plt
import numpy as np
from simplePendulum import *
from animation import *
import pygame


#colours for pygame
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
black = pygame.Color(0,0,0)

SIZE=500,500
pygame.init()
screen=pygame.display.set_mode((SIZE))
screen.fill(white)
pygame.display.update()

#Pendulum(self,length,mass,initialAngle,steps,timestep)
testpen=Pendulum(50,3.0,90.0,10.0,0.001)

def main():
    running=True
    while running:
        for i in range(0,testpen.n-1):
            x = int(round(testpen.calculateXCoordiante(testpen.theta[i])))+250
            y = int(round(testpen.calculateYCoordinate(testpen.theta[i])))+250
            XY=(x,y)
            print(XY)
            pygame.draw.circle(screen,red,XY,1)
            pygame.display.update()
            testpen.calculateNextStep(i)
        running=False
        print('done')

main()