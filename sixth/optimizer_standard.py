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
        for i in range(self.N):
            if self.BestFX == None or self.Fs[i] < self.BestFX:
                self.BestX  = self.Xs[i]
                self.BestFX = self.Fs[i]

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
        for i in range(self.N):
            if self.BestFX == None or self.Fs[i] < self.BestFX:
                self.BestX  = self.Xs[i]
                self.BestFX = self.Fs[i]

    # generate next population
    def generation(self):
        nextXs = []
        for _ in range((int)(self.N/2)): 
            # parent selection
            parent1 = self.TournamentSelection()
            parent2 = self.TournamentSelection()

            #crossover
            offspring1, offspring2 = self.crossover(parent1, parent2)
            
            #mutation
            offspring1 = self.mutation(offspring1)
            offspring2 = self.mutation(offspring2)

            #add offspring to next population
            nextXs.append(offspring1)
            nextXs.append(offspring2)

        #update population
        self.Xs = nextXs

    # parent selection
    def TournamentSelection(self):
        competitor = np.random.choice(range(N),self.TS,replace=False)
        i = competitor[0]
        for x in competitor:
            if self.Fs[x] < self.Fs[i]:
                i = x
        return self.Xs[i]

    # crossover
    def crossover(self, parent1, parent2):
        # execute crossover with probability PC
        if np.random.rand() < self.PC:
            boundary = np.random.randint(1,self.PROB_DIMEINTION-1)
            offspring1 = [parent1[i] for i in range(boundary)]
            offspring2 = [parent2[i] for i in range(boundary)]
            _parent2 = [x for x in parent2 if x not in offspring1]
            _parent1 = [x for x in parent1 if x not in offspring2]
            offspring1 += _parent2
            offspring2 += _parent1

            return offspring1, offspring2

        # return copies of parents if crossover does not act
        else:
            offspring1 = [parent1[i] for i in range(self.PROB_DIMEINTION)]
            offspring2 = [parent2[i] for i in range(self.PROB_DIMEINTION)]
            return offspring1, offspring2

    def mutation(self, offspring):
        # execute mutation with probability PM
        if np.random.rand() < self.PM:
            allele1, allele2 = np.random.choice(range(self.PROB_DIMEINTION),2,replace=False)
            offspring[allele1], offspring[allele2] = offspring[allele2], offspring[allele1]
            return offspring
        else:
            return offspring

# Do not change
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
     