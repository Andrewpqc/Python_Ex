"""
redis的列表操作
"""
import redis
conn = redis.Redis()
conn.rpush("list_key","a")
conn.lpush("list_key","b")
conn.rpush("list_key","c")
conn.ltrim("list_key",2,-1)
print(conn.lrange("list_key",0,-1))
print(conn.lindex("list_key",1))
conn.lpop("list_key")
conn.rpop("list_key")
conn.delete("list_key")

conn.lpush("list_key2","1")
conn.lpush("list_key2","2")
conn.lpush("list_key2","3")
conn.lpush("list_key2","4")
conn.lpush("list_key2","5")
print(conn.ltrim("list_key2",0,2))
conn.delete("list_key2")