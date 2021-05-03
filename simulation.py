from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import time as t


class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        if self.directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGui == "GUI":
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        

    def Run(self):
        for i in range(1500):
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            if self.directOrGui == "GUI":
                t.sleep(1/60)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)

    def __del__(self):
        p.disconnect()
        
