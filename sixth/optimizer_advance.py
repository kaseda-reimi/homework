import numpy as np
import tsp

class RandomSearch:

    def __init__(self, N, MAX_EVALUATIONS, PROB_DIMEINTION):
        #RS settings
        self.N  = N

        #Problem settings
        self.MAX_EVALUATIONS = MAX_EVALUATIONS
        self.PROB_DIMEINTION = PROB_DIMEINTION
        
        #Private variables
        self.Xs = [None for _ in range(self.N)]
        self.Fs = [None for _ in range(self.N)]
        self.BestX = None
        self.BestFX = None
        self.BASICTOUR = [i for i in range(0,self.PROB_DIMEINTION)] #[0,1,2,...,50]

    def initialization(self):
        for i in range(self.N):            
            self.Xs[i] = np.random.permutation(self.BASICTOUR)

    def evaluate(self, tsp):
        for i in range(self.N):
            self.Fs[i] = tsp.evaluate(self.Xs[i])

    def update(self):
        _minID = np.argmin(self.Fs)
        if self.BestFX == None or self.Fs[_minID] < self.BestFX:
            self.BestX, self.BestFX  = self.Xs[_minID], self.Fs[_minID]

    def generation(self):
        self.initialization()

class GeneticAlgorithm:

    def __init__(self, N, CrossoverRate, MutationRate, TournamentSize, MAX_EVALUATIONS, PROB_DIMEINTION):
        # GA settings
        self.N  = N
        self.PC = CrossoverRate
        self.PM = MutationRate
        self.TS = TournamentSize

        #Problem settings
        self.MAX_EVALUATIONS = MAX_EVALUATIONS
        self.PROB_DIMEINTION = PROB_DIMEINTION

        #Private variables
        self.Xs        = [None for _ in range(self.N)]
        self.Fs        = [None for _ in range(self.N)]
        self.BestX     = None
        self.BestFX    = None
        self.BASICTOUR = [i for i in range(0,self.PROB_DIMEINTION)] #[0,1,2,...,50]

    def initialization(self):
        for i in range(self.N):            
            self.Xs[i] = np.random.permutation(self.BASICTOUR)

    def evaluate(self, tsp):
        for i in range(self.N):
            self.Fs[i] = tsp.evaluate(self.Xs[i])

    def update(self):
        _minID = np.argmin(self.Fs)
        if self.BestFX == None or self.Fs[_minID] < self.BestFX:
            self.BestX, self.BestFX  = self.Xs[_minID], self.Fs[_minID]

    def generation(self):
        nextXs = []
        for _ in range((int)(self.N/2)): 
            offspring1, offspring2 = self.crossover(self.tournamentSelection(), self.tournamentSelection())
            #offspring1, offspring2 = self.crossover(self.rouletteWheelSelection(), self.rouletteWheelSelection())
            nextXs.append(self.mutation(offspring1))
            nextXs.append(self.mutation(offspring2))
        self.Xs = nextXs

    def tournamentSelection(self):

        return self.Xs[i]

    def rouletteWheelSelection(self):

        return self.Xs[i]


    def crossover(self, parent1, parent2):

        return offspring1, offspring2

    def mutation(self, offspring):

        return offspring

def run(problem, optimizer, MAX_EVALUATIONS, filename):
    print("run {}".format(filename))

    evals = 0
    log   = []

    optimizer.initialization()
    optimizer.evaluate(problem)

    while evals < MAX_EVALUATIONS:
        optimizer.generation()
        optimizer.evaluate(problem)
        optimizer.update()
        evals += optimizer.N

        #logging
        print(evals, optimizer.BestFX)
        log.append([evals, optimizer.BestFX])
    np.savetxt('_out_{}.csv'.format(filename), log, delimiter=',') 

if __name__ == "__main__":
    #Basic setting (Do NOT change)
    N, MAX_EVALUATIONS, PROB_DIMEINTION = 100, 50000, 50
    TSP = tsp.TSP(PROB_DIMEINTION)
    
    #run Random search
    RS = RandomSearch(N, MAX_EVALUATIONS, PROB_DIMEINTION)
    run(TSP, RS, MAX_EVALUATIONS, "RS")

    #run Genetic algorithm
    CrossoverRate, MutationRate, TournamentSize = 1.0, 0.1, 10
    GA = GeneticAlgorithm(N, CrossoverRate, MutationRate, TournamentSize, MAX_EVALUATIONS, PROB_DIMEINTION)
    run(TSP, GA, MAX_EVALUATIONS, "GA")
     