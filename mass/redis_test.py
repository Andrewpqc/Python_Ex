import redis
import json
a={"a":1,"b":"asdfg","c":[1,2,3]}
r = redis.Redis(host='localhost', port=6379, decode_responses=True) # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379 r.set('name', 'junxi') # key是"foo" value是"bar" 将键值对存入redis缓存 print(r['name']) print(r.get('name')) # 取出键name对应的值 print(type(r.get('name')))
r.set("hhh",json.dumps(a))
print(json.loads(r.get("hhh"))["a"])

