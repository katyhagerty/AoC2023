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
    d = [list(i) for i in data]
    transposed = [list(i) for i in zip(*d)]
    transposed = [''.join(i) for i in transposed]
    transposed.reverse()
    
    splits = [list(i.split('#')) for i in transposed]
    tilted_positions = [sorted(i) for i in splits]
    tilted_string = [''.join() for i in tilted_positions]
    ind_values = [j.span()[1] for i in tilted_string for j in re.findall('O',i)]
    
    return sum(ind_values)
    # for i in tilted_string:
    #     for j in re.findall('O', i):
    #         j.span()[1]
                     
    # for sent in text:
    #     for word in sent:
    #         word
answer1 = part1()