#perform simulation over prescribed time and return 2+1d grid for analysis
#can simulate external B field

def simulate(size, grid, T, time, B=0):
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    from Functions.deltaUB import deltaUB

    #initialize 2+1d array
    sim = []
    print("Simulating...")

    # Actual loop
    for k in range(time):

        i = random.randrange(size)
        j = random.randrange(size)

        dU = deltaUB(i, j, grid, size, B)

        if dU <= 0 or random.random() < np.exp(-dU / T):
            grid[i, j] *= -1

        if k % 1000 == 0: #don't need to save every step
            sim.append(grid.copy())
    
    print("Simulation Complete")

    sim = np.array(sim)
    return sim