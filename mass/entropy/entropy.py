import pprint
from math import log
dict_database = dict().fromkeys(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"),
                                0)  #存储每个字符出现的次数
total_count = 0  #存储文章中总的字符数
entropy = 0  #信息熵
with open("example.txt") as f:
    for line in f:
        for i in line:
            total_count += 1
            if i == " ":
                dict_database["_"] += 1
            elif i.isalpha():
                dict_database[i] += 1
            else:
                pass
print("文章中每个字符的出现次数：")
pprint.pprint(dict_database)
print("total count 2",sum(dict_database.values()))
for k, v in dict_database.items():
    dict_database[k] = v / total_count
print("total count:",total_count)

print("文章中每个字符出现的频率：")
pprint.pprint(dict_database)
print("sum:",sum(dict_database.values()))

for v in dict_database.values():
    if v>0:#不能对非正数取对数，这里要去掉频率为0的字母
    	entropy += -v*log(v, 2)
print("信息熵：",entropy)
