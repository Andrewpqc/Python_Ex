"""
redis的字符串操作
"""
import redis
conn = redis.Redis()
"""
redis的incr和decr操作
"""
conn.set("n1", 1)
print(conn.get("n1"))
conn.incr("n1")
print(conn.get("n1"))
conn.incr("n1", 5)
print(conn.get("n1"))
conn.incrby("n1", 3)
print(conn.get("n1"))
conn.incrbyfloat("n1", 2.5)
print(conn.get("n1"))
# conn.decr("n1") #这里由于n1之前是浮点数，自减1会报错
print(conn.get("n1"))
# conn.decr("n1",5)　#同上面的道理，减少一个整数会报错
print(conn.get("n1"))
# conn.incr("n1",3)　#自加整数也会报错
print(conn.get("n1"))
conn.incrbyfloat("n1", 2.3)
print(conn.get("n1"))  #自加浮点数没事
conn.delete("n1")
print(conn.get("n1"))
"""
从上面的命令可知，redis-py这个包不允许不同类型的数的运算
set k 1
get k
incr k
incrby k d
incrbyflaot k fd
decr k
decrby k d
注意:没有decrbyfloat命令
"""
"""
redis的子串操作和二进制位操作
"""
conn.set("key", "vaule")
print(conn.get("key"))
conn.append("key", " hhh")
print(conn.get("key"))
"""
substr,getrange作用是一样的
"""
subStr1 = conn.getrange("key", 6, 8)
print(subStr1)
subStr2 = conn.substr("key", 6, 8)
print(subStr2)
conn.setrange("key", 0, "V")
print(conn.get("key"))
