import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR
import os


class ROBOT:

    def __init__(self, solutionID=0):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{self.solutionID}.nndf")

        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system(f"rm brain{self.solutionID}.nndf")

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
                desiredAngle = self.nn.Get_Value_Of(
                    neuronName) * c.motorJointRange
                self.motors[jointName.encode()].Set_Value(
                    self.robotId, desiredAngle)

    def Think(self):

        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        xCoordinateOfLinkZero = stateOfLinkZero[0][0]

        # wh    at
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        # basePosition = basePositionAndOrientation[0]
        # xPosition = basePosition[0]

        tmpFile = f"tmp{self.solutionID}.txt"
        fitnessFile = f"fitness{self.solutionID}.txt"

        with open(tmpFile, "w") as f:
            f.write(str(xCoordinateOfLinkZero))

        os.rename(tmpFile, fitnessFile)
