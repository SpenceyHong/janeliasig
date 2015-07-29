def poisson_interarrival(expected, trials):

    data = [np.random.poisson(expected) for i in range(trials)]
    return data