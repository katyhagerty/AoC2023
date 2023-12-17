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

def part2():
    answer = 0
    d= {}
    for step in data.split(','):
        box = 0
        
        if '-' in step:
            label, length = step.split('-')
            
            for letter in label:
                box += ord(letter)
                box *= 17
                box = box % 256
            
            if box in d.keys():
                labels = [i for i in d[box] if label in i]
                if len(labels) > 0:
                    d[box].remove(*labels)
            
        else:
            label, length = step.split('=')
            
            for letter in label:
                box += ord(letter)
                box *= 17
                box = box % 256
            
            if box in d.keys():
                labels = [i for i in d[box] if label in i]
                if len(labels) > 0:
                    old = labels[0]
                    new = f'{label} {length}'
                    ind = d[box].index(old)
                    d[box].pop(ind)
                    d[box].insert(ind,new)
                else:
                    d[box].append(f'{label} {length}')
            else:
                d[box] = [f'{label} {length}']
    
    for box in d.keys():
        for i,lens in enumerate(d[box]):
            label,length = lens.split()
            answer += (box + 1) * (i + 1) * int(length)
    
    return answer
answer2 = part2()