from Functions.initialize import initialize
from Functions.simulate import simulate
from Functions.animate import animate
from Functions.correlation import chart1, chart2
import numpy as np
import matplotlib.pyplot as plt

def aux(): #chiefly for 8.29 part c
    size = 30
    time = 100 * size**2
    B = 0.0

    T = [2,2.1,2.2,2.25,2.3,2.4,2.5,2.6]
    length = np.zeros(len(T))

    for i in range(len(T)):
        grid = initialize(size)
        sim = simulate(size, grid, T[i], time, B)
        length[i] = chart2(sim,T[i],True)

    plt.scatter(T,length)
    plt.xlabel("T", fontsize=18)
    plt.ylabel("Correlation Length", fontsize=14)
    plt.show()

aux()