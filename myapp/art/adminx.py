import xadmin
from xadmin import views

from art.models import TagModel, CategoryModel, BookModel, VolumeSetModel, ChapterModel


# 定制模型
class TagAdmin:
    list_display = ['title', 'add_time']


class CategoryAdmin:
    list_display = ['title', 'add_time', 'parent']


class BookAdmin:
    list_display = ['name',
                    'author',
                    'summary',
                    'content',
                    'category',
                    'tags']

class VolumeSetAdmin:
    list_display = ['name',
                    'add_time',
                    'book',
                    'freeName']


class ChapterAdmin:
    list_display = ['title',
                    'add_time',
                    'char_size',
                    'volume']


# Register your models here.
xadmin.site.register(TagModel, TagAdmin)
xadmin.site.register(CategoryModel, CategoryAdmin)
xadmin.site.register(BookModel, BookAdmin)
xadmin.site.register(VolumeSetModel, VolumeSetAdmin)
xadmin.site.register(ChapterModel, ChapterAdmin)


class GlobalSettings(object):
    # 整体配置
    site_title = '后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'  # 菜单折叠

    # 设置app模块的标题
    apps_label_title = {
        'art': '小说管理'
    }

    # 设置app模块的图标
    apps_icons = {
        'art': 'glyphicon glyphicon-book'
    }

    # 设置模型在后台显示的图标
    global_models_icon = {
        BookModel: 'glyphicon glyphicon-qrcode',
        VolumeSetModel: 'glyphicon glyphicon-tint'
    }


xadmin.site.register(views.CommAdminView,  GlobalSettings)
