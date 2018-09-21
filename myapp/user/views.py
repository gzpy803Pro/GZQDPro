import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms import UserForm

# Create your views here.
def regist(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 验证form的数据
        if form.is_valid():
            user = form.save()
            # 将登录用户的信息存放到缓存中(session)
            return redirect('/')
        else:
            # errors = form.errors  # 网页源码的错误信息(ul-li)
            errors = json.loads(form.errors.as_json())
            print(errors)
    return render(request, 'user/regist.html', locals())
    # return HttpResponse(json.dumps({'name':'disen'}),
    #                     content_type='application/json')
