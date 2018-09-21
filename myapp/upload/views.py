import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from GZQDPro import settings


@csrf_exempt  # 不验证csrf_token
def upload_photo(request):
    result = {'code':200, 'msg':'文件上传成功'}
    if request.method == 'POST':
        # 获取上传文件的对象
        photoFile: InMemoryUploadedFile = request.FILES.get('photo')
        if not photoFile:
            result['code'] = 202
            result['msg'] = 'photo请求参数(File)必须提供！'
        else:
            # 确认文件上传存储在服务器的位置(目录)
            photo_dir = os.path.join(settings.MEDIA_ROOT, 'user')
            file_name = str(uuid.uuid4()).replace('-','')+os.path.splitext(photoFile.name)[-1]

            with open(os.path.join(photo_dir, file_name), 'wb') as f:   # TextIOWrapper
                for chunk in photoFile.chunks():
                    f.write(chunk)

            result['path'] = 'upload/user/'+file_name
    else:
        result['code'] = 201
        result['msg'] = '文件上传，只支持POST方法'
    return JsonResponse(result)