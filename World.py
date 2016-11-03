#/usr/bin/python

import numpy as np
import math
import random
import Person
import matplotlib.pyplot as plt
import seaborn as sns

class World(object):
    """
        This class keeps tabs on all the people within the simulation, and applies various operations to compute their dynamics.
    """

    def __init__(self, Na, Nb, R, l, g, Uab, Uba):
        
        # Feed in parameters
        self.Na = Na
        self.Nb = Nb
        self.R = R
        self.l = l
        self.g = g
        self.Uab = Uab
        self.Uba = Uba

        self.Person_List = [] # list of people objects

        # Generate initial configuration
        index = 0
        # Initialize "a" people
        
        print "Initializing A people"
        for i in range(Na):
            Position = np.array([ 0.5*random.random(), random.random()], dtype = float)
            self.Person_List.append(Person.Person('a', Position, index))
            index += 1
        print "Initializing B people"
        # Initialize "b" people
        for i in range(Na):
            Position = np.array([ 1 - 0.5*random.random(), random.random()], dtype = float)
            self.Person_List.append(Person.Person('b', Position, index))
            index += 1
        return


    def plot_people(self):
        for Person in self.Person_List:
            plt.plot(Person.position[0], Person.position[1], color = Person.color, marker = 'o', markersize = 5)
        plt.show()
        return

    def diffuse(self):
        for Person in self.Person_List:
            Person.move()
        return

    def compute_neighbor_list(self):
        Hist = []
        for person1 in self.Person_List:
            #For each person, loop through every person and add every other person within a radius R to person 1's neighbor list
            for person2 in self.Person_List:
                dx = (person1.position[0]-person2.position[0])
                dy = person1.position[1] - person2.position[1]
                r = math.sqrt(dx**2+dy**2)
                if r<self.R and r!=0.0:
                    person1.neighbor_list.append(person2)
            Hist.append( len(person1.neighbor_list))
    
        plt.hist(Hist,50, normed =1)
        plt.xlabel('Length of Neighbor List')
        plt.ylabel('Probability')
        plt.show()
        return






