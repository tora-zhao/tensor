#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
sys.path.append("/cygdrive/c/Users/Admin/Desktop/tensor")
from classes import *
from numpy import *

def InnerProduct(M1,M2):
    '''行列またはベクトルの内積を計算'''
    m = M1.M
    try:    #行列
        n=M1.N
        sum = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                sum += M1[i][j]*M2[i][j]
        return sum
    except: #ベクトル
        sum = 0
        for i in range(1,m+1):
            sum += M1[i]*M2[i]
        return sum

def Norm(M):
    '''行列またはベクトルのノルムを内積を用いて計算'''
    return InnerProduct(M,M)


def MatrixProduct(M1,M2):
    '''行列の積を計算'''
    m1,n1 = M1.M,M1.N
    m2,n2 = M2.M,M2.N
    Production = Matrix(m1,n2) 
    for i in range(1,m1+1):
        for j in range(1,n2+1):
            sum = 0
            for k in range(1,n1+1):
                sum += M1[i][k]*M2[k][j]
            Production[i][j] = sum 
    return Production

def OuterProduct(V1,V2):
    '''行列の外積を計算'''
    m1,m2 = V1.M,V2.M
    Production = Matrix(m1,m2)
    for i in range(1,m1+1):
        for j in range(1,m2+1):
            Production[i][j] = V1[i]*V2[j]
    return Production

def Kronecker(M1,M2):
    '''行列のKronecker積を計算'''
    m1,n1 = M1.M,M1.N
    m2,n2 = M2.M,M2.N
    m,n = m1*m2,n1*n2
    Production = Matrix(m,n)
    for i in range(1,m1+1):
        for j in range(1,n1+1):
            for k in range(1,m2+1):
                for l in range(1,n2+1):
                    Production[(i-1)*m2+k][(j-1)*n2+l]=M1[i][j]*M2[k][l]
    return Production

def Khatir_Rao(M1,M2):
    '''行列のKhatir_Rao積を計算'''
    m1,n1 = M1.M,M1.N
    m2,n2 = M2.M,M2.N
    m,n = m1*m2,n1
    Production = Matrix(m,n)
    for i in range(1,m1+1):
        for j in range(1,m2+1):
            for k in range(1,n+1):
                Production[(i-1)*m2+j][k]=M1[i][k]*M2[j][k]
    return Production

def Hadamard(M1,M2):
    '''行列のHadamard積を計算'''
    m1,n1 = M1.M,M1.N
    m,n = m1,n1
    Production = Matrix(m,n)
    for i in range(1,m+1):
        for j in range(1,n+1):
            Production[i][j]=M1[i][j]*M2[i][j]
    return Production

def PInverse(M):
    '''numpy.linalg.pinvを用いてMP一般逆行列を計算'''
    m,n = M.M,M.N
    cells,lines = [],[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            cells.append(str(M[i][j]))
        lines.append(",".join(cells))
        cells = []
    mstr = "["+";".join(lines)+"]" #行列をnumpyが認識できる形式に転換
    a=mat(mstr)
    b=linalg.pinv(a)    #MP一般逆行列を求める
    
    #定義されたMatrixクラスの対象に転換する
    k,l = 0,0
    elements = []
    b = str(b).replace("[","").replace("]","")
    lines = b.split("\n")
    for line in lines:
        cells = line.split()
        elements.append(cells)
    k = len(elements) 
    l = len(elements[0])    

    Production = Matrix(k,l)
    for i in range(1,k+1):
        for j in range(1,l+1):
            Production[i][j]=float(elements[i-1][j-1])
    return Production

def Model1(X1,X2):
    '''Model-1の行列を求める'''
    m,n = X1.M,X1.N
    Production = Matrix(m,n+n)
    for j in range(1,n+1):
        for i in range(1,m+1):
            Production[i][j] = X1[i][j]
    for j in range(1,n+1):
        for i in range(1,m+1):
            Production[i][n+j] = X2[i][j]
    return Production

def Model2(X1,X2):
    '''Model-2の行列を求める'''
    m,n = X1.M,X1.N
    Production = Matrix(n,m+m)
    for i in range(1,m+1):
        for j in range(1,n+1):
            Production[j][i] = X1[i][j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            Production[j][m+i] = X2[i][j]
    return Production

def Model3(X1,X2):
    '''Model-3の行列を求める'''
    m,n = X1.M,X1.N
    Production = Matrix(2,m*n)
    for j in range(1,n+1):
        for i in range(1,m+1):
            Production[1][(j-1)*m+i] = X1[i][j]
    for j in range(1,n+1):
        for i in range(1,m+1):
            Production[2][(j-1)*m+i] = X2[i][j]
    return Production

def nModeProduct(U,X1,X2,n):
    '''行列Uとテンソルのmodel-n積を計算'''
    if n == 1:
        X = Model1(X1,X2)
    elif n == 2:
        X = Model2(X1,X2)
    elif n == 3:
        X = Model3(X1,X2)
    else:
        print "No such Mode"
    return MatrixProduct(U,X)

def MatrixDivision1(M):
    X,Y = Matrix(M.M,M.N/2),Matrix(M.M,M.N/2)
    for i in range(1,M.M+1):
        for j in range(1,M.N+1):
            if j <= M.N/2 :
                X[i][j] = M[i][j]
            else:
                Y[i][j-M.N/2] = M[i][j]
    return X,Y
            
def MatrixDivision2(M):
    X,Y = Matrix(M.N/2,M.M),Matrix(M.N/2,M.M)
    for i in range(1,M.M+1):
        for j in range(1,M.N+1):
            if j <= M.N/2 :
                X[j][i] = M[i][j]
            else:
                Y[j-M.N/2][i] = M[i][j]
    return X,Y

def MatrixDivision3(M):
    X,Y = Matrix(M.N/2,M.M),Matrix(M.N/2,M.M)
    for i in range(1,M.M+1):
        for j in range(1,M.N+1):
            if j <= M.N/2 :
                X[j][i] = M[i][j]
            else:
                Y[j-M.N/2][i] = M[i][j]
    return X,Y

def mconvert1(M):
    '''本プログラムにより定義された行列→numpyにより定義された行列'''
    m,n = M.M,M.N
    cells,lines = [],[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            cells.append(str(M[i][j]))
        lines.append(",".join(cells))
        cells = []
    mstr = "["+";".join(lines)+"]" #行列をnumpyが認識できる形式に転換
    return mat(mstr)

def mconvert2(M):
    '''numpyにより定義された行列→本プログラムにより定義された行列'''
    m,n = 0,0
    elements = []
    M = str(M).replace("[","").replace("]","")
    lines = M.split("\n")
    for line in lines:
        cells = line.split()
        elements.append(cells)
    m = len(elements) 
    n = len(elements[0])    
    M = Matrix(m,n)
    for i in range(1,m+1):
        for j in range(1,n+1):
            M[i][j]=float(elements[i-1][j-1])
    return M

def left_singular_vectors(M):
    '''固有ベクトルを計算'''
    m = mconvert1(MatrixProduct(M,M.Transpose()))
    #print linalg.eig(m)
    a,b = linalg.eig(m)

    temp = mconvert2(b)
    result = Matrix(temp.M,temp.N)
    for i in range(1,temp.M+1):
        for j in range(1,temp.N+1):
            result[i][j] = temp[i][j]
    return result

def leading_left_singular_vectors(M):
    '''固有ベクトルを計算'''
    m = mconvert1(MatrixProduct(M,M.Transpose()))
    a,b = linalg.eig(m)

    n = linalg.matrix_rank(m)

    temp = mconvert2(b)
    result = Matrix(n,temp.N)
    for i in range(1,n+1):
        for j in range(1,temp.N+1):
            result[i][j] = temp[i][j]
    return result

if __name__=="__main__":
    '''test code'''

    X1 = Matrix(3,4,[[1,4,7,10],[2,5,8,11],[3,6,9,12]])
    X2 = Matrix(3,4,[[13,16,19,22],[14,17,20,23],[15,18,21,24]])
    U  = Matrix(2,3,[[1,3,5],[2,4,6]])
    V  = Matrix(2,4,[[1,3,5,7],[2,4,6,8]])
    W  = Matrix(2,2,[[1,3],[2,4]])
  


    #left_singular_vectors(X1)
    #print
    temp = Model3(X1,X2)
    temp.mprint()
    print
    MatrixProduct(W,temp).mprint()
    #print linalg.matrix_rank(mconvert1(temp))
    #temp = nModeProduct(V,X1,X2,2)
    #temp.mprint()
    #g1,g2 = MatrixDivision2(temp)
    #Model2(g1,g2).mprint()
    #temp = nModeProduct(V,g1,g2,1)
    #temp.mprint()
    #g1,g2 = MatrixDivision(temp)
    
    g1.mprint()
    g2.mprint()
