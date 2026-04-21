from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm tmp*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessHistory = []

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT")
        self.Record_Best_Fitness()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.Record_Best_Fitness()

        self.Save_Fitness_History()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, "DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            print("Parent fitness:", self.parents[key].fitness,
                  "Child fitness:", self.children[key].fitness)
        print()

    def Show_Best(self):
        bestKey = 0
        for key in self.parents:
            if self.parents[key].fitness < self.parents[bestKey].fitness:
                bestKey = key

        self.parents[bestKey].Start_Simulation("GUI")

    def Evaluate(self, solutions, directOrGUI):
        for key in solutions:
            solutions[key].Start_Simulation(directOrGUI)

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def Record_Best_Fitness(self):
        bestFitness = min(self.parents[key].fitness for key in self.parents)
        self.fitnessHistory.append(bestFitness)

    def Save_Fitness_History(self):
        filename = f"fitness_history_{c.robotType}.txt"
        with open(filename, "w") as f:
            for generation, fitness in enumerate(self.fitnessHistory):
                f.write(f"{generation} {fitness}\n")
