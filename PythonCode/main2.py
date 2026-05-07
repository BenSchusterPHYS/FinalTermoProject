from Functions.initialize import initialize
from Functions.simulate import simulate
from Functions.animate import animate
from Functions.correlation import chart1, chart2
import numpy as np

#Designed to run continuously

def main():
    size = 30
    T = 2 #Tc is at 2.27
    B = 0.0
    time = 100 * size**2 #simulation cycles

    grid = initialize(size)
    sim = simulate(size, grid, T, time, B)

    animate(sim) #gives you the animation

    #chart1(sim, T) #uncomment to plot correlation function stuff
    chart2(sim, T,scatter=True)

main()
