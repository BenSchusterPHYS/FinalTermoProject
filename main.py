from Functions.initialize import initialize
from Functions.loop import loop
import numpy as np
import random

def main():
    size = 100

    # T values picked from Figure 8.9
    T = [10, 5, 4, 3, 2.5, 2, 1.5, 1]

    grid = initialize(size)
    
    for t in T:
        loop(size, grid, t, save = False)

if __name__ == "__main__":
    main()