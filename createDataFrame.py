import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle

'''This script is where all plots can be made. It is done via a dataframe as this makes plotting very fast as once its created, you 
dont have to scim entire simulation data sets'''


def createDataFrameFunc(fileToRead):
    #this is the file containing all the simualtion data you want to put into a dataframe
    #reads data in
    with open('pendulumData/%s.pkl'% fileToRead,'rb') as input:
        pendulum=pickle.load(input)

    #d is a dictionary which sets the column title and the data from fileToRead
    #to select wwhich values are added to the dataframe simply comment out the ones you dont need
    d={'time':pendulum[0], 
    'theta1':pendulum[1],
    'theta2':pendulum[2], 
    'v1':pendulum[3],
    'v2':pendulum[4],
    'x1':pendulum[5],
    'x2':pendulum[6],
    'y1':pendulum[7],
    'y2':pendulum[8],
    #'Ek':pendulum[9],
    #'Ep':pendulum[10]
    }
    
    df=pd.DataFrame(d) #creates the dataframe

    dataFrameFile=fileToRead+str('-DF')
    with open('dataFrames/%s.pkl'% dataFrameFile,'wb') as output:
        pickle.dump(df, output, pickle.HIGHEST_PROTOCOL)


#an example of how to run this module and create a data frame
file='DPsim-L1-10-L2-10-M1-1-M2-1-T1-90-T2-5-timestep-0.004-method-verlet'
createDataFrameFunc(file)
