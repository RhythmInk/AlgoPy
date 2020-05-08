#!/usr/bin/python3.7
# Djikstra's Algorithm
#
# Author: Aaron Zolotor
'''
suppose a graph is given as follows

{vertex1: ((vertex_m, edge_weight), ..., (vertex_n, edge_weight)),
 vertex2: ((vertex_r, weight), ..., (vertex_l, weight)),
 ...
}

Problem: Implement Djikstra's algorithm for finding the shortest path
from the given starting node to all other nodes. 
'''
from numpy import inf


def next_vertex(pathes, visited):
    '''
    Searches through currently traveled pathes for the next shortest path to 
    continue on. i.e. Find vertex in pathes whose current path weight is the
    smallest. 

    Note: This search makes no attempts to be efficient.
    '''

    # initialize vertex/weight 
    next_vertex = None
    weight = inf

    for vertex in pathes:
        _, path_weight = pathes[vertex]

        # ignore already visited vertices
        if vertex in visited:
            continue
        # if our vertex is closer to the starting node, then what is currently
        # stored, then reassign
        elif path_weight < weight:
            next_vertex, weight = vertex, path_weight

    return next_vertex


def djikstra(start, end, graph):
    vertices = [key for key in graph.keys()]
    # keep track of previously visted vertices
    visited = []

    # pathes = {vertex:(precessor, weight)}
    pathes = {vertex: (start, inf) for vertex in vertices}

    # update weights of starting node and those adjacent to it
    pathes.update({start: (None, 0)})
    for edge in graph[start]:
        pathes[edge[0]] = ('a', edge[1])

    # handle easy case
    if start == end:
        path = {'a': 'a'}

        return path

    # keep going until all vertices are visted
    while len(visited) < len(vertices):
        # fetch vertex with shortest path distance so far
        current_vertex = next_vertex(pathes, visited)
        # cycle through vertex and edge weight of all vertices connected to
        # our current vertex
        for vertex, weight in graph[current_vertex]:
            # if the path is shorter from our current vertex, repalce
            # predecessor and update path weight
            if (weight + pathes[current_vertex][1]) < pathes[vertex][1]:
                pathes[vertex] = (current_vertex, weight +
                                  pathes[current_vertex][1])

        visited.append(current_vertex)

    return pathes


graph = {'a': (('b', 2), ('c', 4)),
         'b': (('c', 1), ),
         'c': (('e', 3),),
         'd': (('f', 2),),
         'e': (('d', 3), ('f', 2)),
         'f': ()
         }

print(djikstra('a', 'f', graph))


graph = {'a': (('b', 2), ('c', 4)),
         'b': (('c', 1), ('d',2)),
         'c': (('e', 3),),
         'd': (('f', 2),),
         'e': (('d', 3), ('f', 2)),
         'f': ()
         }

print(djikstra('a', 'f', graph))

graph = {'a': (('c', 4),),
         'b': (('c', 1), ('d',2)),
         'c': (('b', 2), ('e', 3),),
         'd': (('f', 2),),
         'e': (('d', 3), ('f', 2)),
         'f': ()
         }

print(djikstra('a', 'f', graph))

graph = {'a': (('b', 2), ('c', 4)),
         'b': (('a', 2), ('c', 1), ('d',2)),
         'c': (('a', 4), ('b', 1), ('e', 3),),
         'd': (('b', 2), ('f', 2),),
         'e': (('c', 3), ('d', 3), ('f', 2)),
         'f': (('e', 2),)
         }

print(djikstra('a', 'f', graph))