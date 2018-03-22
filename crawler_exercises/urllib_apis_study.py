from urllib import request
# sourceUrl="http://www.baidu.com/?key1=hhh&key2=a b"
# quoteUrl=request.quote(sourceUrl)
# # http%3A//www.baidu.com/%3Fkey1%3Dhhh%26key2%3Da%20b
# unquoteUrl=request.unquote(quoteUrl)
# # http://www.baidu.com/?key1=hhh&key2=a b
# unquotetobyte=request.unquote_to_bytes(quoteUrl)
# b'http://www.baidu.com/?key1=hhh&key2=a b'

# import requests
# from pprint import pprint
# r=requests.get('https://api.github.com/user')
# pprint(r.headers)

# request.urlopen(url="http://www.baidu.com",timeout=0.01)
from urllib.parse import urlencode
d={'a':1,'b':"h?h",'c':"哈哈"}
print(urlencode(d))
