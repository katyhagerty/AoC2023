# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:08:40 2023

@author: ap572e
"""

with open('day11_input.txt', 'r') as f:
    data = f.readlines()
    data = [i.strip() for i in data]
    data = [[j for j in i] for i in data]
    f.close()
    
def expanding_galaxy(data):
    # find rows without galaxies
    rows = [i for i, text in enumerate(data) if set(text) == {'.'}]
    
    # find columns without galaxies
    transposed = [list(i) for i in zip(*data)]
    columns = [j for j,text in enumerate(transposed) if set(text) == {'.'}]
    
    # expand
    for i, row in enumerate(rows):
        data.insert(i + row, '.' * len(data[0]))
    
    data = [list(i) for i in zip(*data)]
    for j, column in enumerate(columns):
        data.insert(j + column, '.' * len(data[0]))
    data = [list(i) for i in zip(*data)]
    
    return data

def find_galaxies(expanded):
    d = {}
    no = 1
    for i, line in enumerate(expanded):
        for j, letter in enumerate(line):
            if expanded[i][j] == '#':
                d[no] = (i,j)
                no += 1
    
    return d
    
def part1():
    expanded = expanding_galaxy(data)
    galaxy_dict = find_galaxies(expanded)
    
    pairs = []
    for i in galaxy_dict.keys():
        for j in range(i + 1, len(galaxy_dict.keys()) + 1):
            pairs.append((i,j))
            
    answer = 0
    for pair in pairs:
        start_i, start_j = galaxy_dict[pair[0]]
        end_i, end_j = galaxy_dict[pair[1]]
        distance = abs(end_i - start_i) + abs(end_j - start_j)
        
        # print(pair)
        # print(distance)
        # print('')
        
        answer += distance
            
    return answer
    
# answer1 = part1()

def expanding_galaxy2(data):
    # find rows without galaxies
    rows = [i for i, text in enumerate(data) if set(text) == {'.'}]
    
    # find columns without galaxies
    transposed = [list(i) for i in zip(*data)]
    columns = [j for j,text in enumerate(transposed) if set(text) == {'.'}]    
   
    return rows, columns
    

def part2():
    rows, columns = expanding_galaxy2(data)
    galaxy_dict = find_galaxies(data)
    
    pairs = []
    for i in galaxy_dict.keys():
        for j in range(i + 1, len(galaxy_dict.keys()) + 1):
            pairs.append((i,j))
            
    answer = 0
    for pair in pairs:
        start_i, start_j = galaxy_dict[pair[0]]
        end_i, end_j = galaxy_dict[pair[1]]
        distance = abs(end_i - start_i) + abs(end_j - start_j)
        
        # account for expanded galaxies
        top_row = min(start_i, end_i)
        bottom_row = max(start_i, end_i)
        left_col = min(start_j, end_j)
        right_col = max(start_j, end_j)
        
        factor = 999999
        distance += factor * len(set(range(top_row, bottom_row)).intersection(rows))
        distance += factor * len(set(range(left_col, right_col)).intersection(columns))
        
        # print(pair)
        # print(distance)
        # print('')
        
        answer += distance
            
    return answer

answer2 = part2()