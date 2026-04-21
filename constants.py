import numpy as np

maxForce = 50

amplitude = np.pi / 4
frequency = 2
phaseOffset = 0

numberOfGenerations = 5
populationSize = 5

# for quadruped
# numSensorNeurons = 9
# numMotorNeurons = 8

# for da hexapod
# numSensorNeurons = 13
# numMotorNeurons = 12

motorJointRange = .3

simulationLength = 3000

robotType = "quadruped"  # or hexapod
