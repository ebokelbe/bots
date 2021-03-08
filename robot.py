import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.sensors = {}
        self.motors = {}