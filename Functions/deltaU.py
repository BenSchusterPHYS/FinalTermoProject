def deltaU(i, j, grid, size):
    '''
    Computes the change in energy of flipping a dipole. We compute the grid mod size to enforce the periodic boundary conditions.
    '''
    top    = grid[((i - 1) % size, j)]
    bottom = grid[((i + 1) % size, j)]
    left   = grid[(i, (j - 1) % size)]
    right  = grid[(i, (j + 1) % size)]

    return 2 * grid[(i, j)] * (top + bottom + left + right)