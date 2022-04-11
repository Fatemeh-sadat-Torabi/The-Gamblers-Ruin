# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 20:09:15 2022

@author: FARZANE.T
"""

import sys
import random

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
wins = 0
bets = 0

for t in range(trials):
    cash = stake 
    while cash > 0 and cash < goal : 
        bets+=1
        if random.randrange(0,2)==0:
            cash +=1
        else:
            cash -=1
    if cash == goal : 
        wins+=1
print('% wins : ',str(100*wins//trials))
print('average # of bets: ',str(bets//trials))