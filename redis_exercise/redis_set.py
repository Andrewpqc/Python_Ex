"""
redis集合操作基本api
sadd
srem
sismember
scard
smembers
srandmember
spop
smove
sdiff
sdiffstore
sinter
sinterstore
sunion
sunionstore
"""
import redis
conn=redis.Redis()
print("成功添加的元素的个数：",conn.sadd("set_key1","a","b","c","a"))
print("成功移除的元素：",conn.srem("set_key1","a","d"))
print("当前集合中所有的元素：",conn.smembers("set_key1"))
print("b在当前集合中吗：",conn.sismember("set_key1","b"))
print("当前集合的元素个数：",conn.scard("set_key1"))
print("当前集合中的随机的一个元素",conn.srandmember("set_key1"))
conn.delete("set_key1")

conn.sadd("s1","a","b","c")
conn.sadd("s2","c","d","e")
print(conn.sdiff("s1","s2"))#s1中独有的元素
print(conn.sinter("s1","s2"))#s1,s1的交际
print(conn.sunion("s1","s2"))#s1,s2的并集


conn.delete("s1","s2")