# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:12:17 2023

@author: ap572e
"""

import re

with open('day4_input.txt', 'r') as f:
    data = f.readlines()
    f.close()

class scratchcard:
    def __init__(self,line):
        self.card_no = int(re.search('Card\s*(\d*)', line).group(1))
        self.winning_no = set(re.search('Card\s*\d*:\s*(\d.*)\|', line).group(1).split())
        self.your_no = set(re.search('Card\s*\d*:\s*\d.*\|\s*(\d.*)', line).group(1).split())
        
    
               
def part1(data):
    points = 0
    
    for line in data:
        card = scratchcard(line)
        matches = card.your_no.intersection(card.winning_no)
        if len(matches) > 0:
            points += 2**(len(matches) - 1)
    
    return points

def part2(data):
    points = 0
    copies = {}
    
    for line in data:
        card = scratchcard(line)
        copies[card.card_no] = copies.get(card.card_no, 1)
        matches = card.your_no.intersection(card.winning_no)
        
        if len(matches) > 0:
            points += copies.get(card.card_no, 1) * 2**(len(matches) - 1)
            for m in range(len(matches)):
                copy_card_no = card.card_no + 1 + m
                copies[copy_card_no] = copies.get(copy_card_no, 1) + 1 * copies[card.card_no]
    
    return sum(copies.values())

# answer = part1(data)
answer2 = part2(data)