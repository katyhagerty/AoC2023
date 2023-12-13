# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:07 2023

@author: ap572e
"""
import itertools

with open('day12_input.txt', 'r') as f:
    data = f.readlines()
    data = [i.strip() for i in data]
    # data = [[j for j in i] for i in data]
    f.close()
    
def solve(field,values, answer):

    
    if '?' not in field:
        result = [len(i) for i in field.split('.') if i != '']
        if result == values:
            # print(field)
            answer +=1

        return answer
    
    for i in ['.', '#']:

        x = field.find('?')
        field = field.replace('?', i, 1)

        answer = solve(field,values,answer)
        
        # undo
        field = field[0:x] + '?' + field[x+1:]
    
    return answer    

def part1():
    answers = []
    for line in data:
        field,values = line.split()
        values = values.split(',')
        values = [int(i) for i in values]
        answer = 0
        answers.append(solve(field,values,answer))
    
    return answers

answer1 = part1()