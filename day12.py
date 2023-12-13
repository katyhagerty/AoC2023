# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:07 2023

@author: ap572e
"""
import itertools

with open('day12_input.txt', 'r') as f:
    data = f.readlines()
    data = [i.strip() for i in data]
    # data = [[j for j in i] for i in data]
    f.close()
    
def part1():
    for line in data:
        field, values = line.split()
        no_springs = sum(values)
        known_springs = field.count('#')
        remaining_springs = no_springs - known_springs
        
        unknown = field.count('?')
        char = '#' * remaining_springs + '.' * unknown - remaining_springs
        patterns = list(set([''.join(i) for i in itertools.permutations(char, r = unknown)]))
        
    
answer1 = part1()