def deltaU(i, j, grid, size):
    """
    Compute the energy change from flipping a spin using periodic boundary conditions
    """
    top    = grid[(i - 1) % size, j]
    bottom = grid[(i + 1) % size, j]
    left   = grid[i, (j - 1) % size]
    right  = grid[i, (j + 1) % size]

    return 2 * grid[i, j] * (top + bottom + left + right)