import numpy as np
import tsp

class RandomSearch:

    def __init__(self, N, MAX_EVALUATIONS, PROB_DIMEINTION):
        self.N  = N
        self.MAX_EVALUATIONS = MAX_EVALUATIONS
        self.PROB_DIMEINTION = PROB_DIMEINTION
        self.Xs = None #must be modified to "array" for population-based random search
        self.Fs = None #must be modified to "array" for population-based random search 
        self.BestX = None
        self.BestFX = None

    def generation(self):
        base_tour = [i for i in range(0,self.PROB_DIMEINTION)] #[0,1,2,...,50]
        
        #below must be modified to generate multiple, i.e. N, solutions for population-based random search
        self.Xs = np.random.permutation(base_tour) #Generate random tour from base_tour
        

    def evaluate(self, tsp):
        #below must be modified to evaluate multiple, i.e. N, solutions for population-based random search
        self.Fs = tsp.evaluate(self.Xs) #Get objectdive value of solution x

    def update(self):
         #below must be modified to check multiple, i.e. N, solutions for population-based random search
        if self.BestFX == None or self.Fs < self.BestFX: # update the current-best solution
            self.BestX  = self.Xs
            self.BestFX = self.Fs


if __name__ == "__main__":

    #Do not change
    N, MAX_EVALUATIONS, PROB_DIMEINTION = 1, 10000, 50 # N must be 1 for single-based random search 

    optimizer = RandomSearch(N, MAX_EVALUATIONS, PROB_DIMEINTION) 
    problem   = tsp.TSP(PROB_DIMEINTION)
    evals     = 0 #the number of evaluations executed
    log       = []
    #Run random search
    
    while evals < MAX_EVALUATIONS:
        optimizer.generation()
        optimizer.evaluate(problem)
        optimizer.update()
        evals += optimizer.N

        print(evals, optimizer.BestFX)
        log.append([evals, optimizer.BestFX])
    np.savetxt('_out.csv', log, delimiter=',') #then, see the "_out.csv"