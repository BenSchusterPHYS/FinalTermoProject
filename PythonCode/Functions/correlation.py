#correlation function for 8.29 - single frame

def cr(grid, r):
    import numpy as np
    
    size = grid.shape[0]

    si = np.mean(grid) # s_i bar, overall average spin

    csum = 0.0

    for i in range(size):
        for j in range(size):
            right = (i + r) % size
            down  = (j + r) % size

            csum += grid[i, j] * (
                grid[right, j] + grid[i, down]
            )

    sisj = csum / (2 * size * size) # s_i s_j bar, average spin product of pairs at distance r.
    
    return sisj - si**2

def cr_avg(sim, r): #time average over 50 frames from the last 1000
    import numpy as np

    frames = sim[-1000::20]

    corr = 0.0

    for grid in frames:
        corr += cr(grid, r)

    corr /= 50

    return corr

# bar chart of correlation function for given r

def chart1(sim, T): 
    import matplotlib.pyplot as plt
    import numpy as np

    grid = sim[-1]  # final state
    size = grid.shape[0]

    r = np.arange(1,int(size/2) + 1) #generates array of r based on size
    correlation = np.zeros(len(r))
    for i in r:
        correlation[i-1] = cr(grid,i)

    plt.figure()
    plt.bar(r,correlation)
    plt.title(f"T = {T}",fontsize=20)
    plt.xlabel("r", fontsize=18)
    plt.ylabel("c(r)", fontsize=18)
    plt.show()

# scatter log plot of correlation function for given r, can choose to return correlation length

def chart2(sim, T, vals=False, scatter=False):
    import matplotlib.pyplot as plt
    import numpy as np

    grid = sim[-1]  # final state
    size = grid.shape[0]

    r = np.arange(1,int(size/2) + 1) #generates array of r based on size
    correlation = np.zeros(len(r))
    for i in r:
        correlation[i-1] = cr_avg(sim,i)

    mask = correlation > 0
    r_fit = r[mask]
    C_fit = correlation[mask]

    m, b = np.polyfit(r_fit[:6], np.log(C_fit[:6]), 1) #need to create a fit line

    print(f"m = {m}")
    print(f"Correlation length is {-1/m}")

    if scatter == True: #can plot line if you want
        plt.figure()
        plt.scatter(r,np.log(np.abs(correlation)))
        x_fit = np.linspace(np.min(r), np.max(r), 100)
        y_fit = m * x_fit + b
        plt.plot(x_fit, y_fit, 'r')
        plt.title(f"T = {T}",fontsize=20)
        plt.xlabel("r", fontsize=18)
        plt.xlim(right=10)
        plt.ylabel("log c(r)", fontsize=18)
        plt.show()

    if vals == True:
        return -1/m
    else:
        return None
