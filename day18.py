# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:07:41 2023

@author: ap572e
"""
import numpy as np

with open('day18_input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    
def part1():
    corners = []
    i,j = (0,0)
    for line in data:
        direction, length, color = line.split()
        length = int(length)
        
        if direction == 'R':
            j += length
        elif direction == 'L':
            j -= length
        elif direction == 'U':
            i -= length
        else:
            i += length
        
        corners.append((i,j))
    
    return corners
    
answer1 = part1()