# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:08:53 2017

@author: Bibek Shrestha
"""

#driver.py

import AC3Board



SudokuInput = open('sudokus_start.txt','r')
SudokuOutput = open('sudokus_finish.txt','r')

i = 1
j = 0
MySol = None

for Line in SudokuInput:
    Csp = AC3Board.AC3Board(Line)
    AC3Board.AC3(Csp)
    MySol = None
    Csp.AssignAC3Output()
    if Csp.IsComplete():
       MySol = Csp.WriteOutput() + ' AC3\n'
       
       
    elif AC3Board.BackTrack(Csp):
        MySol = Csp.WriteOutput() + ' BTS\n'
        
    Solution = SudokuOutput.readline()
    #print(MySol)
    #print(Solution)
    if  MySol == Solution :
        j = j + 1
    print( j ,'out of', i)
    i = i + 1
    

    
    