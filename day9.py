#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:14:46 2023

@author: katyhagerty
"""

import re

with open('day9_input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    
def part1():
    answer = 0
    for line in data:
        history = []
        line = line.split()
        line = [int(i) for i in line]
        history.append(line)
        
        # find differences between numbers at each level
        while set(line) != {0}:
            l = []
            for i in range(len(line) - 1):
                l.append(line[i + 1] - line[i])
            line = l
            history.append(l)
        
        # bottom-up approach to find prediction
        history_level = -2
        while history_level > len(history) * -1:
            prediction_step = history[history_level][-1]
            last_val = history[history_level - 1][-1]
            history[history_level - 1].append(prediction_step + last_val)
            history_level -= 1
        
        answer += last_val + prediction_step
        
    return answer
        
# part1 23 min, 10:38 AM
# answer1 = part1()

def part2():
    answer = 0
    for line in data:
        history = []
        line = line.split()
        line = [int(i) for i in line]
        history.append(line)
        
        # find differences between numbers at each level
        while set(line) != {0}:
            l = []
            for i in range(len(line) - 1):
                l.append(line[i + 1] - line[i])
            line = l
            history.append(l)
        
        # bottom-up approach to find prediction
        history_level = -1
        while history_level > len(history) * -1:
            prediction_step = history[history_level][0]
            first_val = history[history_level - 1][0]
            history[history_level - 1].insert(0, first_val - prediction_step)
            history_level -= 1
        
        answer += first_val - prediction_step
        
    return answer

# part 2, 13 min
answer2 = part2()