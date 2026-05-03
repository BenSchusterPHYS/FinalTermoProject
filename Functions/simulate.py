#perform simulation over prescribed time and return 2+1d grid for analysis

def simulate(size, grid, T, time):
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    from Functions.deltaU import deltaU
    

    # Precompute Boltzmann factors for positive energies
    boltzmann = {
        4: np.exp(-4 / T),
        8: np.exp(-8 / T)
    }

    #initialize 2+1d array
    sim = []
    print("Simulating...")

    # Actual loop
    for k in range(time):

        i = random.randrange(size)
        j = random.randrange(size)

        dU = deltaU(i, j, grid, size)

        if dU <= 0:
            grid[i, j] *= -1
        elif dU == 4:
            if random.random() < boltzmann[4]:
                grid[i, j] *= -1
        elif dU == 8:
            if random.random() < boltzmann[8]:
                grid[i, j] *= -1

        if k % 1000 == 0: #don't need to save every step
            sim.append(grid.copy())
    
    print("Simulation Complete")

    sim = np.array(sim)
    return sim