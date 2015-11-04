#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
from collections import defaultdict

class Vector(defaultdict):
    M = 0   #次元数
    def __init__(self,m,element_list=[]):
        '''初期化の方法 M=Vector(次元数)'''
        '''あるいは (1,2) を初期化する場合を例として　M=Vector(2,[1,2])'''
        if not element_list:
            self.M = m
            for i in range(1,m+1):
                self[i] = 0
        else:
            self.M = m
            for i in range(1,m+1):
                self[i] = element_list[i-1] 

    def vprint(self):
        #ベクトルをpythonの行列の形式で出力
        m = self.M
        temp = []
        for i in range(1,m+1):
            temp.append(self[i])
        print temp


class Matrix(defaultdict):
    M = 0   #横
    N = 0   #縦

    def __init__(self,m,n,element_list=[]):
        '''初期化の方法 M=Matrix(横数,縦数)'''
        '''あるいは 1 2 を初期化する場合を例として　M=Matrix(2,2,[[1,2],[3,4]])'''
        '''         3 4'''
        if not element_list:
            self.M = m  
            self.N = n  #m*nの行列
            for i in range(1,m+1):
                self[i] = defaultdict(dict)
                for j in range(1,n+1):
                    self[i][j] = 1 
        else:
            self.M = m 
            self.N = n
            for i in range(1,m+1):
                self[i] = defaultdict(dict)
                for j in range(1,n+1):
                    self[i][j] = element_list[i-1][j-1]

    def mprint(self):
        #行列を　1 0 のような形式で出力
        #        0 1
        m = self.M
        n = self.N
        for i in range(1,m+1):
            temp = []
            for j in range(1,n+1):
                temp.append(str(self[i][j]))
            print "\t".join(temp)    

    def Transpose(self):
        #行列の転置を求める
        m,n = self.M,self.N
        Production = Matrix(n,m)
        for i in range(1,m+1):
            for j in range(1,n+1):
                Production[j][i] = self[i][j]
        return Production

