def threshold_algorithm(threshold_value, data):
    arrival_times = []
    peak_values []
    maxtab, mintab = peakdet(data,threshold_value)
    
    for integer in range(0, len(maxtab)):
        arrival_times.append(maxtab[integer][0])
        peak_values.append(maxtab[integer][1])
    return arrival_times, peak_values

