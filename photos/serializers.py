from rest_framework.serializers import ModelSerializer, URLField, CharField

from .models import Post


class PostSerializer(ModelSerializer):
    liking_url = URLField()
    clean_time = CharField(source='get_clean_time')

    class Meta:
        model = Post
        fields = '__all__'
