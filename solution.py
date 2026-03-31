import time
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random


class SOLUTION:

    def __init__(self, myID=0):
        self.myID = myID
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.fitness = None

    def Set_ID(self, myID):
        self.myID = myID

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

    def Start_Simulation(self, directOrGUI="DIRECT"):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        brainFile = f"brain{self.myID}.nndf"

        while not os.path.exists(brainFile):
            time.sleep(0.01)

        time.sleep(0.05)

        cmd = f"python3 simulate.py {directOrGUI} {self.myID} &"
        os.system(cmd)

    def Wait_For_Simulation_To_End(self):
        fitnessFile = os.path.abspath(f"fitness{self.myID}.txt")

        time.sleep(0.05)

        while not os.path.exists(fitnessFile):
            time.sleep(0.01)

        with open(fitnessFile, "r") as f:
            self.fitness = float(f.read())

        print(f"Solution {self.myID} fitness: {self.fitness:.4f}")

        os.remove(fitnessFile)

    def Evaluate(self, directOrGUI="DIRECT"):
        self.Start_Simulation(directOrGUI)
        self.Wait_For_Simulation_To_End()

    def Mutate(self):
        row = random.randint(0, 2)
        col = random.randint(0, 1)
        self.weights[row, col] = random.random() * 2 - 1
