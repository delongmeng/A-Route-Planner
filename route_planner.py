#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:21:07 2020

@author: delongmeng
"""

# Implementing a Route Planner
# use A* search to implement a "Google-maps" style route planning algorithm


# Run this cell first!

from helpers import Map, load_map, show_map
from student_code import shortest_path

%load_ext autoreload
%autoreload 2



# Map Basics

map_10 = load_map('map-10.pickle')
show_map(map_10)


map_10.intersections

# {0: [0.7798606835438107, 0.6922727646627362],
#  1: [0.7647837074641568, 0.3252670836724646],
#  2: [0.7155217893995438, 0.20026498027300055],
#  3: [0.7076566826610747, 0.3278339270610988],
#  4: [0.8325506249953353, 0.02310946309985762],
#  5: [0.49016747075266875, 0.5464878695400415],
#  6: [0.8820353070895344, 0.6791919587749445],
#  7: [0.46247219371675075, 0.6258061621642713],
#  8: [0.11622158839385677, 0.11236327488812581],
#  9: [0.1285377678230034, 0.3285840695698353]}


# Roads

# The roads property is a list where, if i is an intersection, roads[i] contains 
# a list of the intersections that intersection i connects to.


# this shows that intersection 0 connects to intersections 7, 6, and 5
map_10.roads[0] 
# [7, 6, 5]


# This shows the full connectivity of the map
map_10.roads


# [[7, 6, 5],
#  [4, 3, 2],
#  [4, 3, 1],
#  [5, 4, 1, 2],
#  [1, 2, 3],
#  [7, 0, 3],
#  [0],
#  [0, 5],
#  [9],
#  [8]]



# map_40 is a bigger map than map_10
map_40 = load_map('map-40.pickle')
show_map(map_40)


# Advanced Visualizations

# The show_map function which generated this map also takes a few optional parameters which might be useful for visualizaing the output of the search algorithm you will write.

# start - The "start" node for the search algorithm.
# goal - The "goal" node.
# path - An array of integers which corresponds to a valid sequence of intersection visits on the map.


# run this code, note the effect of including the optional
# parameters in the function call.
show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])


# The algorithm you write will be responsible for generating a path like the one passed into show_map above. In fact, when called with the same map, start and goal, as above you algorithm should produce the path [5, 16, 37, 12, 34]

# > shortest_path(map_40, 5, 34)
# [5, 16, 37, 12, 34]



path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)


from test import test

test(shortest_path)





