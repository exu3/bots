import pybullet as p
import time
import pybullet_data


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


# to disable sidebars:
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# read in a pyrosim world
p.loadSDF("world.sdf")


for i in range(10000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()
