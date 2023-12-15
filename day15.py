# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:06:01 2023

@author: ap572e
"""

with open('day15_input.txt', 'r') as f:
    data = f.read()
    f.close()
    
def part1():
    answer = 0
    for step in data.split(','):
        a = 0
        for letter in step:
            a += ord(letter)
            a *= 17
            a = a % 256
        answer += a
            
    return answer
    
answer1 = part1()