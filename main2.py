from Functions.initialize import initialize
from Functions.simulate import simulate
from Functions.animate import animate
from Functions.correlation import chart1, chart2
import numpy as np

#Designed to run continuously

def main():
    size = 100
    T = 2.27 #Tc is at 2.27
    time = 100 * size**2 #simulation cycles

    grid = initialize(size)
    sim = simulate(size, grid, T, time)

    #animate(sim) #gives you the animation

    chart1(sim, T) #uncomment to plot correlation function stuff
    #chart2(sim, T)




def aux(): #chiefly for 8.29 part c
    size = 100
    time = 100 * size**2

    T = [0.1, 0.5, 1, 1.5, 2, 2.27, 2.5, 3, 3.5, 4, 4.5, 5]
    length = np.zeros(len(T))

    for i in range(len(T)):
        grid = initialize(size)
        sim = simulate(size, grid, T[i], time)
        length[i] = chart2(sim,T[i],True)

    import matplotlib.pyplot as plt

    plt.scatter(T,length)
    plt.xlabel("T", fontsize=18)
    plt.ylabel("Correlation Length", fontsize=14)
    plt.show()


main()
#aux()