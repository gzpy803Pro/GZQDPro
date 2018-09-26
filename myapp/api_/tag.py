from rest_framework import serializers, viewsets


from art.models import TagModel


class TagSerializer(serializers.HyperlinkedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = TagModel
        fields = ('id', 'title', 'add_time')


class TagViewSet(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer

