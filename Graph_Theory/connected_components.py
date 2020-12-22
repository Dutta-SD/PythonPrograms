#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:06:59 2020

@author: sandip
"""
# Connected Components: Different colors sort of
# Depth first search can be useful to identify the components
# If all coloured same, then all components connected. 
# Connected - there is a path between any two nodes,
# either direct path or through other nodes

# Idea: Start DFS at every node
# If already visited, do not visit

#n : number of connected nodes in the graph
n = 5
# g is the adjacency list
# It is going to be a list of lists
# Index of each element is going to be the list of
# neighbors of that index
g = [[1],
     [2],
     [1, 3, 4],
     [2, 4],
     [2, 3]]

# visited marks if each index is visited or not
# index of one element marked means we have visited it
visited = [False]*n 

# count: counts the number of connected compononts
# also can think as number of clusters
count = 0

# Components: stores count of components for particular node
components = [0]*n

# DFS function:
# Normal case, get one node and dfs on it

def DFS(at_):    #at_: specifies 'at' which node we are on
    # If we have not visited the node, mark the node as visited first
    visited[at_] = True
    # Put the cluster number to that element. 
    components[at_] = count
    # Now we extract the node one by one, and do DFS in each
    for next_node in g[at_]:
        # if visited we will not traverse it, so no base case
        if not visited[next_node]:
            # since we do dfs on only unvisited nodes, so we need no base case here
            DFS(next_node)
            

def findComponents(): # finds the number of components
    # Do DFS for each node to determine components
    # Only visit that node which is not visited yet
    global count
    #Traverse all nodes, we need to do dfs in all nodes.
    for node in range(n):
        # If unvisited node, then do dfs.
        # unvisited nodes 2 types: first node and other cluster node
        if not visited[node]:
            # if unvisited node, increase the count of clusters by 1
            # if first node, we give it 1, else if other cluster count increases by 1
            count += 1
            # Operate dfs on the node that is not labelled/colored/marked/
            #not part of that cluster
            DFS(node)


findComponents()
    
print(f"count {count}, components {components}")

            
            

            
