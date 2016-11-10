#!usr/bin/python

import numpy as np
import random
import math
import Parameters
import copy

class Person(object):
    """
        This class defines a person within a game theory simulation to describe the evolution of language
    """

    def __init__(self, language, position, index):
        # These variables are fed in during construction
        self.language = language #String
        self.position = position #Numpy 2D array
        self.index = index # integer
        
        # These variables must be computed
        self.utility = 0.0 # Float
        self.neighbor_list = [] # A list of inices
        if self.language == 'a':
            self.color = 'r'
        if self.language == 'b':
            self.color = 'b'
        return

    def move(self):
        # Generate random x and y
        x = Parameters.l*np.random.uniform(low=-1.0, high=1.0)
        y = math.sqrt( Parameters.l**2 - x**2)
        z = np.random.uniform(low=0.0, high = 1.0)
        
        if z < 0.5:
            y = -y
        
        new_position = copy.deepcopy(self.position)
        new_position[0] += x
        new_position[1] += y
        # Check to see if the new position is in the box
        logic = (new_position[0] < 1.0 and new_position[1] < 1.0 and new_position[0] > 0.0 and new_position[1] > 0.0)
        if logic:
            self.position = new_position

        return



