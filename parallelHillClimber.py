from solution import SOLUTION
import constants as c


class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        self.nextAvailableID = 0   # NEW

        self.parents = {}

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        # Evaluate each parent (sequentially for now)
        for key in self.parents:
            self.parents[key].Evaluate(directOrGUI="GUI")

        # Commented out for now
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        pass

    def Show_Best(self):
        pass
