# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:10:18 2019

@author: Магистр
"""
'''
#Zad 4.1
print('Zad 4.1')
fw='H:\\Dolya\\Python_Students\\Mahotka\\001.txt'
f=open(fw,'w')
N=int(input('Kolichestvo strok :'))
for i in range(N):
    s=input('Vvedite stroku : ')
    f.write(s+'\n')
f.close()
print('Zapis zavershena') 
#Zad 4.2
print('Zad 4.2')
print("Vvedite spisok iz 12 elementov : ")
L=list(range(12))
for i in range(12):
    L[i]=int(input('Element : '))
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
fw='J:\\Dolya\\Python_Students\\Mahotka\\001.txt'
f=open(fw,'w')
f.write(str(L))
f.close 
fw='J:\\Dolya\\Python_Students\\Mahotka\\001.txt'
f=open(fw,'r')
S=f.read()
Sum=0
for i in range(len(S)):
    if S[i].isdigit()==True:
        Sum=Sum+int(S[i])
print(Sum)
f.close 
#Zad 4.3
print('Zad 4.3')
D={'dog':'sobaka','cat':'koshka','light':'svet','wawe':'volna','think':'dumat','do':'delat','rush':'speshka','down':'vniz','Cash':'nalichka','mine':'moj'}
S=sorted(list(D.items()))
fw='J:\\Dolya\\Python_Students\\Mahotka\\002.txt'
f=open(fw,'w')
for i in range(len(S)):
    f.write(str(S[i][0])+','+str(S[i][1])+'\n')
f.close
fw='J:\\Dolya\\Python_Students\\Mahotka\\002.txt'
f=open(fw,'r')
D2={}
for i in f.readlines():
    key,val=i.strip().split(',')
    D2[key]=val
print(D2)
f.close 
#Zad 4.4
print('Zad 4.4') 
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
A=ListInput('A')
B=ListInput('B')
print(Scalar(A,B)
#Zad 4.5
print('Zad 4.5')
def Sochet(n,m):
    if (m==1):
        return n
    else:
        if (n==m+1):
            return n
        else:
            return (Sochet(n-1,m-1)+Sochet(n-1,m))
print(Sochet(20,14))'''
import sys
sys.path.append("/media/ihor/E239-1272/Dolya/Python_Students/Mahotka/Modules/4.7")
sys.path.append("/media/ihor/E239-1272/Dolya/Python_Students/Mahotka/Modules/4.7")
import TheModule
import TheModule2
print(TheModule2.sum3(1,2,3,2))


