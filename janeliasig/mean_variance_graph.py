def mean_variance_graph(times_data):
    variance_data = []
    mean_data = []
    std_data = []
    for bin_count in range(50, 550, 50):
        events, edges = np.histogram(times_data,bins = bin_count)
        mean_data.append(np.mean(events))
        variance_data.append(np.std(events)**2)
        std_data.append(np.std(events)/float(len(events) ** 0.5))
    return mean_data, variance_data, std_data
    