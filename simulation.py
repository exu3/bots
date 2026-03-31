import pybullet as p
import pybullet_data
import time
from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):

        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        import pybullet_data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # 🔥 REQUIRED

        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        self.time_range = 1000

    def Run(self):
        for t in range(self.time_range):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            # Remove or reduce sleep for faster blind mode
            # time.sleep(1/2000)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
