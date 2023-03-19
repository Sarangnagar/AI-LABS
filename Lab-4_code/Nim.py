#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

def minmax(intial, is_maxAgent):
    if all(x == 0 for x in intial):
        return (0, []) if is_maxAgent else (1, [])

    best_score = -math.inf if is_maxAgent else math.inf
    best_moves = []

    for i, pile in enumerate(intial):
        for j in range(1, pile + 1):
            new_configuration = intial[:]
            new_configuration[i] = pile - j
            current_score, moves = minmax(new_configuration, not is_maxAgent)
            if is_maxAgent:
                if current_score > best_score:
                    best_score = current_score
                    best_moves = [(i, j)] + moves
            else:
                if current_score < best_score:
                    best_score = current_score
                    best_moves = [(i, j)] + moves

    return (best_score, best_moves)

def main():
    intial = list(map(int, input("Enter the number of objects in each Piles, separated by spaces: ").split()))
    turn=True # false => Player 1
    
    while True:
      if turn:
        print("Current state of the game:", intial)
        pile_select = int(input(" Player Select Pile? (between 1 and %d): " % len(intial))) - 1
        if pile_select < 0 or pile_select >= len(intial):
            print("Invalid Pile. Please try again.")
            continue
        remove = int(input("Player No of objects to remove? (between 1 and %d): " % intial[pile_select]))
        if remove < 1 or remove > intial[pile_select]:
            print("Invalid input. Please try again.")
            continue
        intial[pile_select] -= remove
        turn = False
        if all(x == 0 for   x in intial):
            print("You win!")
            return
      else:
        print("Current state of the game:", intial)
        current_score, moves = minmax(intial, True)
        pile_select, remove = moves[0]
        intial[pile_select] -= remove
        print("Computer removed", remove, "objects from pile", pile_select + 1)
        print("Current state of the game:", intial)
        turn = True
        if all(x == 0 for x in intial):
            print("Computer win!")
            return 
main()


# In[ ]:




