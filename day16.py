# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:39:31 2023

@author: ap572e
"""

with open('day16_input.txt', 'r') as f:
    data = f.readlines()
    f.close()

# north, south, east, west    
d = {
     '.': [[-1, 0], [1, 0], [0, 1], [0, -1]],
     #  '/': [[-1, 1], [1, -1], [1, -1], [-1, 1]],
     # '\\': [[-1, -1], [1, 1], [1, 1], [-1,-1]],
      '/': [[0, 1], [0, -1], [-1, 0], [1, 0]],
     '\\': [[0, -1], [0, 1], [-1, 0], [1, 0]],     
     '|': [[-1, 0], [1, 0], [[-1, 0], [1, 0]], [[-1, 0], [1, 0]]],
     '-': [[-1, 0], [1,0], [[0, 1], [0, -1]], [[1, 0], [-1, 0]]]
     }

dd = {
      0: (-1, 0),
      1: (1, 0),
      2: (0, 1),
      3: (0, -1)
      }

def find_next(position,direction):
    x, y = position
    i, j = dd[direction]
    if len(data) <= x + i < 0 or len(data[0]) <= y + j < 0:
        print(x + i)
        print(y + j)
        return []
    
    new_points = d[data[x + i][y + j]][direction]
    # new_points = d[next_symbol][direction]
    if type(new_points) != list:
        new_points = list(list(new_points))
    
    # for points in new_points:
    xx, yy = new_points
    if xx == -1:
        direction = 1
    elif xx == 1:
        direction = 0
    elif yy == 1: 
        direction = 2
    else:
        direction = 3
        
    return (xx +x , yy + y), direction
        
    
def part1():
    positions = [(0,0)]
    direction = 2
    while len(positions) > 0:
        for position in positions:
            positions, directions = find_next(position,direction)
    
answer1 = part1()
    
    