from robot import ROBOT
from world import WORLD

import pybullet as p
import pybullet_data


class SIMULATION:
    def __init__(self):

        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # to disable sidebars:
        # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()
