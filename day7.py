# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:38:06 2023

@author: ap572e
"""

import re

with open('day7_input.txt', 'r') as f:
    data = f.readlines()
    f.close()

s = {
        'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
        '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, 
        '4': 3, '3':2, '2': 1
        }

part2_s = {
        'A': 13, 'K': 12, 'Q': 11, 'J': 0, 'T': 9,
        '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, 
        '4': 3, '3':2, '2': 1
        }
    
def strength(x):
    # cards = x[0]
    return [s[i] for i in x]

def strength2(x):
    # cards = x[0]
    return [part2_s[i] for i in x]

def part1():
    hands = [i.split() for i in data]
    
    five = []
    four = []
    full_house = []
    three = []
    two_pair = []
    one_pair = []
    high_card = []
    
    for cards,no in hands:
        d = {i: cards.count(i) for i in cards}
        
        if len(set(cards)) == 1:
            five.append((cards,no))
        elif len(set(cards)) == 5:
             high_card.append((cards,no))
        elif set(d.values()) == {1,4}:
            four.append((cards,no))
        elif set(d.values()) == {2,3}:
            full_house.append((cards,no))
        elif set(d.values()) == {1,3}:
            three.append((cards,no))
        elif set(d.values()) == {1,2} and len(d.keys()) == 3:
            two_pair.append((cards,no))
        else:
            one_pair.append((cards,no))
    
    labels = [high_card, one_pair, two_pair, three, full_house, four, five]
    
    def strength(x):
        cards = x[0]
        s = {
                'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
                '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, 
                '4': 3, '3':2, '2': 1
                }
        return [s[i] for i in cards]
    
    sorted_hands = []
    answer = 0
    for label in labels:
        l = len(sorted_hands)
        label.sort(key = lambda x :strength(x[0]))
        sorted_hands += label
        for ind,val in enumerate(label):
            card, no = val
            answer += (ind + 1 + l) * int(no)
    
    return answer
    
# answer1 = part1()

class hand:
    def __init__(self, cards, no):
        self.orig_cards = cards
        orig_cards = self.orig_cards
        self.wager = no
        self.joker = True if 'J' in cards else False
        self.cards = self.wildcard()
        joker_cards = self.cards
        self.card_values = [part2_s[i] for i in orig_cards]
        self.joker_values = [part2_s[i] for i in joker_cards]
        self.counts = {i: joker_cards.count(i) for i in joker_cards}
        self.type = ''
    
    def wildcard(self):
        orig_cards = self.orig_cards
        d = {i: orig_cards.count(i) for i in orig_cards}
        
        qty = 0
        best_card= []
        for card in d:
            if d[card] == qty:
                qty = d[card]
                best_card.append(card)
            elif d[card] > qty:
                qty = d[card]
                best_card = [card]
        best_card.sort(key = lambda x: strength2(x))
        orig_cards = orig_cards.replace('J', best_card[-1])
        
        return orig_cards
        
def part2():
    hands = [i.split() for i in data]
    
    five = []
    four = []
    full_house = []
    three = []
    two_pair = []
    one_pair = []
    high_card = []
    
    for cards,no in hands:   
            
        # d = {i: cards.count(i) for i in cards}
        ha = hand(cards, no)
        cards = ha.cards
        no = ha.wager
        d = ha.counts
        
        tiebreakers = []
        if ha.joker:
            tiebreakers.append(ha)
        
        if len(set(cards)) == 1:
            five.append(ha)
            ha.type = 'five'
        elif len(set(cards)) == 5:
             high_card.append(ha)
             ha.type = 'high_card'
        elif set(d.values()) == {1,4}:
            four.append(ha)
            ha.type = 'four'
        elif set(d.values()) == {2,3}:
            full_house.append(ha)
            ha.type = 'full_house'
        elif set(d.values()) == {1,3}:
            three.append(ha)
            ha.type = 'three'
        elif set(d.values()) == {1,2} and len(d.keys()) == 3:
            two_pair.append(ha)
            ha.type = 'two_pair'
        else:
            one_pair.append(ha)
            ha.type = 'one_pair'
    
    labels = [high_card, one_pair, two_pair, three, full_house, four, five]
    
    # def strength(x):
    #     cards = x[0]
    #     s = {
    #             'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
    #             '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, 
    #             '4': 3, '3':2, '2': 1
    #             }
    #     return [s[i] for i in cards]
    
    sorted_hands = []
    answer = 0
    for label in labels:
        l = len(sorted_hands)
        label.sort(key = lambda x :x.joker_values)
        n = len(label)
        swapped = False
        for i in range(n - 1):
            for j in range(n - i - 1):
                if label[j].card_values == label[j + 1].card_values:
                    if label[j].joker_values > label[j + 1].joker_values:
                        swapped = True
                        label[j], label[j + 1] = label[j + 1], label[j]
            # if not swapped:
                # return 
        
        # label_tiebreakers = set(tiebreakers).intersection(label)
        # if len(label_tiebreakers):
        #     for c,n in label_tiebreakers:
        #         ind = label.find((c,n))
        #         if label[ind - 1][0] == c:
                    
                
        sorted_hands += label
        for ind,val in enumerate(label):
            answer += (ind + 1 + l) * int(val.wager)
            
    with open('test7.txt', 'w+') as f:
        f.seek(0)
        d = [f'{i.cards} {i.orig_cards} {i.type} {i.joker}' for i in sorted_hands]
        f.write('\n'.join(d))
        f.close()
    
    return answer
    
answer2 = part2()

