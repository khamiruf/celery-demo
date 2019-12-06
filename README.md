# celery-demo

This is the demo project for article [Distribute Tasks with Python Celery and RabbitMQ](https://tests4geeks.com/tutorials/distribute-tasks-with-python-celery-and-rabbitmq/)

#### For Celery > v4:
- install eventlet prior with (`pip install eventlet`)
- spawn celery worker with:
```
celery -A test_celery worker -l info -P eventlet
```


#### Take note of **Best Practices**:
> `https://denibertovic.com/posts/celery-best-practices/`