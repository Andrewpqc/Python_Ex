import redis
conn=redis.Redis()
conn.set("a",1)
conn.set("b",2)
a,b=conn.mget("a","b")
print(a,b)