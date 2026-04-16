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
        # Hexapod
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Front left leg
        pyrosim.Send_Joint(name="Torso_FrontLeftLeg", parent="Torso", child="FrontLeftLeg",
                           type="revolute", position=[0.5, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[
                          0, 0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="FrontLeftLeg_FrontLeftLowerLeg", parent="FrontLeftLeg", child="FrontLeftLowerLeg",
                           type="revolute", position=[0, 1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # Front right leg
        pyrosim.Send_Joint(name="Torso_FrontRightLeg", parent="Torso", child="FrontRightLeg",
                           type="revolute", position=[0.5, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[
                          0, -0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="FrontRightLeg_FrontRightLowerLeg", parent="FrontRightLeg", child="FrontRightLowerLeg",
                           type="revolute", position=[0, -1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontRightLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # Middle left leg
        pyrosim.Send_Joint(name="Torso_MiddleLeftLeg", parent="Torso", child="MiddleLeftLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[
                          0, 0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="MiddleLeftLeg_MiddleLeftLowerLeg", parent="MiddleLeftLeg", child="MiddleLeftLowerLeg",
                           type="revolute", position=[0, 1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeftLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # Middle right leg
        pyrosim.Send_Joint(name="Torso_MiddleRightLeg", parent="Torso", child="MiddleRightLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleRightLeg", pos=[
                          0, -0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="MiddleRightLeg_MiddleRightLowerLeg", parent="MiddleRightLeg", child="MiddleRightLowerLeg",
                           type="revolute", position=[0, -1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleRightLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # Back left leg
        pyrosim.Send_Joint(name="Torso_BackLeftLeg", parent="Torso", child="BackLeftLeg",
                           type="revolute", position=[-0.5, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[
                          0, 0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="BackLeftLeg_BackLeftLowerLeg", parent="BackLeftLeg", child="BackLeftLowerLeg",
                           type="revolute", position=[0, 1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeftLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # Back right leg
        pyrosim.Send_Joint(name="Torso_BackRightLeg", parent="Torso", child="BackRightLeg",
                           type="revolute", position=[-0.5, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[
                          0, -0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="BackRightLeg_BackRightLowerLeg", parent="BackRightLeg", child="BackRightLowerLeg",
                           type="revolute", position=[0, -1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackRightLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.End()

    def Create_Body_Wahoo(self):
        # quadruped
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg",
                           type="revolute", position=[0, 1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg",
                           type="revolute", position=[0, -1.0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",
                           type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg",
                           type="revolute", position=[-1.0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",
                           type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg",
                           type="revolute", position=[1.0, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[
                          0, 0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        # sensor_links = [
        #     "Torso",
        #     "FrontLeg",
        #     "FrontLowerLeg",
        #     "BackLeg",
        #     "BackLowerLeg",
        #     "LeftLeg",
        #     "LeftLowerLeg",
        #     "RightLeg",
        #     "RightLowerLeg"
        # ]

        # motor_joints = [
        #     "Torso_FrontLeg",
        #     "FrontLeg_FrontLowerLeg",
        #     "Torso_BackLeg",
        #     "BackLeg_BackLowerLeg",
        #     "Torso_LeftLeg",
        #     "LeftLeg_LeftLowerLeg",
        #     "Torso_RightLeg",
        #     "RightLeg_RightLowerLeg"
        # ]
        sensor_links = [
            "Torso",
            "FrontLeftLeg", "FrontLeftLowerLeg",
            "FrontRightLeg", "FrontRightLowerLeg",
            "MiddleLeftLeg", "MiddleLeftLowerLeg",
            "MiddleRightLeg", "MiddleRightLowerLeg",
            "BackLeftLeg", "BackLeftLowerLeg",
            "BackRightLeg", "BackRightLowerLeg"
        ]

        motor_joints = [
            "Torso_FrontLeftLeg", "FrontLeftLeg_FrontLeftLowerLeg",
            "Torso_FrontRightLeg", "FrontRightLeg_FrontRightLowerLeg",
            "Torso_MiddleLeftLeg", "MiddleLeftLeg_MiddleLeftLowerLeg",
            "Torso_MiddleRightLeg", "MiddleRightLeg_MiddleRightLowerLeg",
            "Torso_BackLeftLeg", "BackLeftLeg_BackLeftLowerLeg",
            "Torso_BackRightLeg", "BackRightLeg_BackRightLowerLeg"
        ]

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

        cmd = f"python3 simulate.py {directOrGUI} {self.myID}"  # &
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
