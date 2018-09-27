from __future__ import absolute_import
from test_celery.celery import app
import time
import requests
import psycopg2
from celery.utils.log import get_task_logger

# define logger
logger = get_task_logger(__name__)

# connect to PostgreSQL database
conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="postgres"
)

# create a cursor
cur = conn.cursor()


@app.task(bind=True, default_retry_delay=10)
def hello(self, i):
    # execute a statement
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    logger.info(db_version)

    # close the communication with the PostgreSQL
    cur.close()
    logger.info('Database connection closed.')
    return f'hello {i}'
