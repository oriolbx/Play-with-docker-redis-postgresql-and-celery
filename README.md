# EXECUTE celery tasks

Once celery workers are ready, execute next command to produce the messages

```bash
docker exec -it test_celery_worker_1 python -m test_celery.run_tasks
```