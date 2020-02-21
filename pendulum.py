import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
import ffmpeg


class Pendulum():
    def __init__(self,length,mass,angle):
        self.length=length
        self.mass=mass
        self.angle=angle

    def calculateCoordiantes(angle,length):
        x=math.sin(angle)*length
        y=math.cos(angle)*length
        return x,y
    
    