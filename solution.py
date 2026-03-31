import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random


class SOLUTION:

    def __init__(self, ID):
        self.myID = ID   # NEW
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.fitness = None

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2, -2, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[-.5, 0, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        sensor_links = ["Torso", "BackLeg", "FrontLeg"]
        motor_joints = ["Torso_BackLeg", "Torso_FrontLeg"]

        for i, linkName in enumerate(sensor_links):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=linkName)
        for j, jointName in enumerate(motor_joints):
            pyrosim.Send_Motor_Neuron(name=j+3, jointName=jointName)

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn+3,
                    weight=self.weights[currentRow][currentColumn]
                )
        pyrosim.End()

    def Evaluate(self, directOrGUI="DIRECT"):
        # Generate robot
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        # Run simulation in specified mode
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} &")
        # Read fitness
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Mutate(self):
        # Pick a random row (sensor neuron)
        randomRow = random.randint(0, 2)  # 0,1,2
        # Pick a random column (motor neuron)
        randomColumn = random.randint(0, 1)  # 0,1

        # Replace that synapse weight with a new random value in [-1,1]
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
