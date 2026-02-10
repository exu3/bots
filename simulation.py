import pybullet as p
import time
import pybullet_data
import numpy as np

import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


# to disable sidebars:
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# read in a pyrosim world
p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate(robotId)
print(pyrosim.linkNamesToIndices)  # check link names are correct

time_range = 100
backLegSensorValues = np.zeros(time_range)
frontLegSensorValues = np.zeros(time_range)

for i in range(time_range):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")
    # print(backLegSensorValues[i])
    time.sleep(1/60)

p.disconnect()
print("backLegSensorValues", backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
print("frontLegSensorValues", frontLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
