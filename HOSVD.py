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

    print "結果："
        for i in range(1,4):
            print "A(%d):"%(i)
            A[i].mprint()
            T = nModeProduct(T,A[i].Transpose(),i)
            print

        T.tprint()
            
        #Y = X ×1A(1) ×2A(2) ×3A(3)より結果を検証
    print "検証："
        for i in range(1,4):
            print "A(%d):"%(i)
            A[i].mprint()
            T = nModeProduct(T,A[i],i)
            print
        T.tprint()


if __name__ == "__main__":
    X1 = Matrix(3,4,[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
    X2 = Matrix(3,4,[[13,16,19,22],[14,17,20,23],[15,18,21,24]])
    HOSVD(X1,X2)

    

