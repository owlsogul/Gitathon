# coding=utf-8

from __future__ import absolute_import


# djano 에서 쓰일 setting 지정 아래의 경우 proj/settings.py 를 사용한다는 뜻
import os

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gitathon.settings')
from django.conf import settings  # noqa

# app = Celery('proj',
#              broker='amqp://guest@localhost//',
#              backend='amqp://',
#              include=['proj.tasks'])

app = Celery('gitathon')

# 데이터베이스 Backend이용
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)

# Optional configuration, see the application user guide.
# 문자열로 등록한 이유는 Celery Worker가 Windows를 사용할 경우
# 객체를 pickle로 묶을 필요가 없다는 것을 알려주기 위함입니다.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
