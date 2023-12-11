#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 08:36:31 2023

@author: katyhagerty
"""

import re
import numpy as np

with open('day8_input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    
def part1():
    
    # turn directions string in numbers 
    # L = 0
    # R = 1
    directions = data[0].strip()
    directions = directions.replace('L', '0')
    directions = directions.replace('R', '1')
    
    # create dictionary of nodes
    m = {}
    for line in data[2:]:
        m[re.search('(\w*) =', line).group(1)] = re.search('.* = \((.*)\)', line).group(1).split(', ')
    
    node = 'AAA'
    i = 0
    answer = 0
    while node != 'ZZZ':
        
        position  = int(directions[i])
        node = m[node][position]
        if i + 1 < len(directions):
            i += 1
        else:
            i = 0
        
        answer += 1
    
    return answer
        
# part1 20 min
# answer1 = part1()

def ends_not_Z(nodes):
    for node in nodes:
        if not node.endswith('Z'):
            return True
    
    return False

def part2():
    
    # turn directions string in numbers 
    # L = 0
    # R = 1
    directions = data[0].strip()
    directions = directions.replace('L', '0')
    directions = directions.replace('R', '1')
    
    # create dictionary of nodes
    m = {}
    for line in data[2:]:
        m[re.search('(\w*) =', line).group(1)] = re.search('.* = \((.*)\)', line).group(1).split(', ')
    
    nodes = [i for i in m.keys() if i.endswith('A')]
    answer = []
    i = 0
    
    for node in nodes:
        a = ''
        while node != node[0:2] + 'Z':
            
            position  = int(directions[i])
            node = m[node][position]
            if i + 1 < len(directions):
                i += 1
            else:
                i = 0
                
            a += directions[i]
            
        answer.append(a)
            
    return np.lcm.reduce([len(i) for i in answer])

# part2 30 min
answer2 = part2()