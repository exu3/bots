import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)

        print(pyrosim.linkNamesToIndices)

        self.sensors = {}
        self.motors = {}
