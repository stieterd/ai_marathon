import numpy as np
import pygame
import random
import json


def generation(new_population, generation_n, popsize, fitness):

    


    screenspecs = (800,600)

    player = Player()

    pygame.init()

    white = [255, 255, 255]
    blue  = (0,0,255)
    red = (255,0,0)
    lime = (0,255,0)
    yellow = (255,215,0)
    orange = (255,165,0)
    turquasie = (0, 255,255)
    purple = (255,0,255)
    black = (0,0,0)
    magenta = (255,0,255)
    maroon = (128,0,0)
    olive = (128,128,0)
    green = (0,128,0)
    navy = (0,0,128)
    teal = (0,128,128)
    purple = (128,0,128)
    silver = (192,192,192)


    colors = [green, black, white, blue, lime, maroon, olive, red, magenta, yellow, orange, navy, teal, purple, silver]

    screen = pygame.display.set_mode(screenspecs)

    running = True

    clock=pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 30)



    #popsize = 10
    pop = []

    i = 0

    

    
    while i < popsize:


        pop.append([20,600-60, random.choice(colors[3:])]) #first x and second y
        i+=1

            

        
    n = 0

    while running:

        clock.tick(60)
        pressed = pygame.key.get_pressed()
        screen.fill((white))
        
        finishtext = font.render((f"Finish"), True, black)
        screen.blit(finishtext, (735, 520))
        
        genText = font2.render((f"Generation: {generation_n}"), True, red)
        screen.blit(genText, (20, 20))

        popText = font2.render((f"Popsize is: {popsize}"), True, red)
        screen.blit(popText, (20, 40))

        fitText = font2.render((f"Fitness is: {fitness}"), True, red)
        screen.blit(fitText, (600, 20))

        finish = pygame.draw.rect(screen, red, (800-30, 600 - 60, 20, 40))
        
        ground = pygame.draw.rect(screen, green, (0, 600-20, screenspecs[0], 30))
        
        i = 0
        try:
            while i < popsize:

                plrfill = screen.fill(pop[i][2], (pop[i][0], pop[i][1], player.sizex, player.sizey))
                plr = pygame.draw.rect(screen, black, (pop[i][0], pop[i][1], player.sizex, player.sizey), 1)
                direction = new_population[i][n]
                #direction = 1
                
                pop[i][0] = player.movement(pop[i][0], direction)
                i+=1
        except:
            
            pass
        

        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
        n+=1
        if n > 1200:
            break
        pygame.display.flip()


def firstprogram(popsize):
    
    screenspecs = (800,600)

    player = Player()

    pygame.init()

    white = [255, 255, 255]
    blue  = (0,0,255)
    red = (255,0,0)
    lime = (0,255,0)
    yellow = (255,215,0)
    orange = (255,165,0)
    turquasie = (0, 255,255)
    purple = (255,0,255)
    black = (0,0,0)
    magenta = (255,0,255)
    maroon = (128,0,0)
    olive = (128,128,0)
    green = (0,128,0)
    navy = (0,0,128)
    teal = (0,128,128)
    purple = (128,0,128)
    silver = (192,192,192)


    colors = [green, black, white, blue, lime, maroon, olive, red, magenta, yellow, orange, navy, teal, purple, silver]


    screen = pygame.display.set_mode(screenspecs)

    running = True

    clock=pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 30)



    #popsize = 10
    pop = []

    i = 0

    popdir = []

    while i < popsize:

        popdir.append([])
        i+=1

    i = 0
    while i < popsize:


        pop.append([20,600-60, random.choice(colors[3:])]) #first x and second y
        i+=1

            

        
    n = 0

    while running:

        clock.tick(60)
        pressed = pygame.key.get_pressed()
        screen.fill((white))
        
        finishtext = font.render((f"Finish"), True, black)
        screen.blit(finishtext, (735, 520))
        genText = font2.render((f"Generation: 0"), True, red)
        screen.blit(genText, (20, 20))
        popText = font2.render((f"Popsize is: {popsize}"), True, red)
        screen.blit(popText, (20, 40))

        fitText = font2.render((f"Fitness is: 0"), True, red)
        screen.blit(fitText, (600, 20))

        finish = pygame.draw.rect(screen, red, (800-30, 600 - 60, 20, 40))
        
        ground = pygame.draw.rect(screen, green, (0, 600-20, screenspecs[0], 30))
        
        i = 0
        while i < popsize:


            plrfill = screen.fill(pop[i][2], (pop[i][0], pop[i][1], player.sizex, player.sizey))
            plr = pygame.draw.rect(screen, black, (pop[i][0], pop[i][1], player.sizex, player.sizey), 1)
            
            
            direction = random.randint(-1,1)
            #direction = 1
            popdir[i].append(direction)
            pop[i][0] = player.movement(pop[i][0], direction)
            i+=1

        

        

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
        n+=1
        if n > 1200:
            break
        pygame.display.flip()

    np.array(popdir)
    
    return popdir


class Player:

    
    sizex = 20
    sizey = 40
    speed = 2
    

        

    def movement(self, x, direction):

        x += direction
        return x



class GA:

    def __init__(self, parents):

        
        self.parents = parents

    def crossover(self):

        parent1 = self.parents[0]
        parent2 = self.parents[1]
        
        parentlen = len(parent1)

        gene1 = np.concatenate((parent1[:parentlen-1], parent2[parentlen-1:]))
        gene2 = np.concatenate((parent2[:parentlen-1], parent1[parentlen-1:]))

        return gene1, gene2

    def mutation(self, gene, rate):
        
        
        for idx, x in enumerate(gene):

            if random.randint(0, rate) == rate:

                randomvalue = np.random.uniform(-4.0,4.0)
                
                gene[idx] = gene[idx] + randomvalue
                if gene[idx] > 6.0:

                    gene[idx] = 6.0

                if gene[idx] < -6.0:

                    gene[idx] = -6.0
        
        return gene

