import pybullet as p
import os
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self, solutionID):

        # Load robot body
        self.robotId = p.loadURDF("body.urdf")

        # 🔥 Initialize sensors dictionary
        self.sensors = {}
        self.sensors[0] = SENSOR(linkName="Torso")
        self.sensors[1] = SENSOR(linkName="BackLeg")
        self.sensors[2] = SENSOR(linkName="FrontLeg")

        # 🔥 Initialize motors dictionary
        self.motors = {}
        self.motors[0] = MOTOR(jointName="Torso_BackLeg")
        self.motors[1] = MOTOR(jointName="Torso_FrontLeg")

        # 🔥 Load correct neural network file
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")

        # 🔥 Delete brain file after loading
        os.system(f"rm brain{solutionID}.nndf")  # Mac/Linux

    def Prepare_To_Sense(self):

        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):

        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):

        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode()].Set_Value(
                    self.robotId, desiredAngle)
                print(
                    f"{neuronName}: {self.nn.neurons[neuronName].Get_Value()} jointName: {jointName}, desiredAngle: {desiredAngle}")

    def Think(self):

        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        # Get link 0 state
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        # first tuple contains position
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]  # x position
        # Write to file
        with open("fitness.txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))
