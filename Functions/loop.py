def loop(size, grid, T, save):
    import numpy as np
    import random
    from Functions.deltaU import deltaU
    from Functions.plot import plot

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

    print(f"Magnetization at temperature {T}:", np.sum(grid))

    plot(grid, T, save)