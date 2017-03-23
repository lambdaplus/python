# coding=utf-8
from __future__ import absolute_import

from .celery import app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task(bind=True)
def div(self, x, y):
    logger.info(
        '''
        Executing task : {0.id}
        task.args      : {0.args!r}
        task.kwargs    : {0.kwargs!r}
        '''.format(self.request)
    )
    try:
        res = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=3, max_retries=3)
    else:
        return res
