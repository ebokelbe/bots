import pybullet_data
import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.disconnect

p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

for i in range(1000):
    p.stepSimulation()
    t.sleep(1/60)
