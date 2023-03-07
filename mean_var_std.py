import numpy as np
import math

def calculate(list):
    # sort list for reasons
    sorted_list = sorted(list)
    
    # can use numpy, but would like to exercise algorithms

    # Mean
    # (ps. research if faster way)
    total = 0
    for value in list:
        total += value
    mean = total / len(sorted_list)
    
    # Variance
    variance_list = [(x - mean)**2 for x in sorted_list]
    deviation_sum = sum(variance_list)
    variance = deviation_sum / len(sorted_list)


    # Standard Deviation
    std_dev = math.sqrt(variance)


    # NumPy solution
    array = np.array(sorted_list)
    # calculations = sorted_list
    

    return [mean, variance, std_dev]