import pybullet as p
import constants as c
import time
import pybullet_data
import numpy as np
import random

import pyrosim.pyrosim as pyrosim
from simulation import SIMULATION

simulation = SIMULATION()

time_range = 1000
backLegSensorValues = np.zeros(time_range)
frontLegSensorValues = np.zeros(time_range)

targetAngles_fl = np.zeros(time_range)
targetAngles_bl = np.zeros(time_range)


for i in range(time_range):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    targetAngles_fl[i] = c.amplitude_fl * \
        np.sin(2 * np.pi * c.frequency_fl * i / time_range + c.phaseOffset_fl)

    targetAngles_bl[i] = c.amplitude_bl * \
        np.sin(2 * np.pi * c.frequency_bl * i / time_range + c.phaseOffset_bl)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_bl[i],
        maxForce=c.maxForce)  # Nm

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles_fl[i],
        maxForce=c.maxForce)  # Nm

    # print(backLegSensorValues[i])
    time.sleep(1/2000)  # 1/60

p.disconnect()
print("backLegSensorValues", backLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)
print("frontLegSensorValues", frontLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
np.save("data/targetAngles_fl.npy", targetAngles_fl)
np.save("data/targetAngles_bl.npy", targetAngles_bl)
