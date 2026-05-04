def deltaUB(i, j, grid, size, B=0):
    
    #add external field term with strength B, if not prescribed acts like normal

    top    = grid[((i - 1) % size, j)]
    bottom = grid[((i + 1) % size, j)]
    left   = grid[(i, (j - 1) % size)]
    right  = grid[(i, (j + 1) % size)]

    return 2 * grid[(i, j)] * (top + bottom + left + right + B)