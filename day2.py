#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 00:11:41 2023

@author: katyhagerty
"""

import re
import numpy as np

with open('day2_input.txt', 'r') as f:
    data = f.readlines()
    f.close()

class game:
    def __init__(self, line):
        self.number = int(re.search('Game (\d*)', line).group(1))
        line = line.replace("Game " + str(self.number) +": ",'')
        
        #list of sets
        sets = line.split(';')
        
        # list of dict of cubes in set
        a = []
        
        # create a dict of colors in each set
        for s in sets:
            d={}
            colors = s.split(',')
            for c in colors:
                d[c.split()[1]] = int(c.split()[0])
            a.append(d)
            
        self.sets = a
    
goal = {
        'red': 12, 
        'green': 13, 
        'blue': 14
        }

def part1(data):
    answer = 0
    for line in data:
        g = game(line)
        
        answer += g.number
        
        # Check each set in game
        # If it is impossible set to come from goal configuration, remove from total
        for s in g.sets:
            if s.get('red', 0) > goal['red'] or s.get('green', 0) > goal['green'] or s.get('blue', 0) > goal['blue']:
                answer -= g.number
                break
            
    return answer
                

def part2(data):
    answer = 0
    for line in data:
        g = game(line)
        
        d = {}        
        for s in g.sets:
            for c in s.keys():
                if s[c] > d.get(c,0):
                    d[c] = s[c]
                    
        answer += np.prod([i for i in d.values()])
    return answer

# answer = part1(data)
answer2 = part2(data)