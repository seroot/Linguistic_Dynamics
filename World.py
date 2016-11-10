#/usr/bin/python

import numpy as np
import math
import random
import Person
import Parameters
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
        self.utility_list = []

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
        for i in range(Nb):
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
        Hist1 = []
        Hist2 = []
        for person1 in self.Person_List:
            #For each person, loop through every person and add every other person within a radius R to person 1's neighbor list
            index1 = 0
            index2 = 0
            for person2 in self.Person_List:
                dx = (person1.position[0]-person2.position[0])
                dy = person1.position[1] - person2.position[1]
                r = math.sqrt(dx**2+dy**2)
                if r<=self.R and r!=0.0:
                    person1.neighbor_list.append(person2)
                    if person1.language == person2.language or person1.language == 'c':
                        index1 += 1
                        person1.utility += Parameters.g
                    if person1.language != person2.language:
                        index2 += 1
        
            Hist.append(len(person1.neighbor_list))
            Hist1.append(index1)
            Hist2.append(index2)
            self.utility_list.append(person1.utility)
    
        self.utility_list = np.asarray(self.utility_list)
        plt.hist([Hist, Hist1, Hist2],20, normed =1, label = ["Total", "Can Communicate", "Cant Communicate"])
        plt.xlabel('Size of Neighbor List')
        plt.ylabel('Probability')
        plt.legend()
        plt.savefig('Neighbor_Dist.png')
        plt.clf()
        
        plt.hist(self.utility_list,20, normed =1)
        plt.xlabel('Utility')
        plt.ylabel('Probability')
        plt.legend()
        plt.savefig('Utility_Dist.png')
        return






