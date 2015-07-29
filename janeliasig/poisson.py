def poisson(expected, trials):
    t = 0
    
    poisson_data = np.arange(0, trials, dtype = np.float)
    
    for i in range(1, int(trials) - 1):
        t += random.expovariate(expected)
        
        poisson_data[i] = t
        
    return poisson_data