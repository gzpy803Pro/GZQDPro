import uuid
from datetime import datetime

import os
from django.db import models


# Create your models here.
class TagModel(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='名称',
                             db_column='name',
                             unique=True)
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name  # 去掉复数表示
        ordering = ['-add_time', 'title']


class CategoryModel(models.Model):
    title = models.CharField(max_length=20,  # char(20)或varchar(20)
                             verbose_name='名称',
                             unique=True)

    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    # 所属分类
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name='所属分类')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name




class BookModel(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='书名')

    author = models.CharField(max_length=20,
                              verbose_name='作者')

    summary = models.CharField(max_length=100,
                               verbose_name='简介')

    content = models.TextField(verbose_name='作品信息')

    add_time = models.DateTimeField(verbose_name='发布时间',
                                    null=True,
                                    blank=True,
                                    auto_now_add=True)

    def get_filename(self, filename):
        print('------>', filename)
        return filename

    # 依赖PIL库(pillow)
    cover = models.ImageField(verbose_name='封面',
                              upload_to='art/images',
                              null=True,
                              blank=True)   # 相对于MEDIA_ROOT的目录

    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.SET_NULL,
                                 null=True)

    tags = models.ManyToManyField(TagModel, verbose_name='签标')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        newFileName = str(uuid.uuid4()).replace('-', '') + os.path.splitext(self.cover.name)[1]
        self.cover.name = newFileName  # 图片文件名

        super().save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class VolumeSetModel(models.Model):
    f_levels = ((0, '免费'), (1, 'VIP'), (2, '收费'))

    name = models.CharField(max_length=50,
                            verbose_name='卷名')

    free_level = models.IntegerField(verbose_name='免费等级',
                                     choices=f_levels,
                                     default=0)

    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')

    book = models.ForeignKey(BookModel,
                             verbose_name='所属书',
                             on_delete=models.CASCADE)  # 级联删除

    @property
    def freeName(self):  # 返回免费等级的名称
        return self.f_levels[self.free_level][1]

    def __str__(self):
        return self.name + "-" + self.freeName

    class Meta:
        db_table = 't_volume'
        verbose_name = '卷集'
        verbose_name_plural = verbose_name
        ordering = ['add_time']


class ChapterModel(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='标题')

    content = models.TextField(verbose_name='正文')

    add_time = models.DateTimeField(verbose_name='发布时间',
                                    auto_now_add=True)

    char_size = models.IntegerField(verbose_name='字数',
                                    blank=True)

    volume = models.ForeignKey(VolumeSetModel,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.char_size = len(self.content) - self.content.count('<p>')*2  # 统计字数， 去掉<p>和</p>标签的数量
        super(ChapterModel, self).save()

    class Meta:
        db_table = 't_chapter'
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['add_time']
