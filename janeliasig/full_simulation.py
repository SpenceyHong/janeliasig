def full_simulation(expected, trial, repetition = 1):
    full_data = []
    final_statistics = []
    
    for i in range(0, repetition):
        data = poisson_interarrival(expected, trial)
        
        full_data.append(data)
    
    statistics_x = statistics(full_data, 1)
    statistics_y = statistics(full_data, 2)
    statistics_z = statistics(full_data, 3)
    
    final_statistics.append(round(np.mean(statistics_x), 3))
    final_statistics.append(round(np.mean(statistics_y), 3))
    final_statistics.append(round(np.mean(statistics_z), 3))
    
    return final_statistics