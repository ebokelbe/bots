import numpy as np
import matplotlib.pyplot as plt

#backLegSensorValues = np.load('data/backLegSensorValues.npy')
#frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
backTargetAngles = np.load('data/backTargetAngles.npy')
frontTargetAngles = np.load('data/frontTargetAngles.npy')

#plt.plot(backLegSensorValues, linewidth=3, label='Back Leg')
#plt.plot(frontLegSensorValues, label='Front Leg')
plt.plot(backTargetAngles, lw=3, label='Back Target Angles')
plt.plot(frontTargetAngles, label='Front Target Angles')
plt.legend()
plt.show()
