import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName

        self.Prepare_To_Act()

    def Prepare_To_Act(self):

        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        # make one motor half frequency
        if b"BackLeg" in self.jointName:
            self.frequency = self.frequency / 2

        time_range = 1000

        self.motorValues = self.amplitude * \
            np.sin(2 * np.pi * self.frequency *
                   np.arange(time_range) / time_range + self.offset)

    def Set_Value(self, robotId, desiredAngle):

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce
        )

    def Save_Values(self):

        np.save(f"data/{self.jointName}_motor_values.npy",
                self.motorValues)
