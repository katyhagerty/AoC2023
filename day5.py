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

    for line in data:
        dest, source, length = [int(i) for i in line.split()]
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
    
# part 1
# 1 h 20 min
