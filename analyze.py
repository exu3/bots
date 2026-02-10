import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

print("backLegSensorValues", backLegSensorValues)

plt.plot(backLegSensorValues, linewidth=3)
plt.plot(frontLegSensorValues)
plt.xlabel("time step")
plt.ylabel("touch sensor value")
plt.title("Back/FrontLeg touch sensor values")
plt.legend(["BackLeg", "FrontLeg"])
plt.show()
