def app(environ,start_response):
    print(environ)#这是一个字典，存放的是该次请求的相关信息
    data=b"hello,world\n"
    start_response("200 OK",[
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

def app2(environ,start_response):
    return b"hello,world!"