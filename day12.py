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

# answer1 = part1()

def positions(field):
    return [i for i,v in enumerate(field) if v == '?']

def chars(field,values):
    springs = sum(values)
    not_springs = len(field) - springs
    remainder = springs - field.count('#')
    dots_need = not_springs - field.count('.')
    
    if remainder == field.count('?'):
        return ['#']
    elif remainder == 0:
        return ['.']
    else:
        return ['.', '#']
    
def solve2(field,values, answer):    
    if '?' not in field:
        result = [len(i) for i in field.split('.') if i != '']
        if result == values:
            print(field)
            answer +=1

        return answer
    
    c = chars(field,values)
    for i in c:

        x = field.find('?')
        field = field.replace('?', i, 1)

        answer = solve2(field,values,answer)
        
        # undo
        field = field[0:x] + '?' + field[x+1:]
    
    return answer 

def part2():
    answers = []
    for line in data:
        field,values = line.split()
        values = values.split(',')
        values = [int(i) for i in values]
        # field *= 5
        # values *= 5
        answer = 0
        answers.append(solve2(field,values,answer))
    
    return answers

answer2 = part2()