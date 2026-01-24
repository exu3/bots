import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0
z = .5

length = 1
width = 1
height = 1

# pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
# pyrosim.Send_Cube(name="Box2", pos=[
#                   x + length, y, z + height], size=[length, width, height])

# nine towers, ohyeah
for row in range(3):
    for col in range(3):
        x = row
        y = col

        length = 1
        width = 1
        height = 1

        current_z = height / 2
        for i in range(10):
            pyrosim.Send_Cube(name=f"Box{row}{col}{i}",
                              pos=[x, y, current_z],
                              size=[length, width, height])

            current_z += height
            length *= 0.9
            width *= 0.9
            height *= 0.9

pyrosim.End()
