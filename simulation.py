import pybullet as p
import time
import pybullet_data
import numpy as np
import random

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

time_range = 1000
backLegSensorValues = np.zeros(time_range)
frontLegSensorValues = np.zeros(time_range)

amplitude_fl = np.pi / 4
amplitude_bl = np.pi / 4

frequency_fl = 2
frequency_bl = 2

phaseOffset_fl = 0
phaseOffset_bl = np.pi / 2

# angles = np.linspace(0, 2 * np.pi, time_range)
# # get values in [-1, 1]
# targetAngles = np.sin(angles)
# # scale to [-pi/4, pi/4]
# targetAngles = targetAngles * (np.pi / 4)
targetAngles_fl = np.zeros(time_range)
targetAngles_bl = np.zeros(time_range)


for i in range(time_range):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    # targetAngles[i] = amplitude * np.sin(frequency * i + phaseOffset)
    targetAngles_fl[i] = amplitude_fl * \
        np.sin(2 * np.pi * frequency_fl * i / time_range + phaseOffset_fl)

    targetAngles_bl[i] = amplitude_bl * \
        np.sin(2 * np.pi * frequency_bl * i / time_range + phaseOffset_bl)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_bl[i],
        maxForce=50)  # Nm

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_fl[i],
        maxForce=50)  # Nm

    # print(backLegSensorValues[i])
    time.sleep(1/2000)  # 1/60

p.disconnect()
print("backLegSensorValues", backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
print("frontLegSensorValues", frontLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
np.save("data/targetAngles_fl.npy", targetAngles_fl)
np.save("data/targetAngles_bl.npy", targetAngles_bl)
