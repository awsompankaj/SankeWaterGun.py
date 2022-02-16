# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:43:02 2022

@author: pankaj
"""
from sys import exit
import random

choices = ['s', 'w', 'g']

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'g':
            return True
       
def comp(randNo):
    switcher = {
        1:'s',
        2:'w',
        3:'g'
        }
    return switcher.get(randNo, "Invalid Choice")
def result(a):
    switcher = {
        None:'Game is tie',
        True:'You Win',
        False:'You Lose'
        }
    return switcher.get(a)

print("Computer turn: Snake(s) Water (w) or Gun (g)")
randNo = random.randint(1, 3)

comp = comp(randNo)

while True:
    
    you = str(input("Enter your choice: Snake(s) Water (w) or Gun (g)"))
    if you in choices:
        break
    else:
        print("Enter Valid Choices from 's', 'w', 'g'")
        exit()

a = gameWin(comp, you)   

print(f"computer choice is {comp}")
print(f"Your choice is {you}")

print(result(a))
    
