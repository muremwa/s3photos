from rest_framework.serializers import ModelSerializer, URLField

from .models import Post


class PostSerializer(ModelSerializer):
    liking_url = URLField()

    class Meta:
        model = Post
        fields = '__all__'
