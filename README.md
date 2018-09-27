# Usage

## Initialize containers of Redis, Python app and PostgreSQL database

```bash
docker-compose up
```

## EXECUTE celery tasks

Once the containers are running, open a new terminal, go to the same folder and execute the next command:

```bash
docker exec -it test_celery_worker_1 python -m test_celery.run_tasks
```