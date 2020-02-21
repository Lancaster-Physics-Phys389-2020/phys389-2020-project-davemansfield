import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy
import math

def draw():
    cirlce=plt.Cirlce((0,0), radius=0.75, fc='y')
    plt.gca().add_patch(circle)
    plt.axis('scaled')
    plt.show()

draw()