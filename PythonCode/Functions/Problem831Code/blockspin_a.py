def metropolis_step(grid, T):
    """
    Perform one Monte Carlo sweep using the Metropolis algorithm.
    """

    import numpy as np
    import random
    from Functions.deltaU import deltaU

    size = grid.shape[0]

    # Precompute Boltzmann factors
    boltzmann = {
        4: np.exp(-4 / T),
        8: np.exp(-8 / T)
    }

    for _ in range(size ** 2):
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


def block_transform(grid):
    """
    Apply a 3x3 block spin transformation using the majority rule.
    """

    import numpy as np

    size = grid.shape[0]

    if size % 3 != 0:
        raise ValueError("Grid size must be divisible by 3.")

    new_size = size // 3

    transformed = np.zeros((new_size, new_size), dtype=int)

    for i in range(new_size):
        for j in range(new_size):

            # I am actually so proud that this works it took so long to work out
            block = grid[3 * i:3 * i + 3, 3 * j:3 * j + 3]

            if np.sum(block) > 0:
                transformed[i, j] = 1
            else:
                transformed[i, j] = -1

    return transformed


def magnetization(grid):
    import numpy as np
    """
    Compute average magnetization per spin.
    """

    return np.sum(grid) / grid.size


def run_simulation(size, T, equilibration_sweeps=500, post_sweeps=500, skip=100):
    """
    Run the Ising model simulation and periodically display block transformations.
    equilibration_sweeps: number of steps to take before displaying images
    post_sweeps: number of steps to take after equilibrium has been reached
    skip: How many steps to skip before showing a new imag
    """

    from Functions.initialize import initialize
    from Functions.plot import compare_plots

    grid = initialize(size)

    print(f"\nRunning simulation at T = {T}")

    for _ in range(equilibration_sweeps):
        metropolis_step(grid, T)

    print("System equilibrated.")

    for sweep in range(post_sweeps):
        metropolis_step(grid, T)

        if sweep % skip == 0:
            transformed = block_transform(grid)

            M = magnetization(grid)

            print(f"Sweep {sweep}")
            print(f"Magnetization per spin = {M}")

            compare_plots(grid, transformed, T, sweep)

    return grid


def repeated_block_transformations(grid, levels=10):
    """
    Apply repeated block transformations
    until the lattice is too small (or transfomration is impossible).
    """

    import matplotlib.pyplot as plt
    lattices = [grid]

    current = grid.copy()

    for _ in range(levels):
        size = current.shape[0]

        if size < 3 or size % 3 != 0:
            break

        current = block_transform(current)
        lattices.append(current)

    # Honestly matplotlib is like black magic. I found this code on stackexchange years ago tbh but it works
    fig, ax = plt.subplots(1, len(lattices),figsize=(4 * len(lattices), 4))

    if len(lattices) == 1:
        ax = [ax]

    for i, lattice in enumerate(lattices):
        ax[i].imshow(lattice, cmap='gray', vmin=-1, vmax=1)

        ax[i].set_title(f"Level {i}\n{lattice.shape[0]}x{lattice.shape[0]}")

        ax[i].set_xticks([])
        ax[i].set_yticks([])

    plt.tight_layout()
    plt.show()
