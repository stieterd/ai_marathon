import classes
import numpy as np
import json

sol_per_pop = 2000
results = classes.firstprogram(sol_per_pop)

fitness = np.sum(results, axis=1)
parentsid = fitness.argsort()[-2:][::-1]



generation_n = 1

while True:
    
    

    fitness = np.sum(results, axis=1)
    parentsid = fitness.argsort()[-2:][::-1]

    parents = (results[parentsid[0]], results[parentsid[1]])
    ga = classes.GA(parents)
    

    genes = (ga.crossover())

    results = []

    while len(results) < sol_per_pop//2:
            genex = np.copy(genes[0])
            
           
            results.append(ga.mutation(gene = genex, rate=10))
            

    while len(results) < sol_per_pop:
            geney = np.copy(genes[1])
            results.append(ga.mutation(gene = geney,rate = 10))

    new_population = np.array(results)
    if fitness[parentsid[0]] > 760:

        print('succeeded')
        break

    classes.generation(results, generation_n, sol_per_pop, fitness[parentsid[0]])

    generation_n +=1

    
    

