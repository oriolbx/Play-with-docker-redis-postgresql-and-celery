from celery import Celery
from celery.schedules import crontab

# SET UP CELERY
app = Celery(
    'test_celery',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['test_celery.tasks']
)
app.conf.beat_schedule = {
    'greet-every-30-seconds': {
        'task': 'test_celery.tasks.hello',
        'schedule': 30.0,
        'args': ['...darkness my old friend...'],
    },
}
app.conf.timezone = 'UTC'
