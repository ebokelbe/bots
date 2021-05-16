from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.fitnessMatrix = np.zeros((c.populationSize, c.numberOfGenerations))  # creates a p x g matrix of zeros
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, generation):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.UpdateFitnessMatrix(self.parents, generation)

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n")
        for i in self.parents:
            print("( " + str(self.parents[i].fitness) + ", " + str(self.children[i].fitness) + " )")
        print("\n")

    def Show_Best(self):
        best = 1.0
        for i in self.parents:
            if self.parents[i].fitness < best:
                best = self.parents[i].fitness
                best_key = i
        self.parents[best_key].Start_Simulation("GUI")

        # self.parent.Evaluate("GUI")
    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def UpdateFitnessMatrix(self, solutions, generation):
        for solution in solutions:
            self.fitnessMatrix[solution, generation] = solutions[solution].fitness  # add fitness value to matrix
    
    def SaveFitnessMatrix(self):
        np.save('fitnessValues.npy', self.fitnessMatrix, delimiter=',')