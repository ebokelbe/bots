import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

for i in range(6):
    x = i

    for j in range(6):
        y = j
        z = 0.5
        length = 1
        width = 1
        height = 1

        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
            z = z + height
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height

pyrosim.End()
