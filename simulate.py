import sys
from simulation import SIMULATION

if len(sys.argv) > 1:
    directOrGUI = sys.argv[1]
else:
    directOrGUI = "DIRECT"

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()
