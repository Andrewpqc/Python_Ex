#-*- coding:utf-8 -*-
#!/usr/bin/python
import pprint
sequence=[]
while True:
    ch=input("please input 'S' or 'T'.(input other char  to cancel!)")
    if ch=='' or (ch!="S" and ch!="T"):
        break
    else:
        sequence.append(ch)

T_count=sequence.count('T')#T的数目
total_count=len(sequence)#总数目
Rt=T_count/total_count
print("Rt:",Rt)

g=1#初始的连数
pre=sequence[0]
for i in sequence[1:]:
    if pre!=i:
        g+=1
    pre=i
print("连数:",g)
Ch=(g-1)/total_count
print("行转换率：",Ch)

print("类型：")
if Rt<=0.3:
    print("练习型")
elif Rt>=0.7:
    print("讲授型")
elif Ch>=0.4:
    print("对话型")
elif 0.3<Rt<0.7 and Ch<0.4:
    print("混合型")
else:
    print("未知")


