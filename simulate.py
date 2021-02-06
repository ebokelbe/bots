import pybullet as p
physicsClient = p.connect(p.GUI)
p.disconnect

for i in range(1000):
    p.stepSimulation()
