import pybullet as p
import time

physicsClient = p.connect(p.GUI)

# to disable sidebars:
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# read in a pyrosim world
p.loadSDF("box.sdf")


for i in range(10000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()
