import requests
from bs4 import BeautifulSoup
url1 = 'http://account.ccnu.edu.cn/cas/login'
headers1 = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

#请求首先，得到JSESSIONID
r1=requests.get(url1,headers=headers1)
print("JSESSIONID:",r1.cookies.get("JSESSIONID"))

#根据上面得到的JSESSIONID构造第２个请求的url
url2=url1+";jsessionid="+r1.cookies.get("JSESSIONID")


soup = BeautifulSoup(r1.content.decode(), 'html.parser')
last_section=soup.find("section",attrs={"class":"row btn-row"})
execution=last_section.find('input',attrs={"name":"execution"},recursive=False).get("value")
lt=last_section.find('input',attrs={"name":"lt"},recursive=False).get("value")
print("execution:",execution)
print("lt:",lt)
headers2={
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
            'cache-control': "no-cache",
            'connection': "keep-alive",
            'content-type': "application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
            "Cookie":"JSESSIONID=" + r1.cookies.get("JSESSIONID"),
            "Referer":"https://account.ccnu.edu.cn/cas/login",
            'host': "account.ccnu.edu.cn",
            'origin': "https://account.ccnu.edu.cn",
            'pragma': "no-cache",
          }

data={
        "username":"2016210942",
        "password":"muxistudio",
        "lt":lt,
        "execution": execution,
        "_eventId":"submit",
        "submit":"LOGIN"
}
r2 = requests.post(url2,headers=headers2, data = data)
print("real cookie:",r2.cookies)
