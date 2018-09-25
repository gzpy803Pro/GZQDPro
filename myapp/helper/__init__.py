from redis import Redis
import logging

rd_ = Redis(host='127.0.0.1', db=8)


# 设置日志等级
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s %(name)s %(lineno)d: %(message)s',
                    datefmt='%Y-%m-%d',
                    filename='mm.log',
                    filemode='a')

# 获取 Django的settings.py文件中设置的mdjango日志记录器
mdjango = logging.getLogger('mdjango')

