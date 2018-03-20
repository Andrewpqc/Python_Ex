import redis
conn = redis.Redis()
conn.hmset("hash_key", {"k1": "v1", "k2": "v2", "k3": "v3"})
print(conn.hmget("hash_key", "k1"))  #一次获取一个值
print(conn.hmget("hash_key", ["k1", "k2"]))  #可以一次获取多个键的值
print(conn.hlen("hash_key"))
print(conn.hget("hash_key", "k1"))
print(conn.hgetall("hash_key"))
print(conn.hexists("hash_key", "k1"))
print(conn.hdel("hash_key", "k1", "k2"))  #可以同时删除多个值
print(conn.hexists("hash_key", "k1"))
conn.delete("hash_key")
