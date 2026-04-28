from Functions.initialize import initialize
from Functions.deltaU import deltaU
from Functions.plot import plot
import numpy as np
import random

def main():
    size = 100
    T = 2.5

    grid = initialize(size)

    # Precompute Boltzmann factors for positive energies
    boltzmann = {
        4: np.exp(-4 / T),
        8: np.exp(-8 / T)
    }

    for k in range(100 * size**2):

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

    print("Magnetization:", np.sum(grid))

    plot(grid, size)


if __name__ == "__main__":
    main()