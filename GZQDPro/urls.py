"""GZQDPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin
from art.models import CategoryModel, BookModel


def index(request):
    # 查询一级分类
    cates = CategoryModel.objects.filter(parent__isnull=True).all()


    # 获取当前显示的分类id
    cate_id = int(request.GET.get('cate_id', 0))

    # 查询所有图书(小说)
    if cate_id:
        books = BookModel.objects.filter(category__parent_id=cate_id).all()
    else:
        books = BookModel.objects.all()

    # 实现分页
    paginator = Paginator(books, 2)  # 2表示每页显示的记录数
    pager = paginator.page(int(request.GET.get('page', 1)))  # 获取指定页面的小说

    return render(request,
                  'index.html',
                  locals())  # 将局部变量转成字典


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'', index),
]
