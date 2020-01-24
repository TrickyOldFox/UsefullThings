# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:07:12 2019

@author: Магистр
"""

def root(f,a,b,eps=0.01):
    if (abs(a-b)>eps):
        if (f(a)*f((a+b)/2))<0:
            return root(f,a,(a+b)/2,eps)
        else:
            if (f((a+b)/2)*f(b)<0):
                return root(f,(a+b)/2,b,eps)
            else: return root(f,a/2+(a+b)/4,(a+b)/2+(a+b)/4,eps)
    else:
        return (a+b)/2
def sum3(a,b,c,n=1):
    return a**n+b**n+c**n
def sumn(n=1,*a):
    s=0
    for i in a:
        s=s+i**n
    return s