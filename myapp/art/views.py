import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from art.models import BookModel
from helper import week_rank

import time

from art.tasks import qbuy
from helper import rd_

# Create your views here.
@cache_page(10, cache='art_page', key_prefix='art')
def show(request, id):
    time.sleep(2)
    # 加入到周排行中
    week_rank.add_rank(id)

    book = BookModel.objects.get(pk=id)

    # 获取前5的周点击排行
    rank_ids = week_rank.get_week_rank_ids(5)
    rank_books = [BookModel.objects.get(pk=id_) for id_ in rank_ids]

    return render(request, 'book/show.html', locals())

    # return HttpResponse('<h1>show- &gt;'+book.name+'</h1><hr><img src="'+book.cover.url+'">',
    #                     content_type='text/html;charset=utf-8', status=200)


def qbuy_book(request, book_id):
    msg = {'code': 201, 'msg': '正在抢购...'}
    # 判断是否被抢完
    if rd_.hlen('qbuy_map') >= 5:
        msg['code'] = 202
        msg['msg'] = '已抢完'
    else:
        # 获取当前用户信息
        login_user = request.session.get('login_user')
        if not login_user:
            msg['code'] = 301
            msg['msg'] = '用户未登录'
        else:
            # 开始抢购
            user_id = json.loads(login_user).get('id')
            qbuy.delay(user_id, book_id)

    return JsonResponse(msg)


def query_qbuy(request, book_id):
    msg = {'code':201, 'msg': '正在抢购'}
    # 获取当前用户信息
    login_user = request.session.get('login_user')
    if not login_user:
        msg['code'] = 301
        msg['msg'] = '用户未登录'
    else:
        user_id = json.loads(login_user).get('id')

        # 判断当前用户是否抢到
        if rd_.hexists('qbuy_map', user_id):
            qbuy_book_id = rd_.hget('qbuy_map', user_id)
            print('---', qbuy_book_id, book_id)
            if int(qbuy_book_id) == int(book_id):
                msg['code'] = 200
                msg['msg'] = '抢购成功'
            else:
                msg['code'] = 203
                msg['msg'] = '抢购失败，每位用户只能抢购一本小说.'
        else:
            #  抢购失败 或 正在抢
            if rd_.hlen('qbuy_map') >=5:
                msg['code'] = 202
                msg['msg'] = '抢购失败，已被抢完,等待下次抢活动开启.'

    return JsonResponse(msg)