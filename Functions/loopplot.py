#this loop has the plotting integrated into the function

def loop(size, grid, T, time):
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    from Functions.deltaU import deltaU
    

    # Precompute Boltzmann factors for positive energies
    boltzmann = {
        4: np.exp(-4 / T),
        8: np.exp(-8 / T)
    }
    # Initialize plot
    img_array = np.where(grid == 1, 0, 255).astype(np.uint8)
    im = plt.imshow(img_array)
    plt.ion()
    plt.show()

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

        if k % 1000 == 0:
            #print(f"Magnetization at temperature {T}:", np.sum(grid)) #uncomment this to spam your terminal
            img_array = np.where(grid == 1, 0, 255)
            im.set_data(img_array)
            plt.pause(0.01)