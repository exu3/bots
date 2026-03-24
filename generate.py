import pyrosim.pyrosim as pyrosim
import random

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


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

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


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    sensor_neurons = [0, 1, 2]
    for i in sensor_neurons:
        if i == 0:
            pyrosim.Send_Sensor_Neuron(name=i, linkName="Torso")
        elif i == 1:
            pyrosim.Send_Sensor_Neuron(name=i, linkName="BackLeg")
        elif i == 2:
            pyrosim.Send_Sensor_Neuron(name=i, linkName="FrontLeg")

    motor_neurons = [3, 4]
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    for i in sensor_neurons:
        for j in motor_neurons:
            weight = random.random() * 2 - 1  # [-1,1]
            pyrosim.Send_Synapse(
                sourceNeuronName=i,
                targetNeuronName=j,
                weight=weight
            )

    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
