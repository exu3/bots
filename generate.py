import pyrosim.pyrosim as pyrosim

x = 0
y = 0
z = .5

length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name="Box", pos=[-2, -2, z], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # hook thing
    # pyrosim.Send_Cube(name="Link1", pos=[x, y, z], size=[
    #                   length, width, height])
    # pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2",
    #                    type="revolute", position=[0, 0, 1])
    # pyrosim.Send_Cube(name="Link2", pos=[0, 0, .5], size=[1, 1, 1])
    # pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3",
    #                    type="revolute", position=[0, 0, 1])
    # pyrosim.Send_Cube(name="Link3", pos=[0, 0, .5], size=[1, 1, 1])
    # pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4",
    #                    type="revolute", position=[0, .5, .5])
    # pyrosim.Send_Cube(name="Link4", pos=[0, .5, 0], size=[1, 1, 1])
    # pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5",
    #                    type="revolute", position=[0, 1, 0])
    # pyrosim.Send_Cube(name="Link5", pos=[0, .5, 0], size=[1, 1, 1])
    # pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6",
    #                    type="revolute", position=[0, .5, -.5])
    # pyrosim.Send_Cube(name="Link6", pos=[0, 0, -.5], size=[1, 1, 1])
    # pyrosim.Send_Joint(name="Link6_Link7", parent="Link6", child="Link7",
    #                    type="revolute", position=[0, 0, -1])
    # pyrosim.Send_Cube(name="Link7", pos=[0, 0, -.5], size=[1, 1, 1])

    # bot
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[
                      length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=[-.5, 0, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[
                      length, width, height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[
                      length, width, height])
    pyrosim.End()


Create_World()
Create_Robot()
