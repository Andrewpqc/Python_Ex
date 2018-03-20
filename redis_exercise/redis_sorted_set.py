import redis
conn = redis.Redis()
#在python客户端执行Zadd命令的时候需要先输入成员，再输入分量
conn.zadd("sort_set_key","a",1,"b",2,"c",3)
print(conn.zcard("sort_set_key"))
print(conn.zincrby("sort_set_key","b",5))
print(conn.zscore("sort_set_key","a"))
print(conn.zrank("sort_set_key","c"))
print(conn.zcount("sort_set_key",1,3))
print(conn.zrem("sort_set_key","b"))
print(conn.zrange("sort_set_key",0,-1,withscores=True))

