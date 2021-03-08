import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r
import constants as c
from simulation import SIMULATION

# for j in range(1000):
#    backTargetAngles[j] = c.backAmplitude * np.sin(c.backFrequency * c.x[j] + c.backPhaseOffset)
#    frontTargetAngles[j] = c.frontAmplitude * np.sin(c.frontFrequency * c.x[j] + c.frontPhaseOffset)

#np.save('data/backTargetAngles.npy', backTargetAngles)
#np.save('data/frontTargetAngles.npy', frontTargetAngles)

# np.save('data/backLegSensorValues.npy', backLegSensorValues)
# np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

simulation = SIMULATION()
simulation.Run()