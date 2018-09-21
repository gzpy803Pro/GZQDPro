from django.http import HttpResponse
from django.shortcuts import render

from art.models import BookModel


# Create your views here.
def show(request, id):
    book = BookModel.objects.get(pk=id)
    return render(request, 'book/show.html', locals())

    # return HttpResponse('<h1>show- &gt;'+book.name+'</h1><hr><img src="'+book.cover.url+'">',
    #                     content_type='text/html;charset=utf-8', status=200)