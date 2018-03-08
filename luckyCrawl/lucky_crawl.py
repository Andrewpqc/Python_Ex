import requests
import json
def tofile(d, f):
    print("愿望ID:" + d["info"]["id"], file=f)
    print("愿望内容:" + d["info"]["content"], file=f)
    print("cardno:" + d["info"]["cardno"], file=f)
    print("用户名:" + d["user"]["name"], file=f)
    print("学校：" + d["user"]["school"], file=f)
    print("学院:" + d["user"]["room"], file=f)
    print("-------------------------------\n", file=f)

url = 'https://web.wutnews.net/lucky/index/change'
headers1 = {
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    "Cookie":
    "Hm_lvt_6937a39e5483039406a2ae45f8f1f392=1520487897,1520501099,1520517626;"
    " PHPSESSID=bi9ctcenq39b30iu8am3bu6fg7;"
    " Hm_lpvt_6937a39e5483039406a2ae45f8f1f392=1520517679"
}
#全局变量
total = 0#记录不重复的愿望数
l=[]
with open("huashi.txt", 'a') as ccnu_f:
    with open("wuli.txt", "a") as wuli_f:
        with open("wishes.txt", "a") as f:
            for i in range(10000000000):
                print("iteration index:", i)
                if i % 10 == 0:
                    ccnu_f.flush()
                    wuli_f.flush()
                    f.flush()
                r1 = requests.get(url, headers=headers1)
                d = json.loads(r1.content.decode())
                wish_id = d["info"]["id"]
                if wish_id not in l:
                    total += 1  #记录不同愿望数量
                    l.append(wish_id)
                    print("total:", total)
                    print(wish_id)
                    tofile(d, f)
                    if d["user"]["school"].strip() == "华小师":  #华师的学生
                        tofile(d, ccnu_f)
                    else:  #武理的学生
                        tofile(d, wuli_f)
