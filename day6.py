# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:03:55 2023

@author: ap572e
"""
import re

with open('day6_input.txt', 'r') as f:
    data = f.read()
    f.close()
    
def part1():
    answer = 1
    time = [int(i) for i in re.search('Time:\s+([\s|\d]+)', data).group(1).split()]
    dist = [int(i) for i in re.search('Distance:\s+([\s|\d]+)', data).group(1).split()]
    
    for record_t, d in zip(time,dist):
        times = range(1, record_t)
        winners = [i for i in times if i * (record_t - i) > d]
        answer *= len(winners)
        
    return answer
        
# answer1 = part1()

# part 1
# 10 min

def part2():
    time = int(''.join(re.search('Time:\s+([\s|\d]+)', data).group(1).split()))
    dist = int(''.join(re.search('Distance:\s+([\s|\d]+)', data).group(1).split()))
    
    times = range(1, time)
    winners = [i for i in times if i * (time - i) > dist]
    
    return len(winners)
    
answer2 = part2()