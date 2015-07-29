def make_confusion_matrix(gold_standard_input, algorithm_standard_input, threshold_max = 5, threshold_interval = 0.15):
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