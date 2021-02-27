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

amplitude = np.pi/4
frequency = 10
phaseOffset = 0

pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
x = np.linspace(-np.pi, np.pi, 1000)
targetAngles = amplitude*(np.sin(frequency * x + phaseOffset))

#np.save('data/targetAngles.npy', targetAngles)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = "Torso_BackLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetAngles[i],
            maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = "Torso_FrontLeg",
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetAngles[i],
            maxForce = 25)


    t.sleep(1/60)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
