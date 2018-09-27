from .tasks import hello
import time
from celery.utils.log import get_task_logger

# define logger
logger = get_task_logger(__name__)

if __name__ == '__main__':
    result = hello.delay('...darkness my old friend...')
    logger.info(result.get())
