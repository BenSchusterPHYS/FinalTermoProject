from Functions.initialize import initialize
from Functions.loopplot import loop
import numpy as np
import random

#Designed to run continuously

def main():
    size = 100
    T = 10
    time = 100 * size**2 #simulation cycles

    grid = initialize(size)
    
    loop(size, grid, T, time)    

main()