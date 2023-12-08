#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:58:56 2023

@author: katyhagerty
"""
import re

with open('day5_input.txt', 'r') as f:
    data = f.read()
    f.close()

def search_map(data, value):
    # destination source len
    # soil seed len
    data = [[int(j) for j in i.split()] for i in data]
    # data.sort(key = lambda x:x[1])
    data  = [i for i in data if i[1] <= value and i[2] + i[1] > value]

    for line in data:
        dest, source, length = line
        if source <= value < (source + length):
            return dest + (value - source)
            
    return value

seeds = re.search('seeds:\s(\d.*)', data, flags = re.M).group(1).split()
seed_soil = re.search('seed-to-soil map:\s([\s\d]*\d)', data,flags=re.M).group(1).split('\n')
soil_fertilizer = re.search('soil-to-fertilizer map:\n([\s\d]*\d)', data).group(1).split('\n')
fertilizer_water = re.search('fertilizer-to-water map:\s(\d*[\s\d]*\d)', data,flags=re.M).group(1).split('\n')
water_light = re.search('water-to-light map:\s(\d*[\s\d]*\d)', data,flags=re.M).group(1).split('\n')
light_temp = re.search('light-to-temperature map:\s(\d*[\s\d]*\d)', data,flags=re.M).group(1).split('\n')
temp_humidity = re.search('temperature-to-humidity map:\s(\d*[\s\d]*\d)', data,flags=re.M).group(1).split('\n')
humidity_loc = re.search('humidity-to-location map:\s(\d*[\s\d]*\d)', data,flags=re.M).group(1).split('\n')

def part1():
    answers = []
    for seed in seeds:
        soil = search_map(seed_soil, int(seed))
        fertilizer = search_map(soil_fertilizer, soil)
        water = search_map(fertilizer_water, fertilizer)
        light = search_map(water_light, water)
        temp = search_map(light_temp, light)
        humidity = search_map(temp_humidity, temp)
        loc = search_map(humidity_loc, humidity)
        answers.append(loc)
    return min(answers)
    
# part 1
# 1 h 20 min
# answer1 = part1()
    

def search_map_range(data, ranges):
    # destination source len
    # soil seed len
    
    data = [[int(j) for j in i.split()] for i in data]
    total_ranges = []
    for ra in ranges:
        new_ranges=[]
        # data.sort(key = lambda x:x[1])
        # data  = [i for i in data if i[1] >= ra[0] or i[1] + i[2] > ra[0]]
        start = ra[0]
        length = ra[0] + ra[1]
        filtered_data = [i for i in data if len(set(range(i[1], i[1] + i[2])).intersection(set(range(start,length)))) > 0]
        if filtered_data not in new_ranges:
            new_ranges += filtered_data
        
        # find gaps in new_ranges
        new_ranges.sort(key = lambda x: x[1])
        if len(new_ranges) > 1:
            for ind in range(len(new_ranges) - 1):
                if sum(new_ranges[ind][1:3]) != new_ranges[ind + 1][1]:
                    start = sum(new_ranges[ind])
                    length = new_ranges[ind + 1][0] - start
                    new_ranges.append([start, start, length])
                    new_ranges.sort(key = lambda x: x[1])
        
        for n in new_ranges:
            if n not in total_ranges:
                total_ranges.append(n)
        # total_ranges +=new_ranges
        
    # find gaps between total ranges and ra
    if len(total_ranges) == 0:
        for r in ranges:
            total_ranges.append([r[0], r[0], r[1]])
    # beginning gap
    elif ranges[0][0] < total_ranges[0][1]:
        start = ranges[0][0]
        length = total_ranges[0][1] - start
        total_ranges.append([start,start, length])
        total_ranges.sort(key = lambda x: x[1])
    # trim    
    elif ranges[0][0] > total_ranges[0][1]:
        # trim the fat
        diff = ranges[0][0] - total_ranges[0][1]
        # total_ranges[0] = [i + diff for i in total_ranges[0]] 
        total_ranges[0][0] += diff
        total_ranges[0][1] += diff
        total_ranges[0][2] -= diff
    # end gap    
    if sum(ranges[-1]) > sum(total_ranges[-1][1:3]):
        start = sum(total_ranges[-1][1:3])
        length = sum(ranges[-1]) - start
        total_ranges.append([start, start, length])
    # trim
    elif sum(ranges[-1]) < sum(total_ranges[-1][1:3]):
        diff = sum(total_ranges[-1][1:3]) - sum(ranges[-1])
        total_ranges[-1][-1] -= diff        
    
    #convert total_ranges (map) to values
    total_ranges = [[i[0], i[2]] for i in total_ranges]
    
    # total_ranges += new_ranges
        
        # # add gaps
        # all_new_range = set()
        # for n in new_ranges:
        #     all_new_range = all_new_range.union(range(n[1], n[1] + n[2]))
        
        # gaps = set(range(ra[0], r[1] + r[0])).difference(all_new_range)
        
        # #reformat gaps
        # if len(gaps) > 0:
        #     gaps = gaps
    
    
    #find smallest destination
    # transpose_data = [i for i in zip(*data)]
    # min_destination = min(transpose_data[0])
    # min_index = transpose_data.find(min_destination)
    # data=data[min_index]

    # for line in data:
    #     dest, source, length = line
    #     if source <= value < (source + length):
    #         return dest + (value - source)
            
    # return value
    total_ranges.sort()
    return total_ranges

def find_smallest_loc(loc, start):
    loc.sort(key = lambda x : x[1])
    diff = start - loc[0][1]
    min_loc = loc[0][0] + diff
    return min_loc

def part2():
    answers =[]
    for i in range(int(len(seeds) / 2)):
        start = int(seeds[2 * i])
        r = int(seeds[2* i + 1])

        # for seed in range(start, start + r):
        soil = search_map_range(seed_soil, [[start,r]])
        fertilizer = search_map_range(soil_fertilizer, soil)
        water = search_map_range(fertilizer_water, fertilizer)
        light = search_map_range(water_light, water)
        temp = search_map_range(light_temp, light)
        humidity = search_map_range(temp_humidity, temp)
        loc = search_map_range(humidity_loc, humidity)
        min_loc = find_smallest_loc(loc, start)
        
        answers.append(min_loc)
    return answers

answer2 = part2()

