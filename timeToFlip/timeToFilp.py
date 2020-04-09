from runDoublePendulumSimulation import *
import matplotlib.pyplot as plt 
import numpy as np
from doublePendulum import *
import pickle
import pandas as pd 

p=np.sqrt(1/9.8)
colors=[]
a1=[]
a2=[]

for angle1 in np.arange(0,172,1):
    for angle2 in np.arange(-172,172,1):
        pendulum=doublePendulum(10,20,1,1,angle1,angle2,50,0.1)
        for i in range(pendulum.n-1):
            pendulum.calculateNextStepRK()
            if pendulum.theta2<np.radians(-180) or pendulum.theta2>np.radians(180) or pendulum.theta1<np.radians(-180) or pendulum.theta1>np.radians(180):
                if pendulum.t[i]<=10*p:
                    colors.append('darkviolet')
                    a1.append(angle1)
                    a2.append(angle2)
                    break
                elif pendulum.t[i]<=100*p and pendulum.t[i]>10*p:
                    colors.append('orangered')
                    a1.append(angle1)
                    a2.append(angle2)
                    break
                elif pendulum.t[i]<=1000*p and pendulum.t[i]>100*p:
                    colors.append('limegreen')
                    a1.append(angle1)
                    a2.append(angle2)
                    break
                else:
                    colors.append('black')
                    a1.append(angle1)
                    a2.append(angle2)
                    break
            if i == pendulum.n-1:
                colors.append('black')
                a1.append(angle1)
                a2.append(angle2)

print('here')
for j in range(len(a1)):
    plt.plot(a1[j],a2[j],',',color=colors[j])
plt.xlabel('Initial Angle 'r'$\theta_1$')
plt.ylabel('Initial Angle 'r'$\theta_2$')
plt.show()


save=[colors,a1,a2]
with open('timeToFlipData.pkl','wb') as output:
    pickle.dump(save, output, pickle.HIGHEST_PROTOCOL)





