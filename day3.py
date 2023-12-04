#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:42:58 2023

@author: katyhagerty
"""

import re
import string
import numpy as np

with open('day3_input.txt', 'r') as f:
    data = f.readlines()
    f.close()
    
# def part1(data):
#     for line_no, line in enumerate(data):
#         matches = re.finditer('\W|\.', line)
        
#         for m in matches:
#             ind = m.span()[0]
#             candidates = ''
            
#             #upper left
#             if line_no != 0 and ind != 0:
#                 candidates += data[line_no - 1][ind - 1]
                
#             #upper middle
#             if line_no != 0:
#                 candidates += data[line_no - 1][ind]
                
#             #upper right
#             if line_no != 0 and ind != len(line) - 1:
#                 candidates += data[line_no - 1][ind + 1]
                
#             #left
#             if ind != 0:
#                 candidates += data[line_no][ind - 1]
            
#             #right 
#             if ind != len(line - 1):
#                 candidates += data[line_no][ind + 1]
                
#             #lower left
#             if line_no != len(data) - 1 and ind != 0:
#                 candidates += data[line_no + 1][ind - 1]
            
#             #lower center
#             if line_no != len(data) - 1:
#                 candidates += data[line_no + 1][ind]
                
#             #lower right
#             if line_no != len(data) - 1 and ind != len(line) - 1:
#                 candidates += data[line_no + 1][ind + 1]

def part1(data):
    part_no = 0
    # part_no = []
    test = data.copy()
    
    symbols = string.punctuation
    symbols = symbols.replace('.', '')
    # symbols = '!|"|#|\$|%|&|\'|\(|\)|\*|\+|,|-|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|\{|\||\}|~'
    
    not_symbols = string.ascii_letters + string.digits + '.'
    
    for line_no, line in enumerate(data):
        matches = re.finditer('\d+', line)
        for m in matches:
            
            # index in string 
            start = m.span()[0]
            end = m.span()[1]
            
            rows = [i for i in range(line_no - 1, line_no + 2) if i >= 0 and i < len(data)]
            columns = [i for i in range(start - 1, end + 1) if i >= 0 and i < len(line)]
            
            for r,c in [(i,j) for i in rows for j in columns]:
                if data[r][c]  in symbols:
                    part_no += int(m.group(0))
                    
                    test[line_no] =re.sub(str(m.group(0)), 'A'* len(str(m.group(0))), test[line_no], count=1)                    
                    break
                        
    with open('test.txt', 'w') as f:
        f.seek(0)
        f.write('\n'.join(test))
        f.truncate()
        f.close()
    
    return part_no

def find_no(line, i, line_no):
    matches = re.finditer('\d+', line)
    for m in matches:
        start = m.span()[0]
        end = m.span()[1]
        
        if i >= start and i < end:
            no = m.group(0)
            s = (line_no, start, end)
    return no, s
    

def part2(data):
    answer = 0
    test = data.copy()
    
    for line_no, line in enumerate(data):
        matches = re.finditer('\*', line)
        for m in matches:
            start = m.span()[0]
            end = m.span()[1]
            
            rows = [i for i in range(line_no - 1, line_no + 2) if i >= 0 and i < len(data)]
            columns = [i for i in range(start - 1, end + 1) if i >= 0 and i < len(line)]
            
            adjacent = dict()
            for r,c in [(i,j) for i in rows for j in columns]:
                if data[r][c] in '0123456789':
                    no, s = find_no(data[r], c, r)
                    adjacent[s] = int(no)
            
            if len(adjacent) == 2:
                ratio = np.prod([i for i in adjacent.values()])
                answer += ratio
                t = list(test[line_no])
                t[start] = 'G'
                test[line_no] = ''.join(t)
    
    with open('test2.txt', 'w+') as f:
        f.seek(0)
        f.write('\n'.join(test))
        f.truncate()
        f.close()
    
    return answer
            
            
            
t=['467..114..',
 '...*......',
 '..35..633.',
 '......#...',
 '617*......',
 '.....+.58.',
 '..592.....',
 '......755.',
 '...$.*....',
 '.664.598..']
# answer = part1(data)
answer2 = part2(data)
            

                
            
                
        