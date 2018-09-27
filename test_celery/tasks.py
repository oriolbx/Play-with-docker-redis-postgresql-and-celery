from __future__ import absolute_import
from test_celery.celery import app
import time
import requests
import psycopg2
from celery.utils.log import get_task_logger

# define logger
logger = get_task_logger(__name__)

@app.task(bind=True,default_retry_delay=10)
def hello(self, i):
    return f'hello {i}'
