#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
sys.path.append("/cygdrive/c/Users/Admin/Desktop/tensor")
from classes import *
from functions import *

def HOOI(X1,X2,R1=2,R2=2,R3=2):
    '''HOOIアルゴリズム'''

    #A(n)を初期化
    X = {1:Model1(X1,X2),2:Model2(X1,X2),3:Model3(X1,X2)}
    A = {}  #A = {1:A1,2:A2,3:A3}
    for i in range(1,4):
        A[i] = left_singular_vectors(X[i])

    N = 1000  #イテレーションの回数
    for I in range(0,N):
        for n in range(1,4):
            for i in range(1,4):
                y1,y2 = X1,X2
                if i == n:
                    continue
                else:
                    temp  = nModeProduct(A[n].Transpose(),y1,y2,n)
                    y1,y2 = MatrixDivision(temp)
                
            if n == 1:
                Y1 = Model1(y1,y2)
                tempA1 = left_singular_vectors(Y1)
            elif n == 2:
                Y2 = Model2(y1,y2)
                tempA2 = left_singular_vectors(Y2)
            elif n == 3:
                Y3 = Model3(y1,y2)
                tempA3 = left_singular_vectors(Y3)
        A[1],A[2],A[3] = tempA1,tempA2,tempA3

    for i in range(1,4):
        print "A(%d):"%(i)
        A[i].mprint()
        print
    #gを計算
    g1,g2 = X1,X2
    for n in range(1,4):
        temp = nModeProduct(A[n].Transpose(),g1,g2,n)
        g1,g2 = MatrixDivision(temp)
    print "g1:"
    g1.mprint()
    print
    print "g2:"
    g2.mprint()
            
                

if __name__ == "__main__":
    X1 = Matrix(3,4,[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
    X2 = Matrix(3,4,[[13,16,19,22],[14,17,20,23],[15,18,21,24]])
    HOOI(X1,X2)

