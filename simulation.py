from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import time as t


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.disconnect
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robot,
                jointName = "Torso_BackLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = c.backTargetAngles[i],
                maxForce = 25)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robot,
                jointName = "Torso_FrontLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = c.frontTargetAngles[i],
                maxForce = 25)

            t.sleep(1/60)