#!/bin/bash
from math import sqrt
X=[80,80,85,80,85,90,60,50,70,78,83,81,72,70,95,87,88,82,76,65,68,55,68,91,86,71,73,64,66,76]
Z=[]
C=[]
average=sum(X)/30
print("X的平均值是：",average)
variance=0
for i in X:
    variance+=abs(i-average)**2
variance=variance/30
print("X的方差：",variance)
standard_deviation=sqrt(variance)
print("X的标准差：",standard_deviation)

print("计算每个学生的Z得分、CEEB得分，分别存入存入Z列表、C列表")
for i in X:
    z=(i-average)/standard_deviation
    Z.append(z)
    c=100*z+500
    C.append(c)
print("Z列表：",Z)
print("C列表：",C)
