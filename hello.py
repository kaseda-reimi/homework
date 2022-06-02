print("hello world")
import numpy as np


PROB_DIMEINTION = 3
BASICTOUR = [i for i in range(0,PROB_DIMEINTION)]

def mutation(offspring):
    allele1, allele2 = (np.random.choice(range(PROB_DIMEINTION),2, replace=False))
    print(allele1, allele2)
    offspring[allele1], offspring[allele2] = offspring[allele2], offspring[allele1]
    return offspring


if __name__ == "__main__":
    offspring = np.random.permutation(BASICTOUR)
    print(offspring)
    print(mutation(offspring))