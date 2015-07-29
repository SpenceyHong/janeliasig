def receiver_operating_curve(gold_standard_input, algorithm_standard_input, threshold_max = 5, threshold_interval = 0.15):
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