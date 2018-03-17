from celery import Celery
app=Celery("celery_proj",broker="amqp://",
           backend="redis://",include=['celery_proj.tasks'])
# app.config_from_object("celery_config")
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()