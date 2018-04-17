import base64,json

d={"id":1}
sce=base64.b64encode(json.dumps(d).encode("utf-8"))
print(sce)
ori=base64.b64decode(sce)
print(json.loads(ori.decode("utf-8")).get("id"))