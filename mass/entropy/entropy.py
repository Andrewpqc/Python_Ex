import pprint
from math import log
dict_database = dict().fromkeys(list("abcdefghijklmnopqrstuvwxyz_"),
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
                dict_database[i.lower()] += 1
            else:
                pass
print("文章中每个字符的出现次数：")
pprint.pprint(dict_database)
for k, v in dict_database.items():
    dict_database[k] = v / total_count
print("文章中每个字符出现的频率：")
pprint.pprint(dict_database)

for v in dict_database.values():
    entropy += -log(v, 2)
print("信息熵：")
print(entropy)
