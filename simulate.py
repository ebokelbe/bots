import pybullet_data
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.disconnect

p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    t.sleep(1/60)
