import requests
response=requests.get("http://www.baidu.com")
print(response.text)
print("__________________-")
print(response.content.decode("utf-8"))
