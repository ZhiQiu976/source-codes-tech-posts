#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:08:16 2020

Euler problem 31, Coin sums
09/07/2020, solved by 83730

@author: heatherq
"""

import numpy as np

def compute(inputs, total):
    '''
    Function for solving Project Euler Problem 31. Dynamic programming.

    Parameters
    ----------
    inputs : list of int
        The original input value set.
    total : int
        The target total sum.

    Returns
    -------
    total_ways : int
        The number of combinations of the inputs that 
        could sum up to the target total.
        
    '''
    
	# At the beginning of each loop iteration,
    # ways[j] is the number of combinations of using the coin values before i
    # to form a sum of j
    
    # the list is updated within each loop
    # then get the final total number of ways to sum up to the target total
    # in the ways[total] cell
    
    # using Dynamic Programming algorithm
    
    ways = [1] + [0] * total
    for i in inputs:
        for j in range(1, total+1):
            if i <= j:
                ways[j] += ways[j-i]
    total_ways = ways[total]
    
    return total_ways



# get the answer for Euler problem 31
total = 200
inputs = [1, 2, 5, 10, 20, 50, 100, 200]
result = compute(inputs, total)
print('The total number of ways is {}'.format(result))






