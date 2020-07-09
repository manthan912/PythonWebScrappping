# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import turtle
turtle.bgcolor("black")
Seurat = turtle.Turtle()
Width = 5
Height = 5
dot_distance = 25
Seurat.setpos(-250,250)
def spiral(m,n):
    k,l = 0,0
    f = 0
    Seurat.color("White")
    while k<m and l<n :
        if f == 1:
            Seurat.right(90)
        for i in range(l,n):
            Seurat.forward(dot_distance)
        k+=1
        f = 1
        Seurat.right(90)
        for i in range(k,m):
            Seurat.forward(dot_distance)
        
        n-=1
        Seurat.right(90)
        
        if(k<m):
            for i in range(n-1,l-1,-1):
                Seurat.forward(dot_distance)
        
        m-=1
        Seurat.right(90)
        if(l<n):
            for i in range(m-1,k-1,-1):
                Seurat.forward(dot_distance)
        l+=1
spiral(20,20)
turtle.done()

