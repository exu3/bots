import numpy as np
import matplotlib.pyplot as plt

targetAngles = np.load("data/targetAngles.npy")

plt.plot(targetAngles)
plt.xlabel("time step")
plt.ylabel("radians")
plt.title("motor comamdns")
plt.show()
