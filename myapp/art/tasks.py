from GZQDPro.celery import app
from helper import rd_
from art.models import BookModel
from user.models import UserProfile


@app.task
def qbuy(user_id, book_id):
    user = UserProfile.objects.get(pk=user_id)
    book = BookModel.objects.get(pk=book_id)

    if rd_.hlen('qbuy_map') < 5:
        # 防止一个用户抢多本书
        if not rd_.hexists('qbuy_map', user_id):
            rd_.hset('qbuy_map', user_id, book_id)
            return '%s 抢购 %s 成功' % (user.nick_name, book.name)

    return '%s 抢购 %s 失败' % (user.nick_name, book.name)