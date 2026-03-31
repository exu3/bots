import time
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import constants as c


class SOLUTION:

    def __init__(self, myID=0):
        self.myID = myID
        self.weights = np.random.rand(
            c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.fitness = None

    def Set_ID(self, myID):
        self.myID = myID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2, -2, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",
                           type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",
                           type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        sensor_links = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg"]
        motor_joints = ["Torso_BackLeg", "Torso_FrontLeg",
                        "Torso_LeftLeg", "Torso_RightLeg"]

        for i, linkName in enumerate(sensor_links):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=linkName)

        for j, jointName in enumerate(motor_joints):
            pyrosim.Send_Motor_Neuron(
                name=j + c.numSensorNeurons, jointName=jointName)

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn + c.numSensorNeurons,
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
        row = random.randint(0, c.numSensorNeurons - 1)
        col = random.randint(0, c.numMotorNeurons - 1)
        self.weights[row, col] = random.random() * 2 - 1
