# coding=utf-8
from __future__ import absolute_import
from celery import Celery

app = Celery('projc', include=['projc.tasks'])
app.config_from_object('projc.celeryconfig')


if __name__ == '__main__':
    app.start()
