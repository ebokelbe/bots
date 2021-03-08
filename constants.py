import numpy as np

backAmplitude = np.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = np.pi/5
frontFrequency = 10 
frontPhaseOffset = 0

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
backTargetAngles = np.zeros(1000)
frontTargetAngles = np.zeros(1000)
x = np.linspace(-np.pi, np.pi, 1000)