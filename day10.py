#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:52:09 2023

@author: katyhagerty
"""

import re
import numpy as np

with open('day10_input.txt', 'r') as f:
    data = f.readlines()
    f.close()


# traveling north, south, east, west
# pipes = {
#     '|': [(-1, 0), (1, 0), (), ()], 
#     '-': [(), (), (0, 1), (0, -1)], 
#     'L': [(), (1,1), (), (-1, -1)],
#     'J': [(), (1, -1), (-1, 1), ()], 
#     '7': [(-1, -1), (), (1, 1), ()],
#     'F': [(-1, 1), (), (), (1, -1)],
#     'S': [(), (), (), ()]
#     }

pipes = {
    '|': [(-1, 0), (1, 0), (), ()], 
    '-': [(), (), (0, 1), (0, -1)], 
    'L': [(), (0, 1), (), (-1, 0)],
    'J': [(), (0, -1), (-1, 0), ()], 
    '7': [(0, -1), (), (1, 0), ()],
    'F': [(0, 1), (), (), (1, 0)],
    'S': [(), (), (), ()]
    }

def find_start(data):
    for i, line in enumerate(data):
        if 'S' in line:
            j = line.find('S')
            return (i,j)

def find_connections(start):
    # north, south, east, west
    x, y = start
    connections = []
    directions = []
    for direction, coords in enumerate([(-1, 0), (1, 0), (0, 1), (0, -1)]):
        i,j = coords
        if 0 <= x + i < len(data) and 0 <= y + j < len(data[0].strip()):
            if data[x + i][y + j] != '.':
                if pipes[data[x + i][y + j]][direction] != ():
                    pipes_coord = pipes[data[x + i][y + j]][direction]
                    connections.append(pipes_coord)
                    directions.append(direction)
                
    connections = [(x + i, y + j) for i,j in connections]
    answer = zip(directions, connections)
    
    # each start point has two paths
    # just need one path
    return next(answer)

def find_next(direction, start):
    x, y = start
    current_pipe = data[x][y]
    i, j = pipes[current_pipe][direction]
    if 0 <= x + i < len(data) and 0 <= y + j < len(data[0]):
        next_pipe = data[x + i][y + j]
    else:
        return []
    
    if next_pipe == '.':
        return []
    
    if i == -1:
        new_direction = 0 # north
    elif i == 1:
        new_direction = 1 # south
    
    if j == 1:
        new_direction = 2 # east
    elif j == -1:
        new_direction = 3 # west
    
    return new_direction, (x + i, y + j)
    

def part1():
    start = find_start(data)
    direction, connection = find_connections(start)

    # already took one step from start to first point
    steps_in_loop = 1
    
    while connection != start:
        direction, connection = find_next(direction, connection)
        steps_in_loop += 1 
        # if connection == []:
            # break
    
    return steps_in_loop / 2

# part1 , 2 h
# answer1 = part1()

def transform_data():
    start = find_start(data)
    direction, connection = find_connections(start)
    mask = np.zeros((len(data), len(data[0].strip())))
    mask[start[0], start[1]] = 1
    
    while connection != start:
        x, y = connection
        direction, connection = find_next(direction, connection)
        mask[x][y] = 1
    
    for ind, line in enumerate(data):
        data[ind] = ''.join([j if mask[ind][i] else '.' for i,j in enumerate(line.strip()) ])
        
    
    return data

# 4:48
def part2():
    answer = 0
    new_data = transform_data()
    copy = new_data.copy()
    
    for line_no, line in enumerate(new_data):
        # test = line
        for ind, square in enumerate(line):
            if square == '.':
                left_walls = len(re.findall('[\|\-LFJ7]', line[0:ind]))
                right_walls = len(re.findall('[\|\-LFJ7]', line[ind:]))
                
                transposed = [''.join(list(i)) for i in zip(*new_data)]
                t_line = transposed[ind]
                top = len(re.findall('[\|\-LFJ7]', t_line[0:line_no]))
                bottom = len(re.findall('[\|\-LFJ7]', t_line[line_no + 1:]))
                
                if left_walls == 0 or right_walls == 0 or top == 0 or bottom == 0:
                    continue
                
                if (left_walls % 2 == 1 or right_walls % 2 == 1) and (top % 2 == 1 or bottom % 2 == 1):
                    answer += 1
                
                    copy[line_no] = copy[line_no][0:ind] + 'I' + copy[line_no][ind + 1:]
                    # with open('text10.txt', 'w+') as f:
                    #     f.write(test)
                    #     f.close()
    
    with open('test10.txt', 'w+') as f:
        f.seek(0)
        f.write('\n'.join(copy))
        f.close()
        
    return answer

answer2 = part2()