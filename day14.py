# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 12:15:41 2023

@author: ap572e
"""
import re

with open('day14_input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    
def part1():
    # Transpose input data
    # Working with data will be easier in rows
    d = [list(i) for i in data]
    transposed = [list(i) for i in zip(*d)]
    
    # Reverse each line of data
    # Now the index in string cooresponds to distance from south edge
    transposed = [''.join(reversed(i)) for i in transposed]
    
    # Tilt the rocks
    splits = [list(i.split('#')) for i in transposed]
    tilted_positions = [[''.join(sorted(list(j))) for j in i] for i in splits]
    tilted_string = ['#'.join(i) for i in tilted_positions]
    
    # Add all the indices of the rocks
    ind_values = [j.span()[1] for i in tilted_string for j in re.finditer('O',i)]
    
    return sum(ind_values)

answer1 = part1()