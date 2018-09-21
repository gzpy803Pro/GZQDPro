from django.http import HttpResponse
from django.shortcuts import render

from art.models import BookModel
from helper import week_rank


# Create your views here.
def show(request, id):

    # 加入到周排行中
    week_rank.add_rank(id)

    book = BookModel.objects.get(pk=id)

    # 获取前5的周点击排行
    rank_ids = week_rank.get_week_rank_ids(5)
    rank_books = [BookModel.objects.get(pk=id_) for id_ in rank_ids]

    return render(request, 'book/show.html', locals())

    # return HttpResponse('<h1>show- &gt;'+book.name+'</h1><hr><img src="'+book.cover.url+'">',
    #                     content_type='text/html;charset=utf-8', status=200)