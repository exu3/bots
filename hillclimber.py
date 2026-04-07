from solution import SOLUTION
import copy
import constants


class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()
        self.child = None

    def Evolve(self):
        # Evaluate initial parent
        self.parent.Evaluate(directOrGUI="DIRECT")

        # Loop over generations
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(directOrGUI="DIRECT")
        self.Print()  # optional, print fitness of parent and child
        self.Select()

    def Spawn(self):
        # Deepcopy parent → child
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        # Mutate the child
        self.child.Mutate()

    def Select(self):
        # Replace parent with child if child is better (higher fitness)
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print(
            f"Parent: {self.parent.fitness:.4f}, Child: {self.child.fitness:.4f}")

    def Show_Best(self):
        self.parent.Evaluate(directOrGUI="GUI")
