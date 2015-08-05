def mean_variance_graph(times_data):
    import numpy as np
    variance_data = []
    mean_data = []
    std_data = []
    for bin_count in range(50, 550, 50):
        events, edges = np.histogram(times_data,bins = bin_count)
        mean_data.append(np.mean(events))
        variance_data.append(np.std(events)**2)
        std_data.append(np.std(events)/float(len(events) ** 0.5))
    return mean_data, variance_data, std_data

def gaussian_kernel(sigma):
    from scipy import stats
    import numpy as np
    x = np.arange(-200, 201)
    kernel = []

    for i in x:
		kernel.append(stats.norm.pdf(i, 0, sigma))
    return kernel
def make_confusion_matrix(gold_standard_input, algorithm_standard_input, threshold_max = 5, threshold_interval = 0.15):
    from sklearn.metrics import confusion_matrix, matthews_corrcoef
    import numpy as np
    matrix_set = []
    matthews_coeff_set = []
   
    if len(gold_standard_input) > len(algorithm_standard_input):
        gold_standard_input = gold_standard_input[0:len(algorithm_standard_input)]
    elif len(gold_standard_input) < len(algorithm_standard_input):
        algorithm_standard_input = algorithm_standard_input[0:len(gold_standard_input)]

    for criterion in np.arange(0., threshold_max, threshold_interval):
    
        algorithm_standard_cm = threshold_algorithm(criterion, algorithm_standard_input)
        gold_standard_cm = threshold_algorithm(0, gold_standard_input)
        algorithm_full_data_cm = np.zeros(len(algorithm_standard_input))
        gold_full_data_cm = np.zeros(len(gold_standard_input))

        algorithm_full_data_cm[algorithm_standard_cm] = 1
        gold_full_data_cm[gold_standard_cm] = 1

        matrix = confusion_matrix(gold_full_data_cm, algorithm_full_data_cm)
        true_positive = float(matrix[0][0])
        false_positive = float(matrix[0][1])
        false_negative = float(matrix[1][0])
        true_negative = float(matrix[1][1])
    
        matthews_coeff_set.append(matthews_corrcoef(gold_full_data_cm, algorithm_full_data_cm))
        matrix_set.append(matrix)
    return matrix_set, matthews_coeff_set

def receiver_operating_curve(gold_standard_input, algorithm_standard_input, threshold_max = 5, threshold_interval = 0.15):
    import numpy as np

    if len(gold_standard_input) > len(algorithm_standard_input):
        gold_standard_input = gold_standard_input[0:len(algorithm_standard_input)]
    elif len(gold_standard_input) < len(algorithm_standard_input):
        algorithm_standard_input = algorithm_standard_input[0:len(gold_standard_input)]
    
    false_positive_set = []
    true_positive_set = []
    threshold_value_set = []
    global gold_full_data, algorithm_full_data
    
    for criterion in np.arange(0, threshold_max, threshold_interval):
        true_positive = 0.
        false_positive = 0.
        true_negative = 0.
        false_negative = 0.
        false_positive_rate = 0.
        true_positive_rate = 0.
        
        algorithm_standard = threshold_algorithm(criterion, algorithm_standard_input)
        algorithm_full_data = np.zeros(len(algorithm_standard_input))
        algorithm_full_data[algorithm_standard] = 1
        
        gold_standard = threshold_algorithm(0, gold_standard_input)
        gold_full_data = np.zeros(len(algorithm_standard_input))
        gold_full_data[gold_standard] = 1
        
        threshold_value_set.append(criterion)
        
        for index in range(0, len(gold_full_data)):
            if algorithm_full_data[index] == 1:
                if gold_full_data[index] == 1:
                    true_positive += 1.
                else:
                    false_positive += 1.
            elif algorithm_full_data[index] == 0.:
                if gold_full_data[index] == 0:
                    true_negative += 1
                else:
                    false_negative += 1.
        
        true_positive_rate = true_positive/sum(gold_full_data)
        false_positive_rate = false_positive/(len(gold_full_data) - sum(gold_full_data))
        
        #print true_positive, false_positive, true_negative, false_negative, true_positive_rate, false_positive_rate
    
        false_positive_set.append(false_positive_rate)
        true_positive_set.append(true_positive_rate)
    return false_positive_set, true_positive_set

def rsquared(x, y):
    import scipy as sp
    slope, intercept, r_value, p_value, std_err = sp.stats.linregress(x, y)
    return r_value ** 2
def statistics(interval_data, variable = 1):
    import numpy as np
    stats_mean = np.average(interval_data)
    stats_variance = np.var(interval_data)
    stats_stderror = np.std(interval_data)/(len(interval_data)**0.5)
    
    if variable == 2:
        return round(stats_variance, 3)
    elif variable == 3:
        return round(stats_stderror, 3)
    else:
        return round(stats_mean, 3)

def full_simulation(expected, trial, repetition = 1):
    import numpy as np

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
def poisson(expected, trials):
    import numpy as np
    import random
    t = 0
    
    poisson_data = np.arange(0, trials, dtype = np.float)
    
    for i in range(1, int(trials) - 1):
        t += random.expovariate(expected)
        
        poisson_data[i] = t
        
    return poisson_data
def poisson_interarrival(expected, trials):
    import numpy as np

    data = [np.random.poisson(expected) for i in range(trials)]
    return data
def load_raw_data(filename, num_elements = float("inf"), sourcedataformat = 'int8', target_dataformat = 'int8'):
    import os
    import math
    import numpy as np

    #dirinfo = dir(filename)
    file_size_bytes = os.path.getsize(filename)
   
    def doInt8(): 
        #bytesperelement = 1
        return 1
    def doInt16():
        #bytesperelement = 2
        return 2
    def doInt32():
        #bytesperelement = 4
        return 4
    def doInt64():
        #bytesperelement = 8
        return 8
    def error():
        print "Your input has not been recognized"
    formats = {
        'int8': doInt8(),
        'uint8': doInt8(),
        'int16': doInt16(),
        'uint16': doInt16(),
        'int32': doInt32(),
        'uint32': doInt32(),
        'int64': doInt64(),
        'uint64': doInt64()}
    
    bytes_per_element = formats.get(sourcedataformat, 'int8')
    
    num_file_elements = math.floor(file_size_bytes / bytes_per_element)
    
    num_elements = min(num_elements, num_file_elements)
    data = np.zeros(num_elements, target_dataformat)
    
    chunk_size_bytes = 50e6
    chunk_size_elements = chunk_size_bytes / bytes_per_element
    
    fileID = open(filename, 'rb')
    
    for iter in range(1, int(math.floor(num_elements/chunk_size_elements))):
         data[chunk_size_elements*(iter-1)+1: chunk_size_elements*iter] = np.fromfile(fileID, sourcedataformat, chunk_size_elements)
    
    remaining_elements = int(num_elements%chunk_size_elements)
    data[-1 - remaining_elements+1:-1] = np.fromfile(fileID, sourcedataformat, remaining_elements - 1)
   
    return data
    fileID.close()

def peakdet(data_array, threshold, x_axis = None):
    import numpy as np
    maxtab = []
    mintab = []
       
    if x_axis is None:
        x_axis = np.arange(len(data_array))
    
    data_array = np.asarray(data_array)
    
    if len(data_array) != len(x_axis):
        raise ValueError('Input vectors v and x must have same length')
    
    if not np.isscalar(threshold):
        raise ValueError('Input argument delta must be a scalar')
    
    if threshold < 0:
        raise ValueError('Input argument delta must be positive')
    
    mn, mx = np.Inf, -np.Inf
    mnpos, mxpos = np.NaN, np.NaN
    
    look_for_max = True
    
    for i in np.arange(len(data_array)):
        this = data_array[i]
        if this > mx:
            mx = this
            mxpos = x_axis[i]
        if this < mn:
            mn = this
            mnpos = x_axis[i]
        
        if look_for_max:
            if this < mx-threshold:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x_axis[i]
                look_for_max = False
        else:
            if this > mn+threshold:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x_axis[i]
                look_for_max = True
 
    return np.array(maxtab), np.array(mintab)

def threshold_algorithm(threshold_value, data):

    arrival_times = []
    peak_values = []
    maxtab, mintab = peakdet(data,threshold_value)
    
    for integer in range(0, len(maxtab)):
        arrival_times.append(maxtab[integer][0])
        peak_values.append(maxtab[integer][1])
    return arrival_times, peak_values

def threshold_histogram(data):
    import numpy as np

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
    
    temp_peak_times, temp_peak_values = threshold_algorithm(threshold_value,data)
   
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
