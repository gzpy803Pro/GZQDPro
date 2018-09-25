from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


# 设置Celery启动时的环境变量
from GZQDPro import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GZQDPro.settings')

app = Celery('QDCelery')
app.config_from_object('django.conf:settings')

# 自动查询异步任务
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)