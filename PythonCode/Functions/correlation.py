#correlation function for 8.29a

def cr(sim, r):
    import numpy as np
    
    grid = sim[-1]  # final state
    size = grid.shape[0]

    si = np.average(grid) # s_i bar, overall average spin

    prod = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            up = grid[(i-r) % size][j]
            down = grid[(i+r) % size][j]
            left = grid[i][(j-r) % size]
            right = grid[i][(j+r) % size]

            prod[i][j] = grid[i][j] * (up + down + left + right)

    sisj = np.average(prod)/2 # s_i s_j bar, average spin product of pairs at distance r. divide by 2 to account for doubling up
    
    return sisj - si**2

# bar chart of correlation function for given r

def chart1(sim, T): 
    import matplotlib.pyplot as plt
    import numpy as np

    grid = sim[-1]  # final state
    size = grid.shape[0]

    r = np.arange(1,int(size/2) + 1) #generates array of r based on size
    correlation = np.zeros(len(r))
    for i in r:
        correlation[i-1] = cr(sim,i)

    plt.figure()
    plt.bar(r,correlation)
    plt.title(f"T = {T}",fontsize=20)
    plt.xlabel("r", fontsize=18)
    plt.ylabel("c(r)", fontsize=18)
    plt.show()

# scatter log plot of correlation function for given r, can choose to return correlation length

def chart2(sim, T, vals=False): 
    import matplotlib.pyplot as plt
    import numpy as np

    grid = sim[-1]  # final state
    size = grid.shape[0]

    r = np.arange(1,int(size/2) + 1) #generates array of r based on size
    correlation = np.zeros(len(r))
    for i in r:
        correlation[i-1] = cr(sim,i)

    #plt.figure()
    #plt.scatter(r,np.log(np.abs(correlation)))

    m, b = np.polyfit(r[:10], np.log(np.abs(correlation[:10])), 1) #need to create a fit line
    #x_fit = np.linspace(np.min(r), np.max(r), 100)
    #y_fit = m * x_fit + b
    #plt.plot(x_fit, y_fit, 'r')

    print(f"m = {m}")
    print(f"Correlation length is {-1/m}")

    #plt.title(f"T = {T}",fontsize=20)
    #plt.xlabel("r", fontsize=18)
    #plt.xlim(right=10)
    #plt.ylabel("log c(r)", fontsize=18)
    #plt.show()

    if vals == True:
        return -1/m
    else:
        return None
