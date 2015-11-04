#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
sys.path.append("/cygdrive/c/Users/Admin/Desktop/tensor")
from classes import *
from functions import *

def CP_ALS(X1,X2,R=2):
    '''CP_ALSアルゴリズム'''

    '''A(1),A(2),A(3)をそれぞれX(1),X(2),X(3)の一番左側の二列に初期化'''
    A1=Matrix(3,2,[[1,4],[2,5],[3,6]])
    A2=Matrix(4,2,[[1,2],[4,5],[7,8],[10,11]])
    A3=Matrix(2,2,[[1,2],[13,14]])
    A = {1:A1,2:A2,3:A3}    #pythonの辞書でA(n)を格納
    lamda = {1:0,2:0}       #pythonの辞書でlambdaを格納
    for liter in range(0,1):    #リタレーションの回数、ここでは1回だけにする
        for n in range(1,4):    #A(1),A(2),A(3)の順番で回す

            '''V<-A(1)TA(1)*...A(n-1)TA(n-1)*A(n+1)TA(n+1)*...*A(N)TA(N)'''
            V = Matrix(2,2) #Vを初期化
            for i in range(1,4):    #Hadamard積を計算するために回す
                if i == n:  
                    continue    #A(n)自身は計算しない
                else:
                    temp = MatrixProduct(A[i].Transpose(),A[i])     #A(i)TA(i)を計算
                    V = Hadamard(temp,V)    #Hadamard積を計算

            '''A(N)<-X(N)(A(N)...A(1))V+'''
            #model-nを決める
            if n==1:
                multiplier1 = Model1(X1,X2)
            elif n==2:
                multiplier1 = Model2(X1,X2)
            elif n==3:
                multiplier1 = Model3(X1,X2)
            multiplier2 = Matrix(1,2)   #Khatir_Rao積を初期化
            for i in range(3,0,-1):     #Khatir_Rao積を計算するために回す
                if i == n:
                    continue    #A(n)自身は計算しない
                else:
                    multiplier2 = Khatir_Rao(multiplier2,A[i])  #Khatir_Rao積を計算
            multiplier3 = PInverse(V)   #VのMP一般行列
            temp = MatrixProduct(multiplier1,multiplier2)
            A[n] = MatrixProduct(multiplier2,multiplier3)   #行列の積によるA[n]を格納
                    
            '''normalize columns of A(n),storing norms as lambda'''
            #A[n]の各列のノルムを計算、lambdaとして格納
            for j in range(1,A[n].N+1):
                column = Vector(A[n].M)
                for i in range(1,A[n].M+1):
                    column[i] = A[n][i][j]
                lamda[j] = Norm(column)

        '''return lamda and A(1),A(2)...A(N)'''
        #結果を出力
        for n in range(1,4):
            print "A(%d)"%n
            A[n].mprint()
            print
            print
        print lamda[1],lamda[2]



if __name__ == "__main__":
    X1 = Matrix(3,4,[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
    X2 = Matrix(3,4,[[13,16,19,22],[14,17,20,23],[15,18,21,24]])
    CP_ALS(X1,X2)

