def statistics(interval_data, variable = 1):
    
    stats_mean = np.average(interval_data)
    stats_variance = np.var(interval_data)
    stats_stderror = np.std(interval_data)/(len(interval_data)**0.5)
    
    if variable == 2:
        return round(stats_variance, 3)
    elif variable == 3:
        return round(stats_stderror, 3)
    else:
        return round(stats_mean, 3)