import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c


class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = np.zeros(c.simulationLength)

    def Get_Value(self, t):

        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(
            self.linkName
        )

        # if t == len(self.values) - 1:
        #     print(self.values)

    def Save_Values(self):

        np.save(f"data/{self.linkName}_sensor_values.npy", self.values)
