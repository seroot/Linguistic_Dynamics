#!usr/bin/python

import Person
import World
import numpy as np
from Parameters import *


def main():
    # Instantiate a world
    New_World = World.World( Na, Nb, R, l, g, Uab, Uba)
    #New_World.plot_people()
    New_World.compute_neighbor_list()
    

    return


if __name__ == '__main__':main()

