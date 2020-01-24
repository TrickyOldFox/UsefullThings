# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:06:24 2019

@author: Магистр
"""
#1.1
print('Zad 1.1')
a=6*3-0.8/(1.5/((3/2)*0.4*50/(1/(1/2))))+ 1/4 + (1+1/2*1/0.25)/(6-46/(1+2.2*10))
print(a)
#1.2
print('Zad 1.2')
import math
import cmath
from math import *
a=2;b=3
z1=exp(b)*sin(a)
z2=a**(1/3)*b**(2/7)
print(z1,z2)

#1.3
print('Zad 1.3')
for i in range(4):
    print(log(i+2))
#1.4
#x**2-11*x+28=0
print('Zad 1.4')
D=11**2-4*28
if D<0:
    print('Net korney')
else:
    x1=(11+sqrt(D))/2
    x2=(11-sqrt(D))/2
    print(x1,x2,x1**2-11*x1+28)
#1.5
print('Zad 1.5')
z1=1/3*(3-5j); z2=1+2j
print(z1+z2,z1*z2,z1**2+z2**3,z1/z2)
#1.6
print('Zad 1.6')
print(((2+1j)*(1/2+3j))**(-2),(1-2j)/(2+3j)-(3+1j)/2j)
#1.7
print('Zad 1.7')
z1=(1+1j)**15/(1-1j)**9
z2=(2-3j)*cmath.sqrt(-1+1j)
z3=(1+1j+1j**2+1j**3)**10
print(cmath.polar(z1),cmath.polar(z2),cmath.polar(z3))
#1.8
print('Zad1.8')
print(sin(1)*cmath.sin(1+1j)*sqrt(3)+cmath.sqrt(1-1j))
#1.9
print('Zad1.11')
surname=input('Vvedite Familiju ')
age=int(input('Vvedite Vozrast '))
mark=float(input('Vvedite ozenku '))
print('Familija:',surname,'Vozrast:',age,'Ozenka:',mark)
