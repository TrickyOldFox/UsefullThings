# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:50:25 2019

@author: karan
"""
import math
import cmath
import random
from math import *
'''#Zad 3.1
print("Zad 3.1")
L=list(input("Vvedite chislo : "))
a=L[0]
L[0]=L[len(L)-1]
L[len(L)-1]=a
print(L) 
#Zad 3.2
print('Zad 3.2')
L=list(input("Vvedite spisok : "))
P=list(range(6))
K=list(range(6))
for i in range(6):
    K[i]=L[2*i]
    P[i]=L[2*i+1]
K=sorted(K)
P=sorted(P,reverse=True)
for i in range(6):
    L[2*i]=K[i]
    L[2*i+1]=P[i]
print(L)
#Zad 3.3
print('Zad 3.3')
U=list(range(20))
Y=list(range(10))
X=list(range(10))
U=sorted(U)
print(U)
for i in range(10):
    X[i]=U[i]
    Y[i]=U[19-i]
print(X,Y) 
#Zad 3.5
print('Zad 3.5')
a=0
L=input('Vvedite stroku : ')
for i in range(len(L)):
    if 48<ord(L[i])<57:
        a+=1
print(a)
#Zad 3.6
print('Zad 3.6')
a=0
L=input('Vvedite stroku : ')
for i in range(len(L)):
    print(ord(L[i]))
    if 65<=ord(L[i])<=90:
        a+=1
print(a)
#Zad 3.7
print('Zad 3.7')
a=0

L=input('Vvedite stroku : ')
for i in range(len(L)-1):
    if ord(L[i+1])==32 and L[i+1]!=L[i]:
            a+=1
if L[len(L)-1]==' ':
    a-=1
print(a)
#Zad 3.8
print('Zad 3.8')
X=5; Y=8; Z=12; W=3
i=X
X=W
W=Y
Y=Z
Z=i
print(X,Y,Z,W) 
#Zad 3.9
print('Zad 3.9')
L=8,15,26
P=list(L)
n=int(input('Vvedite nomer elementa na zamenu : '))
P[n]=int(input('Vvedite zamenu :'))
L=L[0:n]+(P[n],)+L[n+1:len(L)]
L=tuple(P)
print(L)
#Zad 3.10
print('Zad 3.10')
Name={}
Faculty={}
GradYear={}
a=int(input('Vvedite kolichestvo studentov : '))
for i in range(a):
    s=input("Enter student's surname : ")
    Name[s]=input("Enter student's name : ")
    Faculty[s]=input("Enter student's faculty : ")
    GradYear[s]=int(input("Enter student's graduation year : "))
k=input('Search by surname \nEnter surname here: ')
print("Student's name :",Name[k],"\nStudent's faculty : ",Faculty[k],"\nStudent's graduation year :",GradYear[k])
    
#Zad 3.11
print('Zad 3.11')
Chisla=dict([(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten')])
a=int(input('Enter value in range between 0 and 10 : '))
print(Chisla[a])
#Zad 3.12
s=input('Enter values name : ')
Chisla=dict([(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten')])
for i in range(10):
    if Chisla[i+1]==s:
        print(i+1)
#Zad 3.13
print('Zad 3.13')
Zifri=dict([(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten')])
ChislaDec=dict([(20,'twenty'),(30,'thirty'),(40,'forty'),(50,'fifty'),(60,'sixty'),(70,'seventy'),(80,'eighty'),(90,'ninty')])
Chisla=dict([(11,'eleven'),(12,'twelve'),(13,'thirteen'),(14,'fourteen'),(15,'fifteen'),(16,'sixteen'),(17,'seventeen'),(18,'eighteen'),(19,'nineteen'),(20,'twenty')])
a=int(input('Enter value between 0 and 100 : '))
b=0
if -100<a<0:
    b=1
    a=-a
if 0<a<10:
    if b==0:
        print(Zifri[a])
    else:
        print('minus',Zifri[a])
else:
    if 10<a<=20:
        if b==0:
            print(Chisla[a])
        else:
            print('minus',Chisla[a])
    else:
        if 20<a<100:
            if b==0:
                print(ChislaDec[a//10*10],Zifri[a%10])
            else:
                print('minus',ChislaDec[a//10*10],Zifri[a%10])
        else:
            print('Value out of range')

#Zad 3.14
print('Zad 3.14')
L=[1,2,3,4,5,6,7,8,9,10]
K=['one','two','three','four','five','six','seven','eight','nine','ten']
S=list(zip(L,K))
print(S)

#Zad 3.15
print('Zad 3.15')
N=int(input('Vvedite kolichestvo chisel v spiske : '))
L=list(range(N))
for i in range(N):
    L[i]=100/(random.randrange(1000)+1)
L=list(filter(lambda x: x<0.5,L))
print(L)
'''
#Zad 3.16
print('Zad 3.16')
L=list(range(40))
for i in range(20):
    L[2*i]=random.randrange(100)
    L[2*i+1]=str(random.randrange(100))
a=0;b=0
for i in range(40):
    if type(L[i])==int:
        a+=1
    else:
        b+=1
N=list(range(a+1))
S=list(range(b+1))
a=0;b=0
for i in range(40):
    if type(L[i])==int:
        N[a]=L[i]
        a+=1
    else:
        S[b]=L[i]
        b+=1
print(N,S)