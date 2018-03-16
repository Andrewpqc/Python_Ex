import requests
import time
url1 = "http://120.77.220.239:8002/api/grade/?xnm=2017&xqm=3"
headers1 = {
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Bigipserverpool":"89172160.20480.0000",
    "Jsessionid":"45D7E7DA2E7C05218ED95B70D99A9761",
    "Sid":"2016211129"
}

data={
"_search":False,
"nd":"1520853209939",
"queryModel.currentPage":"1",
"queryModel.showCount":"15",
"queryModel.sortName":"",
"queryModel.sortOrder":"asc",
"time":"0",
"xnm":"2017",
"xqm":"3"
}
time1=time.time()
r2 = requests.get(url1, headers=headers1)
time2=time.time()

print(r2.json())
print("time:",time2-time1)