import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as r

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.disconnect

p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

backAmplitude = np.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = np.pi/5
frontFrequency = 10 
frontPhaseOffset = 0


pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
backTargetAngles = np.zeros(1000)
frontTargetAngles = np.zeros(1000)
x = np.linspace(-np.pi, np.pi, 1000)

for j in range(1000):
    backTargetAngles[j] = backAmplitude * np.sin(backFrequency * x[j] + backPhaseOffset)
    frontTargetAngles[j] = frontAmplitude * np.sin(frontFrequency * x[j] + frontPhaseOffset)

#np.save('data/backTargetAngles.npy', backTargetAngles)
#np.save('data/frontTargetAngles.npy', frontTargetAngles)



for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = "Torso_BackLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = backTargetAngles[i],
            maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = "Torso_FrontLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = frontTargetAngles[i],
            maxForce = 25)


    t.sleep(1/60)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
