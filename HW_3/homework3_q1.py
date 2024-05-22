import math
import numpy as np

def my_Bayes_candy(pi_list, p_list, c_list):
    posterior_probabilities = [[0] * 5 for _ in range(10)] # Default initialization with all zeros
    
    # Implement your code to calculate the posterior probabilities here
    past_p = pi_list[:]

    for i in range(10):
        for j in range(5):
            past_p[j] *= 1 - p_list[j] if c_list[i] else p_list[j]
            
        sum_p = sum(past_p)
        for j in range(5):
            posterior_probabilities[i][j] = past_p[j] / sum_p

    return posterior_probabilities

#test line