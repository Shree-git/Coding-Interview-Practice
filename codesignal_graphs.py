# The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional (one-way). He personally prepared the roadRegister of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.

import numpy as np

def solution(roadRegister):
    roadRegister = np.array(roadRegister)
    roadRegisterTranspose = roadRegister.T
    
    counter = [0]*len(roadRegister)
    for i in range(len(roadRegister)):
        for j in range(len(roadRegister[0])):
            if roadRegister[i][j] == True:
                counter[i] += 1
            if roadRegisterTranspose[i][j] == True:
                counter[i] -= 1
    counter = np.array(counter)
    if np.count_nonzero(counter) == 0:
        return True
    else:
        return False



# Given the existing roads and the number of cities in the kingdom, you should use the most modern technologies and find out which roads should be built again to connect each pair of cities. Since the crystal ball is quite old and meticulous, it will only transfer the information if it is sorted properly.

# The roads to be built should be returned in an array sorted lexicographically, with each road stored as [cityi, cityj], where cityi < cityj.

def solution(cities, roads):
    graph = {}
    cit = [x for x in range(cities)]
    for x in range(cities):
        graph[x] = []
    for x,y in roads:
        if not graph.get(x):
            graph[x] = [y]
        else:
            graph[x].append(y)
    sol = []
    for x in graph.keys():
        sol.extend([x,j] for j in cit if j not in graph[x] and j != x and x not in graph[j])
    sol = list(filter(lambda x: x if (x[0]<x[1]) else None, sol))
    return sol


