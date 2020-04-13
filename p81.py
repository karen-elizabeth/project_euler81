# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:41:33 2020

@author: storm
"""



with open('p081matrix.txt') as file1:
    numbers = file1.read()

numbers = numbers.strip().split('\n') 

data = [] 

for line in numbers:
    row = line.split(',')
    row = [int(i) for i in row]
    data.append(row)
    
rdata = []

for i in range(80):
    newrow=[]
    m = i
    n = 0
    while m >= 0:
        newrow.append(data[m][n])
        m = m - 1
        n = n + 1
    rdata.append(newrow)
    
for j in range(1,80):
    newrow=[]
    m = 79
    n = j
    while n < 80:
        newrow.append(data[m][n])
        m = m - 1
        n = n + 1
    rdata.append(newrow)

rdata[157][0] = rdata[157][0] + rdata[158][0]
rdata[157][1] = rdata[157][1] + rdata[158][0]

for k in range(156,78,-1):
    rowl = len(rdata[k])-1
    rdata[k][0] = rdata[k][0]+rdata[k+1][0]
    rdata[k][rowl] = rdata[k][rowl]+rdata[k+1][rowl-1]
    for p in range (1,rowl):
        rdata[k][p] = rdata[k][p] + min(rdata[k+1][p-1], rdata[k+1][p])
 

for q in range(78,-1,-1):
    rowl = len(rdata[q])
    for r in range (rowl):
        print(q,r)
        rdata[q][r] = rdata[q][r] + min(rdata[q+1][r], rdata[q+1][r+1])
    
 
