import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
p.disconnect

for i in range(1000):
    p.stepSimulation()
    t.sleep(1/60)
