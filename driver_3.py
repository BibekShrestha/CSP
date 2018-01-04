# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:48:15 2017

@author: Bibek Shrestha
"""

#driver_3.py
import sys
import AC3Board



OutputFile = open('output.txt','w')

Csp = AC3Board.AC3Board(sys.argv[1])
AC3Board.AC3(Csp)
MySol = None
Csp.AssignAC3Output()
MySol = None
if Csp.IsComplete():
    MySol = Csp.WriteOutput() + ' AC3'
    
elif AC3Board.BackTrack(Csp):
    MySol = Csp.WriteOutput() + ' BTS'
    
OutputFile.write(MySol)
Csp.ShowBoardState()

OutputFile.close()
input()
        

    

    
    
