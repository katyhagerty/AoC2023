# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:05:11 2023

@author: ap572e
"""

import re

with open('day1_input.txt', 'r') as f:
    data = f.readlines()
    f.close()

def soln(data):
    total = 0        
    for line in data:
        first = re.search('\d', line).group(0)
        last = re.search('\d', line[::-1]).group(0)
        total += int(f'{first}{last}')
        
    return total

def part2(data):
    total = 0        
    d = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
        }
        
    for line in data:
        first = re.search(f'\d|{"|".join(d.keys())}', line).group(0)
        first = d.get(first, first)
        
        rev = [i[::-1] for i in d.keys()]
        last = re.search(f'\d|{"|".join(rev)}', line[::-1]).group(0)
        last = d.get(last[::-1], last)
        
        total += int(f'{first}{last}')
        
    return total

total =part2(data)

        