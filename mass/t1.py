
#!/bin/bash
from math import sqrt
s1=[80,80,85,80,85,90,60,50,70,78,83,81,72,70,95,87,88,82,76,65,68,55,68,91,86,71,73,64,66,76]
s2=[80,75,85,80,80,78,77,65,54,56,98,94,86,88,78,70,65,68,92,82,83,65,69,59,74,86,89,90,70,77]
average1=sum(s1)/30
average2=sum(s2)/30
print("S1,S2的平均值分别是：",average1,average2)
variance1=0
variance2=0
for i in s1:
    variance1+=abs(i-average1)**2
for j in s2:
    variance2+=abs(j-average2)**2
variance1=variance1/30
variance2=variance2/30
standard_deviation1=sqrt(variance1)
standard_deviation2=sqrt(variance2)
print("S1,S2的方差分别为：",variance1,variance2)
print("S1,S2的标准差分别为：",standard_deviation1,standard_deviation2)
union_variance=0
for i,j in zip(s1,s2):
    union_variance+=(i-average1)*(j-average2)
union_variance=union_variance/30
print("S1,S2的共分散为：",union_variance)
g=union_variance/standard_deviation1*standard_deviation2
print("S1,S2的再测信度系数为：",g)