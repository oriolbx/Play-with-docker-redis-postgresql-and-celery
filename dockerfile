FROM python:3.7
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/test_celery
WORKDIR /app/
RUN pip install -r requirements.txt
RUN pip install --upgrade https://github.com/celery/celery/tarball/master