#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:45:36 2023

@author: katyhagerty
"""
import re

with open('day19_input.txt', 'r') as f:
    data = f.read()
    # data = [list(i) for i in data]
    f.close()
    
# class Part:
#     def __init__(self,line):
#         self.x = re.search('x=(\d*)', line).group(1)
#         self.m = re.search('m=(\d*)', line).group(1)
#         self.a = re.search('a=(\d*)', line).group(1)
#         self.s = re.search('s=(\d*)', line).group(1)
#         self.status = 'U'
    
#     def get(self, string):
#         return self.string

def rate(part,ratings,  key):
    
    part = re.search('\{(.*)\}', part).group(1)
    part = part.split(',')
    d = {}
    for i in part:
        k,v = i.split('=')
        d[k] = v
        
        
    # result = False
    # while !result:
    rating = re.search(key + '{(.*)}', ratings).group(1)
    tests = rating.split(',')        
    for test in tests:
        if '<' in test:
            var, value = test.split('<')
            if d[var] < value:
                key = test.split(':')[0]
            else: 
                continue
        else:
            var,value = test.split('>')
            if d[var] > value:
                key = test.split(':')[0]
            else:
                continue
        
        if key == 'R' or key == 'A':
            return key
        else:
            rate(part, ratings,key)
            

def part1():
    ratings, parts = data.split('\n\n')
    # ratings = ratings.split('\n')
    parts = parts.split('\n')
    
    for part in parts:
        # p = Part(part)
        # rating = Rating('in')
        key = 'in'
        result = rate(part, ratings, key)
            
    
    
answer1 = part1()