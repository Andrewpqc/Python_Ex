import certifi
import urllib3
http=urllib3.PoolManager(cert_reqs="CERT_REQUIRED",ca_certs="/etc/ssl/certs/ca-certificates.crt")
#下面请求https://google.com
# http.request("GET",'https://google.com')#没有任何错误

#下面请求https://expired.badssl.com
http.request("GET",'https://expired.badssl.com')
#抛出urllib3.exceptions.SSLError的错误，说明该网站没有配置安全证书。
