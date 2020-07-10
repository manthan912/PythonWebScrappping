# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:01:41 2019

@author: MANTHAN
"""
import numpy
board = numpy.array([['-','-','-',],['-','-','-',],['-','-','-']])
p1 = "X"
p2 = "O"




def play():
    turn = 0
    for turn in range(0,9):
        if turn%2 == 0:
            print("x turn")
            place(p1)
            if won(p1):
                break
        else:
            print(" o turn")
            place(p2)
            if won(p2):
                break
    if not(won(p1)) and not(won(p2)):
        print('draw')




def check_row(syb):
    
    for i in range(3):
        count = 0
        for c in range(3):
            if board[i][c] == syb:
                count = count + 1
            if count == 3:
                print(syb,' you have won')
                return True
    return False
def check_col(syb):
    
    for i in range(3):
        count = 0
        for c in range(3):
            if board[c][i] == syb:
                count = count + 1
            if count == 3:
                print(syb,' you have won')
                return True
    return False
def check_diag(syb):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0]==syb:
        print(syb,' you have won ')
        return True
    elif  board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0]==syb:
        print(syb,' you have won ')
        return True

def won(syb):
   return check_row(syb) or check_col(syb) or check_diag(syb)
def place(syb):
    print(numpy.matrix(board))
    while(1):
        row = int(input("row :1 or 2 or 3 : " ))
        col = int(input("col :1 or 2 or 3 : " ))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1] == '-':
            break
        else:
            print('invlaid entry')
    board[row-1][col-1] = syb
play()   