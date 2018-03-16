import redis
import json
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("hhh",1)
print(r.get("hhh"))
r.set("hhh",2)
print(r.get("hhh"))

