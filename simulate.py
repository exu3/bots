import sys
from simulation import SIMULATION

directOrGUI = sys.argv[1] if len(sys.argv) > 1 else "DIRECT"

solutionID = int(sys.argv[2]) if len(sys.argv) > 2 else 0

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
