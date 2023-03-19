#!/usr/bin/env python
# coding: utf-8

# In[10]:


import heapq
import numpy as np

goal_state = np.array([[5,1,4],[0,3,2],[7,6,8]])

# Manhatten distance heuristic
def manhatten_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                distance += abs(i - (state[i][j] - 1) // 3) + abs(j - (state[i][j] - 1) % 3)
    return distance

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # cost of the path from the initial state to the current state
        self.h = h  # estimated cost of the path from the current state to the goal state
        self.f = g + h  # total estimated cost of the path from the initial state to the goal state
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return np.array_equal(self.state, other.state)
    
    def __hash__(self):
        return hash(str(self.state))

# generate successor nodes
def successors(node):
    successors = []
    i, j = np.where(node.state == 0)
    moves = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for move in moves:
        if 0 <= move[0] < 3 and 0 <= move[1] < 3:
            new_state = np.copy(node.state)
            new_state[i,j], new_state[move[0],move[1]] = new_state[move[0],move[1]], new_state[i,j]
            successors.append(Node(new_state, node, node.g + 1, manhatten_distance(new_state)))
    return successors

# A* search algorithm
def a_star_search(initial_state):
    initial_node = Node(initial_state, None, 0, manhatten_distance(initial_state))
    frontier = [initial_node]
    explored = set()
    while frontier:
        node = heapq.heappop(frontier)
        if np.array_equal(node.state, goal_state):
            path = [node.state]
            while node.parent:
                node = node.parent
                path.append(node.state)
            return path[::-1]
        explored.add(node)
        for successor in successors(node):
            if successor in explored:
                continue
            for frontier_node in frontier:
                if np.array_equal(successor.state, frontier_node.state) and successor.g >= frontier_node.g:
                    break
            else:
                heapq.heappush(frontier, successor)
    return None

# test
initial_state = np.array([[1,3,4],[5,2,0],[7,6,8]])
path = a_star_search(initial_state)
for state in path:
    print(state)
    print()


# In[ ]:





# In[ ]:




