# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:38:01 2023

@author: ap572e
"""

with open('day13_input.txt', 'r') as f:
    data = f.read()
    f.close()

def mirror(lines):
    # print(lines)
    # print('')
    for i in range(1, len(lines[0])):
        length = min(len(lines[0][0:i]), len(lines[0][i: 2 * i]))
        left = [line[i - length:i] for line in lines]
        left = ''.join(left)
        right = [line[i: i + length] for line in lines[::-1]]
        right = ''.join(right)                 
        if left == right[::-1]:
            return i
    return False
    
def part1():
    
    hor= []
    cols = []
    answer = 0
    patterns = data.split('\n\n')
    for pattern in patterns:
        lines = pattern.split('\n')
        # first_line = lines[0]
        col = mirror(lines)
        if col:
            # cols.append(col)
            answer += col
        else:
            transposed = [list(i) for i in zip(*lines)]
            transposed= [''.join(i) for i in transposed]
            h = mirror(transposed)
            # hor.append(h)
            answer += 100 * h

    # return cols,hor
    return answer
        
#part1
# 11:35 am
# 57 m    
# answer1= part1()

def mirror2(lines):
    # print(lines)
    # print('')
    for i in range(1, len(lines[0])):
        length = min(len(lines[0][0:i]), len(lines[0][i: 2 * i]))
        left = [line[i - length:i] for line in lines]
        left = ''.join(left)
        right = [line[i: i + length] for line in lines[::-1]]
        right = ''.join(right)                 
        
        difference = [i for i in zip(left, right[::-1]) if len(set(i)) != 1]
        
        # if difference = 1
        if len(difference) == 1:
            return i
    return False
    
# part2
# 16 m

def part2():
    hor= []
    cols = []
    answer = 0
    patterns = data.split('\n\n')
    for pattern in patterns:
        lines = pattern.split('\n')
        # first_line = lines[0]
        col = mirror2(lines)
        if col:
            # cols.append(col)
            answer += col
        else:
            transposed = [list(i) for i in zip(*lines)]
            transposed= [''.join(i) for i in transposed]
            h = mirror2(transposed)
            # hor.append(h)
            answer += 100 * h

    # return cols,hor
    return answer

answer2= part2()