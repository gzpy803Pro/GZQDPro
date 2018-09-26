from rest_framework import serializers, viewsets

from art.models import  BookModel
from api_.tag import TagSerializer
from api_.category import ChildCategorySerilizer


class BookSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = ChildCategorySerilizer(many=False, read_only=True)

    class Meta:
        model = BookModel
        fields = ('id',
                  'name',
                  'summary',
                  'content',
                  'cover',
                  'author',
                  'tags',
                  'category')


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer