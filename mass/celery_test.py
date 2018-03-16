from celery import Celery
celery= Celery('tasks', broker='pyamqp://guest@localhost//')
@celery.task
def add(x, y):
    return x + y


# from celery import Celery
# from celery import task
#
# celery = Celery('tasks', broker='amqp://guest@localhost//')