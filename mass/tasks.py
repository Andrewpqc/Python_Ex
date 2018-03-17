from celery import Celery
celery= Celery('tasks',backend='rpc://', broker='pyamqp://guest@localhost//')

@celery.task
def add(x, y):
    return x + y


