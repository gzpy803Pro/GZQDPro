from rest_framework import routers


from api_.tag import TagViewSet
from api_.category import CategoryViewSet
from api_.book import BookViewSet


api_router = routers.DefaultRouter()  # 创建api路由

api_router.register('tag', TagViewSet)
api_router.register('category', CategoryViewSet)
api_router.register('book', BookViewSet)
