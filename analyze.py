import numpy as np
import matplotlib.pyplot as plt

#backLegSensorValues = np.load('data/backLegSensorValues.npy')
#frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
targetAngles = np.load('data/targetAngles.npy')

#plt.plot(backLegSensorValues, linewidth=3, label='Back Leg')
#plt.plot(frontLegSensorValues, label='Front Leg')
plt.plot(targetAngles, label='Target Angles')
plt.legend()
plt.show()
