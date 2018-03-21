import redis
conn = redis.Redis()
#在python客户端执行Zadd命令的时候需要先输入成员，再输入分量
conn.zadd("sort_set_key", "a", 1, "b", 2, "c", 3)
print(conn.zcard("sort_set_key"))
print(conn.zincrby("sort_set_key", "b", 5))
print(conn.zscore("sort_set_key", "a"))
print(conn.zrank("sort_set_key", "c"))
print(conn.zcount("sort_set_key", 1, 3))
print(conn.zrem("sort_set_key", "b"))
print(conn.zrange("sort_set_key", 0, -1, withscores=True))

conn.zadd("zset_1","a",1,"b",2,"c",3)
conn.zadd("zset_2","b",3,"c",5,"d",4)
#aggregate指定聚合运算使用的聚合函数，备选函数有min,max,sum.默认使用的是sum
conn.zinterstore("zset_3",["zset_1","zset_2"],aggregate="min")
print(conn.zrange("zset_3",0,-1,withscores=True))

#用户也可以把集合传给zinterstore,zunionstore,
# redis会把他们看做分值全为１的成员处理
conn.sadd("set1","x","y","z")
conn.zinterstore("set_and_zset",["set1","zset_1","zset_2"],aggregate="max")
print(conn.zrange("set_and_zset",0,-1,withscores=True))

conn.zunionstore("zset_4",["zset_1","zset_2"],aggregate="max")
print(conn.zrange("zset_4",0,-1,withscores=True))
conn.delete("sort_set_key","zset_1","zset_2","zset_3","zset_4","set_and_zset")


