import datetime
now = datetime.datetime.now()
print(now)

import time
now_t=time.time()
print(now_t)

time_t2=time.localtime()
print(time_t2.tm_year)
print(time_t2)
a=2
print(1<a<3)


now=datetime.datetime.now().date()
print(type(now.year))
date=datetime.date(2015, 10, 28)
data2=datetime.date(2019,3,3)
print(data2>now>date)