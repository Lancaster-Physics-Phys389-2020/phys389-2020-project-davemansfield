import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle
import random
import os

'''here i saved the code for some of the plots I made as an indiviual function and used, the code itself is not important but you can see how i 
have used the modules that make up the simualtion'''

def plot1():
    count=0
    timesRK=[]
    anglesRK=[]
    anglesVERLET=[]
    timesVERLET=[]
    #loops through multiple data frames in order to find the time at witch each run through became unstable comparing verlet and RK

    ##COLLECT TIME TO BECOME UNSTABLE FOR RK METHOD
    for test in range(45,55,1):
        time=0
        aRK=0
        dataFrameFile='DPsim-L1-10-L2-10-M1-1-M2-1-T1-10-T2-'+str(test)+'-timestep-0.01-method-RK-DF'
        with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
            df=pickle.load(input)
        
        for i, row in df.iterrows():
            if row['theta1']<0 and row['theta2']<0:
                if count==0:
                    time=row['time']
                    aRK=test
                count=count+1
                if count==3000:
                    anglesRK.append(aRK)
                    timesRK.append(time)
                    break
            else:
                count=0
                time=0
    
    ##COLLECT TIME TO BECOME UNSTABLE FOR VERLET METHOD
    count=0
    for test in range(45,55,1):
        time=0
        aV=0
        dataFrameFile='DPsim-L1-10-L2-10-M1-1-M2-1-T1-10-T2-'+str(test)+'-timestep-0.01-method-verlet-DF'
        with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
            df=pickle.load(input)
        
        for i, row in df.iterrows():
            if row['theta1']<0 and row['theta2']<0:
                if count==0:
                    time=row['time']
                    aV=test
                count=count+1
                if count==3000:
                    timesVERLET.append(time)
                    anglesVERLET.append(aV)
                    break
            else:
                count=0
                time=0


    #calculate avergae time
    #avRK=round(sum(timesRK)/len(timesRK),3)
    #avVERLET=round(sum(timesVERLET)/len(timesVERLET),3)

    print(timesRK)
    print(anglesRK)
    print()
    print(timesVERLET)
    print(anglesVERLET)
    
def plot2():
    #bar charts to show how fast simualtions became unstable
    RK001A1=[93.16, 38.05,0.0, 18.31, 68.0, 71.69,0.0, 20.69, 74.18, 110.45]
    RK0001A1=[0.0,24.59,0.0, 25.78,0, 19.23, 20.31, 11.87, 11.90, 11.93]
    RK0001A2=[15.937000000000001, 16.001, 16.065, 16.129, 16.194, 16.259, 16.325, 16.391000000000002, 16.458000000000002, 16.525]

    V001A1=[72.15, 31.38, 67.43, 71.77, 21.63, 134.13, 112.53,0.0, 19.17, 24.73]
    V0001A1=[0,38.91, 18.83, 24.80, 19.75, 24.31, 20.59, 39.98, 11.89, 11.92]
    V0001A2=[15.93, 15.993, 16.057, 16.121, 16.186, 16.251, 16.316, 16.382, 16.448, 16.515]

    A=[45,46,47,48,49,50,51,52,53,54]
    x=np.arange(len(A))
    width=0.35

    av001=round(sum(V001A1)/len(V001A1),2)
    av0001=round(sum(V0001A1)/len(V0001A1),2)

    fig,ax=plt.subplots()
    rects1=ax.bar(x-width/2,V001A1,width,color='purple',label='Timestep - 0.01')
    rects2=ax.bar(x+width/2,V0001A1,width,color='grey',label='Timestep - 0.001')
    ax.set_ylabel('Time Taken')
    ax.set_xlabel('Intial value of 'r'$\theta_1$')
    ax.set_xticks(x)
    ax.set_xticklabels(A)
    ax.plot([0,12],[av001,av001],color='purple',marker='_')
    ax.text(9,av001+1,'Average 0.01 = '+str(av001))
    ax.plot([0,12],[av0001,av0001],color='grey',marker='_')
    ax.text(10,av0001+1,'Average 0.001 = '+str(av0001))
    ax.legend()
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()

def plot3():
    tavRK=[14.97,15.78,13.40,16.37,12.22,5.62,9.32,8.74,8.31,7.41]
    tavV=[12.97,11.32,11.29,12.32,13.32,10.96,9.01,7.64,5.21,4.82]
    timesteps=[0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01]

    plt.plot(tavRK,timesteps,color='red',label='Runge-Kutta')
    plt.plot(tavV,timesteps,color='limegreen',label='Velocity Verlet')
    plt.xlabel('Average time for simulation to become unstable')
    plt.ylabel('Timestep')
    plt.legend()
    plt.show()


def plot4():
    dataFrameFile='DPsim-L1-10-L2-10-M1-1-M2-1-T1-90-T2-30-timestep-0.01-method-verlet-DF'
    with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
        df=pickle.load(input)

    df['Et']=df['Ek']-df['Ep']
    ax=df.plot(x='time',y=['Ek','Ep','Et'],label=['Total Energy','Potential Energy','Kinetic Energy'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Energy')
    ax.legend(loc='best')
    plt.show()



def plot5():
    dataFrameFile='DPsim-L1-10-L2-12-M1-1-M2-1-T1-50-T2-30-timestep-0.004-method-RK-DF'
    with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
        df=pickle.load(input)
    
    ax=df.plot(x='theta1',y='theta2')
    ax.set_xlabel('Theta1')
    ax.set_ylabel('Theta2')
    plt.show()

def plot6():
    dataFrameFile='DPsim-L1-10-L2-12-M1-1-M2-1-T1-50-T2-30-timestep-0.004-method-RK-DF'
    with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
        df1=pickle.load(input)

    dataFrameFile='DPsim-L1-10-L2-12-M1-1-M2-1-T1-50-T2-30-timestep-0.004-method-verlet-DF'
    with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
        df2=pickle.load(input)
    

    df1['v1x']=df1['v1']*np.cos(df1['theta1'])
    df1['v2x']=df1['v2']*np.cos(df1['theta2'])

    df2['v1x']=df2['v1']*np.cos(df2['theta1'])
    df2['v2x']=df2['v2']*np.cos(df2['theta2'])

    fig =plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(df1['x2'],df1['v2x'],label='Runge-Kutta')
    ax.plot(df2['x2'],df2['v2x'],label='verlet')
    ax.set_xlabel('X postion')
    ax.set_ylabel('Velocity in x direction')
    plt.legend()
    plt.show()


def plot7():
    dataFrameFile='DPsim-L1-10-L2-10-M1-1-M2-1-T1-90-T2-5-timestep-0.004-method-verlet-DF'
    with open('dataFrames/%s.pkl'% dataFrameFile,'rb') as input:
        df=pickle.load(input)

    df['v1x']=df['v1']*np.cos(df['theta1'])
    df['v2x']=df['v2']*np.cos(df['theta2'])


    fig =plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(df['x1'],df['v1x'],label='Bob 1',color='crimson')
    ax.plot(df['x2'],df['v2x'],label='Bob 2',color='mediumorchid')
    ax.set_xlabel('X postion')
    ax.set_ylabel('Velocity in x direction')
    plt.legend()
    plt.show()

plot7()