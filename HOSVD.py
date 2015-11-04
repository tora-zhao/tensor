#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
sys.path.append("/cygdrive/c/Users/Admin/Desktop/tensor")
from classes import *
from functions import *

def HOSVD(X1,X2,R1=2,R2=2,R3=2):
    '''HOSVDアルゴリズム'''

    #A(n)を計算
    X = {1:Model1(X1,X2),2:Model2(X1,X2),3:Model3(X1,X2)}
    A = {}  #A = {1:A1,2:A2,3:A3}
    for i in range(1,4):
        A[i] = left_singular_vectors(X[i])

    for i in range(1,4):
        print "A(%d):"%(i)
        A[i].mprint()
        print

    temp = nModeProduct(A[1].Transpose(),X1,X2,1)
    temp.mprint()
    print
    g1,g2 = MatrixDivision(temp)
    temp = Model2(g1,g2)
    MatrixProduct(A[2].Transpose(),temp).mprint()
    #temp = nModeProduct(A[2].Transpose(),g1,g2,2)
    #temp.mprint()
    #gを計算
    #g1,g2 = X1,X2
    #for n in range(1,4):
    #    temp = nModeProduct(A[n].Transpose(),g1,g2,n)
    #    g1,g2 = MatrixDivision(temp)
    #    print "g1:"
    #    g1.mprint()
    #    print
    #    print "g2:"
    #    g2.mprint()

    #temp = nModeProduct(A[1],g1,g2,1)
    #g1,g2 = MatrixDivision(temp)
            

if __name__ == "__main__":
    X1 = Matrix(3,4,[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
    X2 = Matrix(3,4,[[13,16,19,22],[14,17,20,23],[15,18,21,24]])
    HOSVD(X1,X2)

    

