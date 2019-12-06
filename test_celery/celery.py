from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://khamiruf:khamiruf123@localhost/khamiruf_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
