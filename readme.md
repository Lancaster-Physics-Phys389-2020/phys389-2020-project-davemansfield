# PENDULUM SIMULATOR

doublePendulum.py
--------------
This is the class for a double pendulum object. It stores its current velocity, postion and x and y for each bob.
It also contains the constants of the system which are the masses of the bobs, lengths of the arms, initial conditions and the time-step of the system. All of these inital conditons are defined by the user when they initalise a doublePendulum object.
As well as these it also has steps, which is again defined by the user which is used with the timestep to create an array called t which is the time in seconds. It also has n which is the total number of iterations that will run.

The methods are calculateAccerleration1 and calculateAcceleration2 which both take two arguments which are the corrected values of the angle needed to implemnet iterative methods.
There is calculateNextStepRk which updates the velocitys, angles and cartiesian coordinates of the bob using the Runge-Kutta method of intergration. And there is also calculateNextStepVerlet which does the same as calculateNextStepRK except it updates the values using the velocity verlet method of intergation. 
This script does not need to be alterd in anyway to run the simulation


runDoublePendulumSimulation.py
---------------------
This script is where the calculations are done and where the user defines their doublePendulum object, the intial conditons and the intergration method they want to use. All the data calculted is saved in lists into a pickle file under a unique file name that contains infromation about all the defining quntities of the system(masses, lengths, intital conditions, timestep and iterative method).
The lines the user should change to run this script are line 15, which is where they pick the inital conditions for their pendulum object and lines 19 and 20 where they only have to choose which line to comment out and which to keep. This picks the update method.
Once all these have been set, run the program and the data will be stored in a folder called pendulumData
This script should be used the user only wants to run one set of initial conditions. This is useful for getting a spercific set to veiw visually on the animation


changeInitialConditions.py
------------------
This script is used when the user wants to run multiple simulations at once i.e. with a range of intial condtions. They pick the range and the steps size. you can test multiple at once by using more for loops in excatly the same format or by adding a nested for loop with a differnet iterator. Note using a nested loop will test lots of values and may take a while to run.
Once the ranges and condions are set the program will run runDoublePendulumSimulation.py multiple times and save each as a seperate file. You can read multiple files into one dataFrame using createDataFrame.py


createDataFrame.py
------------------
This is where plots can be made. It reads data from one or more simulation data files in pendulumData and creates a dataframe using a module called pandas.

doublePendulumAnimation.py
------------------------
This file does not need to be changed much by the user. You can choose weather or not to have fading trails on the bobs. On line 60 change fileToRead to the name of the data file from runDoublePendulumSimulation you want to see animated.

createPlots.py
---------------
This module is not part of the working simulation it just shows some custom methods I made to run anaysis and give an idea of how the project can be used.

testModules
----------
These contain the pytest modules for the simulation. Note these must be moved to the same directory as the files they are testing for them to execute without error

simplePendulum
---------
contains three files, a prototype of a simple pendulum system an animation for it and a module to plot its angle. This isnt a final piece of work and is inlcuded to show where the actual simulation began.

timeToFlip
---------
contains the code and data used to produce the graph of how long it takes for a pendulum to flip. Note this graph takes alot of computuatinal power and time to run since it has to do so many calculations and independent simulations.