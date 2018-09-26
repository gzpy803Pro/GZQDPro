from rest_framework import serializers, viewsets


from art.models import CategoryModel


class ChildCategorySerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'title', 'parent_id')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    childs = ChildCategorySerilizer(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = ('id', 'title','childs')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer

