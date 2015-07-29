def threshold_histogram(data):
    global c
    bin_count = 1
    temp_data = []
    while 0 not in temp_data:
        temp_data, x = np.histogram(data, bins = bin_count)
        bin_count += 1
    
    hist, bin_edges = np.histogram(data, bins = bin_count)
    
    total_count = sum(hist)
    temp_sum = 0
    threshold_value = 0
    
    for i in range(0, len(hist)):
        temp_sum += hist[i]
        if temp_sum >= total_count * 0.90 and bin_edges[i] > 0:
            threshold_value = i
            break
            
    threshold_value = bin_edges[threshold_value]
    
    temp_peak_times = threshold_algorithm(threshold_value,data)
    temp_peak_values = threshold_algorithm_1(threshold_value, data)
    peak_values = []
    peak_times = []
    reached_peakhigh = False
    #print temp_peak_times[0:200], temp_peak_values[0:200]
    #print "__________________________________________"
    for c in range(0, len(temp_peak_values)):
        if reached_peakhigh and temp_peak_values[c] < 1200:
            reached_peakhigh = False
            continue
        if temp_peak_values[c] < 2300:
            peak_values.append(temp_peak_values[c])
            peak_times.append(temp_peak_times[c])
        if temp_peak_values[c] >= 2500:
            reached_peakhigh = True
            

    final_peak_times = peak_times
    final_peak_values = []
    
    for peak in peak_values:
        final_peak_values.append(1)
    
    return final_peak_times                                                                
    '''
    ax = plt.figure().add_subplot(111)
    #ax.plot(data)
    ax.scatter(final_peak_times, final_peak_values)
    
    ax.set_xlim(0, 800)
    ax.set_xlim(-100, 2500)
    plt.show()
    '''