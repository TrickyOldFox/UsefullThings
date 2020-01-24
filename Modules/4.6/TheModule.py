# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:13:58 2019

@author: karan
"""
def Scalar (A,B):
    S=0
    if len(A)==len(B):    
        for i in range(len(A)):
            S=S+A[i]*B[i]
    else:
        print('Wrong data input')
    return S
def ListInput (name):
    n=1; A=[]
    while (n!='S'):
        n=input('Enter the element of the list, to break enter S  : ')
        if (n!='S'):
            A.append(int(n))
        else:
            print('List ',name,' saved')
    return(A)
def Sochet(n,m):
    if (m==1):
        return n
    else:
        if (n==m+1):
            return n
        else:
            return (Sochet(n-1,m-1)+Sochet(n-1,m))
def CircleArea(R):
    import math
    return math.pi*R**2
def CircleLength(R):
    import math
    return 2*math.pi*R
def CircleAreaSector(R,fi):
    import math
    return math.pi*R**2*360/fi
def TriangularArea(x1,y1,x2,y2,x3,y3):
    A=1/2*((x1-x3)*(y2-y3)-(y1-y3)*(x2-x3))
    if A>0:
        return A
    else:
        return -A
def TriangularLength(x1,y1,x2,y2,x3,y3):
    import math
    return (math.sqrt((x1-x2)**2+(y1-y2)**2)+math.sqrt((x3-x2)**2+(y3-y2)**2)+math.sqrt((x1-x3)**2+(y1-y3)**2))

