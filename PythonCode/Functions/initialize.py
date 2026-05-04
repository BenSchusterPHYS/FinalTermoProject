def initialize(size):
    import numpy as np
    """
    Initialize the Ising lattice with random spins.
    """
    return np.random.choice([-1, 1], size=(size, size))