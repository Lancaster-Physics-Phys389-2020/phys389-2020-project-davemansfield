import matplotlib.pyplot as plt
import numpy as np
from simplePendulum import *

def main():
    testpen=Pendulum(12.0,3.0,90.0,10.0,0.001)
    for i in range(0,testpen.n-1):
        testpen.calculateNextStep(i)
    testpen.plot()

main()
