from celery_app.task1 import add
from celery_app.task2 import sub

a=add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
b=sub.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)
print(a.get())
print(b.get())
print('hello world')