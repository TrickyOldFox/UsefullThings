# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:52:53 2019

@author: Магистр
"""

import math
import cmath
from math import *
'''
#Zad 2.1
print('Zad 2.1')
i=1
while i<6:
    print(i**3)
    i=i+1
for i in range(6):
    print((i+1)**3)
for i in [1,2,3,4,5]:
    print((i)**3)
#Zad 2.2
print('Zad 2.2')
s=0
N=int(input('Vvedite N: '))
for i in range(N):
    s=s+(i+1)**2
print(s)
#Zad 2.3
print('Zad 2.3')
a=int(input('Vvedite zeloe chislo: '))
if a%2==0:
    print('Parnoe')
else:
    print('Ne parnoe')
#Zad 2.4
print('Zad 2.4')
for i in range(11):
    a=i/10
    print('Dlia x=',a,'Sin(x)=',sin(a),'Tg(x)= ',tan(a),'Exp(x)= ',exp(a))
#Zad 2.5
print('Zad 2.5')
L=list(range(N))
print('Vvedite 8 elementov:')
for i in range(8):
    L[i]=int(input('Vvedite element: '))
for i in range(8):
    L[i]=L[i]**2
    print(L[i])
#Zad 2.6
print('Zad 2.6')
N=int(input("Vvedite kolichestvo elementov: "))
P=list(range(N))
K=list(range(N))
for i in range(N):
    P[i]=int(input('Vvedite element: '))
s=0
for i in range(N):
    K[i]=P[i]**2
    s=s+K[i]
print('Summa kvadratov:',s) 
#Zad 2.7
print('Zad 2.7')
def f(a):
    if a<3:
        return a**2
    if 3<=a<7:
        return a+3
    if a>=7:
        return a
L=list(range(10))
for i in range(10):
    L[i]=i+1
    print(f(L[i]))
#Zad 2.8
print('Zad 2.8')
def f(a,b):
    if a>5:
        return a*b
    if a<=5:
        return 3*a*b/2
L=list(range(11))
b=int(input('Vvedite b: '))
for i in range(11):
    L[i]=i
    print(f(L[i],b))
#Zad 2.9
print('Zad 2.9')
x=float(input('Vvedite x: '))
y=float(input('Vvedite y: '))
n=int(input('Vvedite n: '))
s=0
for i in range(n+1):
    s=s+cos(i*x)
print(s)
s=0
for i in range(n+1):
    s=s+sin(x+i*y)
print(s)
#Zad 2.13
print('Zad 2.13')
a=int(input('Vvedite a: '))
b=int(input('Vvedite b: '))
c=int(input('Vvedite c: '))
D=b**2-4*a*c
if D<0:
    x1=(-b+cmath.sqrt(D))/(2*a)
    x2=(-b-cmath.sqrt(D))/(2*a)
else: 
    if D==0:
        x1=x2=-b/(2*a)
    else:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
print(x1,x2,a*x1**2+b*x1+c,a*x2**2+b*x2+c)
#Zad 2.14
print('Zad 2.14')
a=int(input('Vvedite a: '))
i=-1
b=a
while b!=0:
    c=b%10
    b=b//10
    i=i+1
d=a%10
a=a%10**i+d*10**i-a%10+c
print(a)'''
#Zad 2.15
print('Zad 2.15')
a=list(input('Vvedite spisok :'))
b=len(a)
c=a[0]
for i in range(b-1):
    if a[i+1]>c:
        c=a[i+1]
print(c)
