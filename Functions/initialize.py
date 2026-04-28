def initialize(size):
    import numpy as np
    '''
    Initialize the grid
    '''
    return np.random.choice([-1, 1], size=(size, size))