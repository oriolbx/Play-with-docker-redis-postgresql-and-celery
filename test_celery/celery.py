from celery import Celery

# SET UP CELERY
app = Celery(
    'test_celery',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['test_celery.tasks']
)