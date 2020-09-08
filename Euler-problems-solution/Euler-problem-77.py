#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:11:12 2020

Euler problem 77, Prime summations
09/07/2020, solved by 18309

@author: heatherq
"""

from eulerlib import primes
import itertools


def compute(threshold):
    '''
    The main function for finding the target number for Euler problem 77.
    Get the first value which can be written as the sum of primes in over
    the threshold number of different ways.

    Parameters
    ----------
    threshold : int
        The threshold number of ways.

    Returns
    -------
    sum_value : int
        The target sum of primes.

    '''
    
    # get the first item from an iterable that matches a condition
    sum_value = next(filter(lambda n: prime_ways(n) > threshold,
                            itertools.count(2)))
    # starts from 2, step = 1
    
    return sum_value




def prime_ways(n):
    '''
    Function to calculate how many different ways can an integer n 
    be written as the sum of primes.

    Parameters
    ----------
    n : int
        The number to be calculated with.

    Returns
    -------
    num_ways : int
        The total number of ways of different combinations.

    '''
    
    # get the primes before n (includes n)
    primes_set = primes(n)
    
    # dynamic programming
    ways = [1] + [0] * n
    for p in primes_set:
        for j in range(1, n+1):
            if p <= j:
                ways[j] += ways[j-p]
            
    num_ways = ways[n]
    
    return num_ways




threshold = 5000
result = compute(threshold)
print('The first value which can be written as the sum of primes in over 5000 different ways is {}'.format(result))





