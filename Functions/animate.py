#animate it

def animate(sim):
    import numpy as np
    import matplotlib.pyplot as plt

    # Initialize plot
    sim_img = np.where(sim == 1, 0, 255)

    #img_array = sim_img[0]
    im = plt.imshow(sim_img[0])
    plt.ion()
    plt.show()

    for t in range(len(sim)):
        #print(f"Magnetization at temperature {T}:", np.sum(grid)) #uncomment this to spam your terminal
        im.set_data(sim_img[t])
        plt.pause(0.01)

    plt.close('all')
    plt.ioff()